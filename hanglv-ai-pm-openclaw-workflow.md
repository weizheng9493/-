# 航旅纵横 AI PM 工作流给 OpenClaw 使用说明

## 目标

这套工作流用于帮助航旅纵横机票业务产品经理，用 AI 提效从问题发现到方案、PRD、UI、前端、验收和团队协作的完整产研流程。

核心目标不是让 AI 替代 PM/UI/前端，而是：

- 自动整理客诉和评价。
- 判断问题是否真实、是否严重、是否值得做。
- 生成方案卡和 PRD。
- 生成 HTML 原型、截图和 Figma/UI 交付材料。
- 将设计交付物转成前端实现建议、测试用例和 PR 草案。
- 对比 UI 稿和前端实现，输出差异报告。
- 通过飞书群通知 UI、前端、PM 等负责人做人工确认。
- 沉淀需求资产、竞品案例和 badcase。

## 主 Skill

主 skill：

```text
hanglv-ai-pm-workflow
```

主 skill 只做三件事：

1. 判断当前任务属于哪个产研环节。
2. 调用对应专项子 skill。
3. 串联子 skill 的输入输出，保证证据、状态、产物和人工确认闭环。

## 子 Agent 列表

| 子 Agent | 负责环节 | 固定输出 |
| --- | --- | --- |
| `hanglv-problem-radar-agent` | 原始反馈到问题雷达 | `ProblemRadarReport` |
| `hanglv-competitor-analysis-agent` | 竞品录屏/截图到案例库和参考报告 | `CompetitorCaseLibrary`、`CompetitorReferenceReport` |
| `hanglv-diagnosis-agent` | 问题真实性、严重度、根因与优先级诊断 | `ProblemDiagnosisReport` |
| `hanglv-prd-agent` | 方案卡与 PRD 初稿 | `SolutionCard`、`PRDDraft` |
| `hanglv-design-delivery-agent` | HTML 原型、截图、Figma/UI 交付 | `DesignDeliveryPackage` |
| `hanglv-frontend-implementation-agent` | 设计交付物到前端代码和 PR 草案 | `FrontendImplementationPackage` |
| `hanglv-frontend-qa-agent` | 前端验收、设计差异、PR 评论、发布门禁 | `FrontendQAReport` |
| `hanglv-team-workflow-ops-agent` | 飞书通知、状态流转、资产归档、文件触发 | `TeamWorkflowOpsReport` |

## 工作流主链路

```text
飞书客诉 / App 评价 / 客服工单 / 用户原声
-> ProblemRadarReport
-> ProblemDiagnosisReport
-> SolutionCard
-> PRDDraft
-> DesignDeliveryPackage
-> FrontendImplementationPackage
-> FrontendQAReport
-> TeamWorkflowOpsReport
-> LaunchReview
```

## 问题诊断规则

问题整理不是核心，关键是判断问题是否严重、是否值得产品介入。

诊断时必须判断：

- 是否是真问题。
- 是否影响下单、支付、出票、退改、报销等核心链路。
- 是否是 Bug 或错误信息。
- 影响人数和发生频次。
- 单个用户损失程度。
- 是否影响转化、信任、客服成本或合规风险。
- 产品是否可解，还是需要运营、客服、航司或研发协同。

优先级口径：

- `P0`：阻断搜索、下单、支付、出票、退改、报销；Bug 阻断核心链路；价格/航班/退改/出票状态展示错误；合规、资损、舆情风险。
- `P1`：明显影响下单转化、用户信任或客服成本；影响人数较多；用户可绕过但理解成本高。
- `P2`：体验影响明确，但不明显阻断核心任务；适合排期优化。
- `P3`：单点反馈、边缘场景、证据弱或产品不可控，进入观察池。

## 飞书客诉自动触发建议

推荐先用轻量方案：

```text
飞书智能体每日/每周总结客诉
-> 导出 PDF / Word / Markdown / CSV
-> 放到固定文件夹
-> OpenClaw/Codex 定时扫描
-> 发现新文件
-> 调用问题雷达和诊断
-> 如有 P0/P1 候选问题，飞书群通知 PM
```

建议本机文件夹：

```text
/Users/weizheng/Downloads/hanglv-complaints-inbox/
```

处理规则：

