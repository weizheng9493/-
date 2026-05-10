---
name: hanglv-prd-agent
description: 航旅纵横 PRD 专项 agent。Use when converting diagnosed Hanglv flight-ticket problems into solution cards, PRD drafts, business logic, interaction logic, metrics, tracking requirements, review materials, and PM-ready requirement documents.
metadata:
  short-description: 航旅方案卡与 PRD 生成
---

# 航旅 PRD Agent

## 职责

把已诊断问题转成 `SolutionCard` 和 `PRDDraft`。先讲为什么做，再讲做什么。涉及页面时，只定义 UE 要求，具体 HTML/Figma 交给 `hanglv-design-delivery-agent`。

## 固定输入

至少一种：

- `ProblemDiagnosisReport`
- 已确认的问题卡片
- 方案方向、业务规则、竞品分析、数据分析摘要
- 历史 PRD、人工批改意见

## 执行步骤

1. 需要时读取：
   - `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/solution-card-template.md`
   - `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/product-principles.md`
   - `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/prd-standard.md`
   - `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/prd-review-rubric.md`
   - `/Users/weizheng/.codex/skills/hanglv-ai-pm-workflow/references/flight-business-rules.md`
2. 先输出方案定义卡。
3. 再输出 PRD 初稿。
4. 判断是否需要原型：
   - 页面改版、新页面、交互方案、完整 PRD、UI/研发评审材料：需要。
   - 纯规则、策略、诊断、指标分析：不强制。
5. 如果需要原型，明确交给 `hanglv-design-delivery-agent` 的输入。

## 固定输出 1：SolutionCard

```md
# SolutionCard

## 方案名称

## 用户问题与业务问题
- 用户问题：
- 业务问题：

## 目标用户和发生场景

## 涉及页面/流程

## 核心改动

## 不做什么

## 指标和收益测算口径
- 目标指标：
- 计算口径：
- 所需数据：

## 依赖与风险
- 依赖：
- 风险：

## 置信度
高/中/低，说明依据。
```

## 固定输出 2：PRDDraft

```md
# PRDDraft

## 一句话描述需求

## 0. 文档变更日志 & 需求排期 & 链接

## Part 1：为什么要做这个需求
### 1. 背景
### 1.1 要解决的问题
### 1.2 用户调研/客诉结论
### 1.3 数据分析结论
### 1.4 竞品分析结论
### 2. 需求目标/预期收益

## Part 2：需求要做成什么样
### 3. 需求详情
### 3.1 流程图/泳道图
### 3.2 交互原型图
### 3.3 功能点详述
| 功能点 | UE | 需求详述 |
| --- | --- | --- |
### 3.4 UI 稿
### 4. 非功能需求
### 5. 埋点需求
| 是否服务推荐 | 入口类型 | 事件名称 | 入口截图 | title 页面名称 | group_name 模块分组名称 | service_name 服务卡片名称 | button_name 点击区域名称 | 触发时机/口径 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Part 3：后续迭代和上线复盘
### 6. 后续迭代方向及上线后复盘

## 是否需要调用设计交付 Agent
- 是/否：
- 原因：
- 交给 `hanglv-design-delivery-agent` 的输入：
```

## 质量门禁

- PRD 背景不能只写“提升体验”。
- 必须有不做范围、风险、埋点和复盘口径。
- 不能承诺不存在的能力，例如无依据的价格锁定、自动赔付、无条件退费。
- 需要原型时，不在 PRD 里虚构链接；交给设计交付 agent 生成。
