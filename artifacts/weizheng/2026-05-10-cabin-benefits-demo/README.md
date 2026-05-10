# 舱位选择页权益展示 Demo

## 基本信息

- 提交人：weizheng
- 日期：2026-05-10
- 关联 Issue：https://github.com/weizheng9493/-/issues/2
- 使用的智能体或工具：Codex
- 输入来源：Issue #2 舱位选择页权益展示与选择规则优化
- 产物类型：端到端工作流 Demo

## 内容说明

这个目录用于快速跑通“产品 → UI → 研发 → QA → PR 审核”的完整工作流。当前不接真实接口，不修改线上代码，只使用假数据模拟舱位选择页的权益展示需求。

## 目标

- 验证 Issue 能否转化为 PRD 草稿。
- 验证 PRD 能否转化为 UI 交付说明。
- 验证 UI 和 PRD 能否转化为研发实现说明和假数据。
- 验证 QA 能否基于产物进行验收。
- 验证所有内容能否通过 PR 进入仓库。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `prd.md` | 产品需求草稿 |
| `ui-handoff.md` | UI 交付说明 |
| `engineering-plan.md` | 研发实现说明 |
| `qa-report.md` | QA 验收报告 |
| `data/cabin-benefits.mock.json` | 假数据 |
| `scripts/validate-cabin-benefits.mjs` | 假数据校验脚本 |
| `prototype/index.html` | 可交互 HTML 原型 |

## Figma 链接

- HTML 原型 Capture：https://www.figma.com/design/loxVuPKMBrzo2EW0XLPChk

说明：这个 Figma 文件由 HTML 原型捕获生成，用于快速跑通 UI 协作和视觉评审流程。当前是 raw frames，不是组件化设计系统稿。

## 原型查看方式

直接用浏览器打开：

```text
prototype/index.html
```

原型支持：

- 点击舱位卡片展开/收起权益。
- 切换选中舱位。
- 展示不可选舱位和不可选原因。
- 底部确认条承接已选舱位。

## 人工校验状态

- [ ] 未校验
- [x] 已初步校验
- [ ] 已充分校验

## 当前结论

这个 Demo 只用于跑通流程，不代表最终产品方案。真实上线前仍需确认权益字段来源、航司差异、订单链路承接和埋点方案。

## 风险和待确认

- 当前权益字段为假数据，未连接真实接口。
- 当前 UI 交付说明为文字说明，不包含 Figma 设计稿。
- 当前研发计划不修改真实代码，只作为后续实现输入。
- 当前 QA 报告基于静态文档和假数据，不代表真实页面验收。

## 后续建议

- [x] 保留在 artifacts
- [ ] 整理进 docs
- [ ] 整理进 prompts
- [ ] 整理进 workflows
- [ ] 不建议继续使用
