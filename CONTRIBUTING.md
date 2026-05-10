# 贡献指南

本仓库采用 Pull Request 协作。任何正式内容更新都需要经过审核后合并。

## 提交流程

1. 从 `main` 拉取最新代码。
2. 创建新分支。
3. 新增或修改文件。
4. 提交 commit。
5. push 分支到 GitHub。
6. 创建 Pull Request。
7. 按 PR 模板说明更新点、影响范围、验证方式和风险。
8. 等待 reviewer 审核。
9. 审核通过后合并。

## 分支命名建议

```text
docs/<主题>
workflow/<主题>
prompt/<主题>
artifact/<提交人>-<主题>
skill/<技能名>-<主题>
chore/<主题>
```

示例：

```text
docs/release-process
workflow/codex-issue-pr
artifact/weizheng-design-review-demo
```

## Commit 信息建议

```text
docs: update release process
workflow: add codex issue to pr flow
prompt: add PRD generation prompt
artifact: add design review demo
skill: update diagnosis agent rubric
chore: bootstrap repository governance
```

## 智能体生成内容提交规范

智能体生成内容必须放在：

```text
artifacts/<提交人或团队>/<YYYY-MM-DD-主题>/
```

每个产物目录必须包含 `README.md`，并说明：

- 提交人。
- 生成工具或智能体。
- 输入来源。
- 产物内容。
- 使用场景。
- 人工校验状态。
- 主要风险。
- 是否建议沉淀为正式文档、Prompt 或工作流。

## 审核标准

Reviewer 应重点检查：

- 是否符合仓库目录规范。
- 是否说明更新原因和影响范围。
- 是否有明确验证方式。
- 是否包含隐私、密钥或未经脱敏的信息。
- 是否把推测内容写成事实。
- 是否会影响已有工作流或 Agent Skill。

## 发布规则

合并到 `main` 代表内容进入主仓库，但不等于正式发布。

正式发布需要：

1. 更新 `CHANGELOG.md`。
2. 确认本次发布范围。
3. 在 GitHub 创建 Release。
4. 在团队沟通渠道同步版本号和主要更新。
