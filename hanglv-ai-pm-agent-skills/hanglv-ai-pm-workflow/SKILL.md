---
name: hanglv-ai-pm-workflow
description: 航旅纵横 AI PM 主路由工作流。Use when the user wants to coordinate Hanglv flight-ticket problem discovery, competitor analysis, diagnosis, PRD drafting, UI/Figma delivery, frontend implementation, design QA, PR review, release gates, Feishu notifications, team workflow operations, or post-launch review. This skill routes work to specialized Hanglv sub-skills with fixed inputs and outputs, instead of doing every step inside one large prompt.
metadata:
  short-description: 航旅机票 AI PM 主路由与产研自动化工作流
---

# 航旅 AI PM 主路由工作流

## 定位

本 skill 只做三件事：

1. 判断用户任务属于哪个产研环节。
2. 调度对应专项子 skill。
3. 串联子 skill 的输入输出，保证证据、状态、交付物和人工确认闭环。

不要把所有细节都塞进主 skill。专项能力交给 8 个子 skill：

| 子 skill | 负责环节 | 固定输出 |
| --- | --- | --- |
| `hanglv-problem-radar-agent` | 原始反馈到问题雷达 | `ProblemRadarReport` |
| `hanglv-competitor-analysis-agent` | 竞品录屏/截图到案例库和参考报告 | `CompetitorCaseLibrary`、`CompetitorReferenceReport` |
| `hanglv-diagnosis-agent` | 问题真实性与根因诊断 | `ProblemDiagnosisReport` |
| `hanglv-prd-agent` | 方案卡与 PRD 初稿 | `SolutionCard`、`PRDDraft` |
| `hanglv-design-delivery-agent` | HTML 原型、截图、Figma/UI 交付 | `DesignDeliveryPackage` |
| `hanglv-frontend-implementation-agent` | 设计交付物到前端代码和 PR | `FrontendImplementationPackage` |
| `hanglv-frontend-qa-agent` | 前端实现验收、差异报告、PR 建议 | `FrontendQAReport` |
| `hanglv-team-workflow-ops-agent` | 飞书通知、状态流转、资产归档、文件触发 | `TeamWorkflowOpsReport` |

## 全局原则

- 始终区分：已确认、推测、待验证。
- 每个关键结论都要能回到证据：用户原声、标签频次、评分、埋点、页面截图、Figma、前端截图、历史 PRD 或业务规则。
- 问题优先级用 P0/P1/P2/P3；置信度用高/中/低，并说明依据。
- 方案必须包含优势与劣势/风险。
- 如果收益无法量化，给计算口径和所需数据，不要编造数字。
- 对航旅纵横机票交易链路，优先保持可信、透明、低阻塞、低理解成本。
- 如输入包含手机号、订单号、身份证、乘机人姓名等敏感信息，输出前必须脱敏。

## 工作流状态

用下面状态判断当前任务走到哪里：

| 状态 | 下一步 |
| --- | --- |
| `raw_feedback` 原始反馈/评价/工单 | 调用 `hanglv-problem-radar-agent` |
| `complaint_file_detected` 下载文件夹发现客诉日报/周报文件 | 调用 `hanglv-team-workflow-ops-agent`，再进入 `hanglv-problem-radar-agent` |
| `competitor_material` 竞品录屏/截图/流程 | 调用 `hanglv-competitor-analysis-agent` |
| `problem_with_competitor_reference` 航旅问题需要竞品参考 | 调用 `hanglv-competitor-analysis-agent` 后再进入诊断或 PRD |
| `problem_card` 已有问题卡 | 调用 `hanglv-diagnosis-agent` |
| `diagnosed_problem` 已诊断问题 | 调用 `hanglv-prd-agent` |
| `prd_or_solution` 已有方案/PRD | 如涉及页面，调用 `hanglv-design-delivery-agent`；否则输出评审意见 |
| `design_ready` 已有 HTML/Figma/UI 稿 | 如需要写前端代码，调用 `hanglv-frontend-implementation-agent` |
| `implementation_ready` 已有前端实现包/测试页面/PR | 调用 `hanglv-frontend-qa-agent` |
| `frontend_ready` 已有测试页面/PR，只需验收 | 调用 `hanglv-frontend-qa-agent` |
| `workflow_state_changed` 需要通知团队或等待确认 | 调用 `hanglv-team-workflow-ops-agent` |
| `launched` 已上线 | 生成复盘，并把 badcase/规则更新建议回流 |

