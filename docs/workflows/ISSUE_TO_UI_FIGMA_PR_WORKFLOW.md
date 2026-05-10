# Issue 到 UI/Figma/PR 的快速闭环工作流

## 1. 适用场景

当团队希望快速验证一个产品需求、UI 方案或交互想法时，可以先用假数据跑通完整流程，而不是等待真实接口、正式 Figma 设计稿和完整研发排期。

适合场景：

- 新需求的快速 Demo。
- 产品、UI、研发三方对齐方案。
- 验证 GitHub Issue 到 PR 的协作机制。
- 验证 HTML 原型能否进入 Figma 评审。
- 验证智能体生成产物能否沉淀到仓库。

不适合场景：

- 直接作为上线代码。
- 直接替代正式 Figma 设计稿。
- 直接作为真实业务规则。

## 2. 标准流程

```text
GitHub Issue
→ 产品 PRD 草稿
→ UI 交付说明
→ HTML 交互原型
→ Figma MCP Capture
→ Figma 链接回写仓库
→ 研发实现说明
→ QA 验收报告
→ Pull Request
→ 产品 / UI / 研发 Review
→ 合并 main
→ 必要时 Release
```

## 3. 角色分工

| 角色 | 负责内容 | 主要产物 |
| --- | --- | --- |
| 产品 | 明确问题、目标、范围、验收标准 | `prd.md` |
| UI | 定义页面结构、状态、视觉方向 | `ui-handoff.md`、Figma 链接 |
| 研发 | 判断实现方式、数据结构、风险 | `engineering-plan.md`、mock data |
| QA | 检查状态覆盖和验收结果 | `qa-report.md` |
| AI Agent | 生成草稿、原型、校验脚本、PR 说明 | artifacts 产物包 |

## 4. 推荐目录结构

每个需求 Demo 都放在独立 artifacts 目录：

```text
artifacts/<提交人>/<YYYY-MM-DD-需求主题>/
├── README.md
├── prd.md
├── ui-handoff.md
├── engineering-plan.md
├── qa-report.md
├── data/
│   └── *.mock.json
├── scripts/
│   └── validate-*.mjs
└── prototype/
    └── index.html
```

## 5. 产物要求

### 5.1 PRD 草稿

至少包含：

- 背景。
- 目标。
- 非目标。
- 用户故事。
- 页面范围。
- 字段说明。
- 交互状态。
- 埋点建议。
- 验收标准。
- 风险和待确认。

### 5.2 UI 交付说明

至少包含：

- Figma 链接。
- 页面结构。
- 信息层级。
- 默认态、展开态、选中态、不可选态、异常态。
- 设计验收清单。
- 待确认问题。

### 5.3 HTML 原型

要求：

- 可以本地直接打开或通过静态服务打开。
- 使用假数据模拟核心状态。
- 至少覆盖主要交互。
- 不接真实接口。
- 不包含敏感信息。

### 5.4 Figma MCP Capture

流程：

1. 本地启动 HTML 原型服务。
2. 使用 Figma MCP `generate_figma_design` 创建新 Figma 文件或写入已有文件。
3. 打开带 capture 参数的本地页面。
4. 等待 capture 完成。
5. 将 Figma 链接写回 `README.md`、`ui-handoff.md`、`qa-report.md`。

注意：

- Capture 结果通常是 raw frames。
- 它适合快速视觉评审，不等同于组件化设计系统稿。
- 如果要正式交付设计，应由 UI 在 Figma 中进一步组件化、规范化。

### 5.5 QA 报告

至少包含：

- 验收范围。
- 验收项。
- 校验命令。
- 当前结论。
- 阻塞项。
- 风险等级。

## 6. Pull Request 要求

PR 需要说明：

- 本次更新点。
- 关联 Issue。
- 为什么需要这次更新。
- 影响范围。
- 验证方式。
- 风险与待确认。

示例验证命令：

```bash
node artifacts/<提交人>/<YYYY-MM-DD-需求主题>/scripts/validate-*.mjs
```

## 7. 飞书通知

GitHub 事件会通过 GitHub Actions 推送到飞书群机器人。

当前监听事件：

- Issue 创建、编辑、关闭、重新打开。
- PR 创建、重新打开、ready for review、更新、关闭。
- PR review 提交。
- Release 发布。

需要在 GitHub 仓库中配置 Actions Secrets：

| Secret | 用途 |
| --- | --- |
| `FEISHU_WEBHOOK` | 飞书自定义机器人 Webhook 地址 |
| `FEISHU_SECRET` | 飞书机器人签名密钥，可选但建议配置 |

通知内容会包含：

- 仓库。
- Issue / PR / Release 标题。
- 状态。
- 操作人。
- GitHub 链接。
- 产品、UI、前端、QA 的建议处理项。

## 8. 当前示例

示例需求：

- Issue #2：舱位选择页权益展示与选择规则优化。

示例 PR：

- PR #3：新增舱位选择页权益展示 Demo。

示例 Figma：

- https://www.figma.com/design/loxVuPKMBrzo2EW0XLPChk

## 9. 优势

- 产品、UI、研发不用等待完整真实系统，即可先对齐方案。
- 所有产物进入 GitHub，可追踪、可审核、可复用。
- HTML 原型能快速变成 Figma 可评审材料。
- QA 可以提前检查状态覆盖。
- PR 形成正式审核入口。

## 10. 风险

- 假数据可能和真实接口不一致。
- HTML 原型可能偏离正式设计系统。
- Figma capture 是 raw frames，需要 UI 后续规范化。
- 如果 Issue 写得不清楚，AI 生成产物会跑偏。
- 如果没有人工审核，AI 产物可能被误当成正式规范。

## 11. 最小可执行版本

如果只想快速跑通，至少需要：

1. 一个 GitHub Issue。
2. 一个 artifacts 目录。
3. 一个 `prd.md`。
4. 一个 `ui-handoff.md`。
5. 一个 `prototype/index.html`。
6. 一个 Figma capture 链接。
7. 一个 `qa-report.md`。
8. 一个 Pull Request。
