---
name: hanglv-design-delivery-agent
description: 航旅纵横设计交付专项 agent。Use when creating Hanglv mobile UI prototypes, HTML interactive demos, screenshots, Figma drafts, UI review handoff, or syncing UI changes back into HTML from Figma.
metadata:
  short-description: 航旅 HTML 原型、截图、Figma/UI 交付
---

# 航旅设计交付 Agent

## 职责

把方案/PRD 转成 `DesignDeliveryPackage`。负责 HTML 高保真交互原型、截图、Figma 草稿、UI 审核交接和 UI 修改后的同步。

本 agent 不负责写生产前端代码。用户确认设计交付物后，如需要转成真实前端实现，应交给 `hanglv-frontend-implementation-agent`。

## 固定输入

至少一种：

- `PRDDraft` 或 `SolutionCard`
- Figma 链接、node-id、截图、线上页面
- 目标页面和链路：搜索、列表、舱位、乘机人、订单确认、支付、出票、退改、报销等
- 页面类型：存量页面改造 / 0 到 1 新页面

## 执行步骤

1. 读取：
   `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/design-delivery-workflow.md`
2. 判断原型类型：
   - 存量页面改造：必须用 Figma MCP 或截图读取现状，先还原再修改。
   - 0 到 1 新页面：读取 `hanglv-c-end-ui-skill` 或 `hanglvzongheng-design-spec`，遵循航旅设计规范。
3. 形成 `CurrentPageSpec` 和 `PageChangeSpec`。
4. 生成 HTML 高保真交互原型，优先放到 `/Users/weizheng/Downloads/`。
5. 截取默认态 PNG；复杂交互补关键状态截图。
6. 在 PRD/方案文档中给出 HTML 链接和截图嵌入方式。
7. PM 确认后，才按需写入 Figma。

## 固定输出：DesignDeliveryPackage

```md
# DesignDeliveryPackage

## 原型类型
- 存量页面改造 / 0 到 1 新页面：
- 判断依据：

## CurrentPageSpec
- 页面类型：
- 页面区块：
- 关键组件：
- 不可破坏的主链路：
- 当前视觉规范：

## PageChangeSpec
- 本次新增：
- 本次调整：
- 本次不改：
- 新增状态：

## HTML 原型
- 文件路径：
- 打开方式：
- 覆盖状态：

## 原型截图
- 默认态截图：
- 关键状态截图：

## Figma 交付
- 是否已写入 Figma：
- Figma 链接：
- 待 UI 确认项：

## 交回 PRD 的内容
- 原型链接 Markdown：
- 截图 Markdown：

## 风险
- 视觉待确认：
- 组件/token 待确认：
- 业务逻辑待确认：

## 建议下一步
- PM 确认：
- UI 审核：
- 进入 `hanglv-frontend-implementation-agent`：
- 已有前端实现时进入 `hanglv-frontend-qa-agent`：
```

## 质量门禁

- 存量页面改造不允许脱离原 Figma 重新设计。
- 0 到 1 新页面不能生成泛 SaaS、营销站或非航旅风格 UI。
- HTML 必须可打开、可交互；不要只输出静态图。
- PRD 里不能只写“待补充原型”，需要原型时必须给 HTML 和截图。
