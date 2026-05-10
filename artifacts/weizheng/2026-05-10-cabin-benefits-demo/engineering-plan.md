# 研发实现说明：舱位权益展示 Demo

## 1. 实现目标

当前阶段不接真实接口，只用 `data/cabin-benefits.mock.json` 跑通展示数据结构、状态覆盖和 QA 校验。

## 2. 数据输入

假数据文件：

```text
artifacts/weizheng/2026-05-10-cabin-benefits-demo/data/cabin-benefits.mock.json
```

## 3. 建议组件拆分

```text
CabinSelectionPage
├── FlightSummary
├── CabinCard
│   ├── CabinHeader
│   ├── BenefitSummary
│   ├── BenefitList
│   └── SelectButton
└── SelectedCabinBar
```

## 4. 核心逻辑

- 按 `sortOrder` 排序舱位。
- 可选舱位展示选择按钮。
- 不可选舱位展示 `unavailableReason`。
- 默认只展示前 3 个权益。
- 展开后展示完整权益。
- `available = false` 的权益需要降级展示。
- 缺失字段使用兜底文案。

## 5. 校验脚本

运行：

```bash
node artifacts/weizheng/2026-05-10-cabin-benefits-demo/scripts/validate-cabin-benefits.mjs
```

校验内容：

- 至少 3 个舱位。
- 至少 2 个可选舱位。
- 至少 1 个不可选舱位。
- 可选舱位至少 3 个权益。
- 每个权益必须有 `benefitId`、`name`、`summary`。

## 6. 后续接真实接口时需要确认

- 舱位权益字段是否由航司、供应商还是自有配置提供。
- 接口是否返回权益排序。
- 是否需要前端做权益字段兜底映射。
- 不同航司权益口径不一致时如何展示。

## 7. 风险

- 假数据结构可能和真实接口不一致。
- UI 文字规则需要设计确认。
- 权益真实规则可能影响订单和售后链路。