## 路由规则

### 1. 原始反馈、App 评价、客服工单、飞书群摘要

触发条件：

- 用户给 CSV、客服摘要、飞书群消息、App 评价、媒体投诉、用户原声。
- 用户说“帮我看看用户主要问题”“做问题雷达”“从反馈里提炼需求”。
- Codex 定时任务在 `/Users/weizheng/Downloads/hanglv-complaints-inbox/` 发现新的客诉日报/周报 PDF、Word、Markdown 或 CSV。

使用：

- 如果来自下载文件夹自动触发，先调用 `hanglv-team-workflow-ops-agent` 记录文件、归档和状态。
- 调用 `hanglv-problem-radar-agent`。
- 若是 CSV，优先执行共享脚本：`/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/scripts/analyze_reviews.py`。

输出后：

- 如果用户要继续出方案，交给 `hanglv-diagnosis-agent`。
- 如果发现 P0/P1 候选问题，交给 `hanglv-team-workflow-ops-agent` 生成飞书通知草案或发送飞书群提醒。
- 不要把单条吐槽直接包装成需求。

### 2. 竞品录屏、截图、流程与异常 case

触发条件：

- 用户给携程、去哪儿、飞猪、航司 App 等竞品录屏、截图、GIF、流程描述。
- 用户说“记一下竞品怎么做”“沉淀竞品案例”“航旅有类似问题时参考竞品”。
- 航旅当前问题需要参考竞品类似用户画像、购票诉求或异常 case。

使用：

- 调用 `hanglv-competitor-analysis-agent`。

输出后：

- 如果只是沉淀竞品，输出 `CompetitorCaseLibrary`。
- 如果是为航旅问题找参考，输出 `CompetitorReferenceReport`，再交给 `hanglv-diagnosis-agent` 或 `hanglv-prd-agent`。
- 不把竞品做法直接当成航旅应该照搬的方案。

### 3. 团队状态流转、飞书通知、资产归档

触发条件：

- 某个产物生成后需要通知下一岗位确认，例如 UI 审核、前端实现、设计验收、发布确认。
- 用户要求“通知 UI/前端/测试”“飞书群 @ 某人”“记录到需求资产库”。
- 工作流规则有变动，需要同步团队。

使用：

- 调用 `hanglv-team-workflow-ops-agent`。

输出后：

- 输出 `TeamWorkflowOpsReport`，包含状态、owner、确认人、资产路径和飞书通知正文。
- 如果没有真实飞书 webhook 或权限，只输出飞书消息草案，不声称已发送。

### 4. 已有问题卡、问题诊断、候选需求

触发条件：

- 用户已经给了一个候选问题或需求方向。
- 用户问“这个问题是不是真问题”“是否值得做”“根因是什么”。

使用：

- 调用 `hanglv-diagnosis-agent`。

输出后：

- 只有证据强度中/高、且产品可解的问题，才进入 PRD。
- 如果是规则、客服、航司协同、供给问题，要明确不是单靠产品改版解决。

### 5. 方案卡、PRD、评审材料

触发条件：

- 用户要求 PRD、产品需求文档、方案评审、给研发/UI 评审材料。
- 用户给出诊断结论，希望转成方案。

使用：

- 调用 `hanglv-prd-agent`。

输出后：

- 如果涉及页面改版、新页面、交互状态、UI/研发评审，继续调用 `hanglv-design-delivery-agent`。
- 如果只是规则、策略、诊断或复盘，不强制生成 HTML 原型。

### 6. HTML 原型、Figma、UI 协作

触发条件：

- 用户要求原型图、HTML 原型、页面改版、交互 Demo、Figma、UI 评审材料。
- PRD 中存在“交互原型图/UE”且不是纯规则需求。

使用：

- 调用 `hanglv-design-delivery-agent`。
- 如果是存量页面改造，必须先用 Figma MCP 或截图读取现状。
- 如果是 0 到 1 新页面，必须遵循 `hanglv-c-end-ui-skill` 或 `hanglvzongheng-design-spec`。

输出后：