- 新文件放到 inbox 根目录。
- 处理成功后移动到 `processed/`。
- 处理失败后移动到 `failed/`。
- 输出报告进入需求资产库。
- 客诉里如有手机号、订单号、身份证、乘机人姓名，输出前必须脱敏。

## 需求资产库

需求资产库是所有 AI 产物和评审链接的统一目录，避免 PRD、Figma、HTML、PR、验收报告散落在聊天记录和飞书里。

建议路径：

```text
/Users/weizheng/航旅纵横工作/ai-pm-artifacts/
```

推荐结构：

```text
ai-pm-artifacts/
  index.md
  problems/
  diagnosis/
  prd/
  design/
  frontend/
  qa/
  launch-review/
  competitor/
```

每个需求至少记录：

```text
需求 ID
需求标题
当前状态
优先级
Owner
当前确认人
ProblemRadarReport
ProblemDiagnosisReport
PRD
HTML 原型
Figma
前端 PR
FrontendQAReport
LaunchReview
下一步
```

## 团队状态流转

推荐状态：

```text
问题池
-> 待诊断
-> 待方案
-> 待 PRD 评审
-> 待 UI 审核
-> UI 审核中
-> 待前端实现
-> 前端开发中
-> 待设计验收
-> 待发布
-> 已上线
-> 待复盘
-> 已沉淀
```

## 飞书通知模板

### UI 审核通知

```text
【AI PM 工作流｜待 UI 审核】
需求：<需求标题>
优先级：<P0/P1/P2/P3>
PRD：<链接>
HTML 原型：<链接>
默认态截图：<链接>
需要确认：视觉方案、组件使用、关键状态、是否可进入前端
请 @<UI负责人> 在 <截止时间> 前确认。
```

### 前端实现通知

```text
【AI PM 工作流｜待前端实现】
需求：<需求标题>
Figma：<链接>
PRD：<链接>
页面验收矩阵：<链接>
请 @<前端负责人> 评估实现并创建 PR。
注意：HTML 原型是交互参考，不是生产代码。
```

### 前端验收通知

```text
【AI PM 工作流｜待设计验收】
需求：<需求标题>
PR：<链接>
测试环境：<链接>
AI 验收报告：<链接>
P0/P1：<有/无>
请 @<PM> @<UI负责人> 确认是否允许合并/发布。
```

### 工作流变更通知

```text
【AI PM 工作流更新】
变更点：<新增/调整规则>
影响范围：<问题诊断/PRD/UI/前端/验收/复盘>
生效时间：<时间>
需要团队注意：<一句话说明>
负责人：<PM>
```

## OpenClaw 使用方式

如果飞书妙搭里的 OpenClaw 连接的是这台机器的 OpenClaw，本机 skill 加载目录是：

```text
/Users/weizheng/.openclaw-autoclaw/workspace/.opencode/skills/
```

应把完整 skill 文件夹复制到该目录，而不是只复制本说明文档。

完整 skill 包在：

```text
/Users/weizheng/Downloads/hanglv-ai-pm-agent-skills.zip
```

解压后需要包含：

```text
hanglv-ai-pm-workflow
hanglv-problem-radar-agent
hanglv-competitor-analysis-agent
hanglv-diagnosis-agent
hanglv-prd-agent
hanglv-design-delivery-agent
hanglv-frontend-implementation-agent
hanglv-frontend-qa-agent
hanglv-team-workflow-ops-agent
```

## 给飞书 OpenClaw 的测试指令

复制 skill 后，可以在飞书里对 OpenClaw 说：

```text
使用 hanglv-ai-pm-workflow，说明你现在支持哪些航旅 AI PM 工作流能力。
```

如果它能说出以下能力，说明加载基本成功：

- 问题雷达
- 竞品分析
- 问题诊断
- PRD 生成
- HTML/Figma/UI 交付
- 前端实现
- 前端验收
- 飞书通知和团队状态流转

## 重要边界

- AI 生成内容不能替代 PM、UI、前端、测试的人工确认。
- HTML 原型不能直接作为生产代码。
- mock 数据验收不等于真实服务端联调验收。
- 没有真实飞书 webhook、chat_id 或 OpenClaw 消息权限时，只能生成飞书消息草案，不能声称已发送。
- 涉及价格、出票、退改、报销、支付等核心链路，必须保留人工 review。