- PM 确认 HTML 后，才写入 Figma。
- UI 修改 Figma 后，再同步回 HTML。
- 生成 HTML/Figma/UI 审核材料后，如需通知 UI，调用 `hanglv-team-workflow-ops-agent`。

### 7. 前端实现、测试用例、截图与 PR 草案

触发条件：

- 用户已经有 HTML 原型、Figma/UI 稿或 `DesignDeliveryPackage`，并要求“转前端代码”“改成项目技术栈”“给前端代码”“推到 GitHub/GitLab”“创建 PR”。
- 用户提供前端仓库路径、页面路由、组件路径或技术栈信息。

使用：

- 调用 `hanglv-frontend-implementation-agent`。

输出后：

- 输出真实前端代码改动、mock 数据、页面验收矩阵、测试/截图结果和 PR 草案。
- 如已生成测试页面、截图或 PR，继续调用 `hanglv-frontend-qa-agent` 做设计验收。
- 如需通知前端或记录 PR 状态，调用 `hanglv-team-workflow-ops-agent`。
- 只有前端未打通服务端时，也可以基于 mock 数据生成 UI/交互测试用例和自动截图，但必须标注“不等于真实交易链路验收”。
- 不把 HTML 原型直接当生产代码，不自动合并 PR。

### 8. 前端验收、设计差异、PR 评论、发布门禁

触发条件：

- 用户给前端测试页面、GitHub/GitLab PR、Storybook、页面路由、前端截图。
- 用户要求“帮我验收 UI”“和 Figma 对比”“能不能输出修复建议/代码”。

使用：

- 调用 `hanglv-frontend-qa-agent`。

输出后：

- 输出设计差异报告、严重等级、修复建议和 PR 评论草案。
- 如果 P0/P1 需要人工确认是否阻断发布，调用 `hanglv-team-workflow-ops-agent` 生成飞书确认通知。
- 不承诺 AI 自动替代前端。自动 patch 必须作为草案，由前端 review。

## 固定交接对象

子 skill 之间优先用下面对象交接：

```text
ProblemRadarReport
  -> CompetitorReferenceReport
  -> ProblemDiagnosisReport
  -> SolutionCard
  -> PRDDraft
  -> DesignDeliveryPackage
  -> FrontendImplementationPackage
  -> FrontendQAReport
  -> TeamWorkflowOpsReport
  -> LaunchReview
```

每次输出都要标明当前对象类型和建议下一步。

## 人工确认门禁

以下节点必须人工确认：

1. 问题是否进入方案：PM 确认。
2. 方案卡是否进入 PRD：PM 确认。
3. HTML 原型是否写入 Figma：PM 确认。
4. Figma/UI 稿是否进入研发：UI/PM 确认。
5. AI 生成的前端实现是否创建 PR：前端/PM 确认。
6. AI 生成的前端 patch 是否合入：前端确认。
7. P0/P1 差异是否阻断发布：PM/UI/研发共同确认。

## 共享引用

子 skill 可按需读取主 skill 的共享资料：

- `references/problem-radar.md`
- `references/review-data-dictionary.md`
- `references/diagnosis-framework.md`
- `references/solution-card-template.md`
- `references/product-principles.md`
- `references/prd-standard.md`
- `references/prd-review-rubric.md`
- `references/flight-business-rules.md`
- `references/page-task-map.md`
- `references/design-delivery-workflow.md`
- `references/badcase-library.md`
- 竞品案例库：`/Users/weizheng/.codex/skills/hanglv-competitor-analysis-agent/references/competitor-case-library.md`
- 团队资产库建议路径：`/Users/weizheng/航旅纵横工作/ai-pm-artifacts/`

共享资料目录：

`/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/`

## 批改回流

当用户明确要求“记住/沉淀/更新 skill”时，才修改 skill 或 references。

回流规则：

- 模板问题：更新 `references/prd-standard.md`。
- 判断标准问题：更新 `references/prd-review-rubric.md`。
- 业务规则问题：更新 `references/flight-business-rules.md`。
- 页面任务问题：更新 `references/page-task-map.md`。
- 反例问题：更新 `references/badcase-library.md`。
- 竞品案例问题：更新 `hanglv-competitor-analysis-agent/references/competitor-case-library.md`。
- 工作流路由问题：更新本主 skill。
