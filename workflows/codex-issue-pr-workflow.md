# Codex + GitHub Issue + PR 工作流

## 目标

把飞书讨论、个人想法或智能体输出，转化为可追踪、可审核、可发布的 GitHub 协作流程。

## 标准链路

```text
飞书讨论或个人想法
→ GitHub Issue
→ Codex 或其他智能体执行
→ 生成文件或代码
→ Pull Request
→ 人工审核
→ 合并 main
→ 必要时发布 Release
```

## Issue 应该写什么

一个好的 Issue 至少包含：

- 背景。
- 要解决的问题。
- 目标。
- 输入材料。
- 期望输出。
- 验收标准。
- 风险或边界。

## 让 Codex 执行

如果 GitHub 已经接入 Codex，可以在 Issue 或 PR 中使用：

```text
@codex implement this issue
```

或者：

```text
@codex review this PR and identify risks
```

如果没有接入，也可以在本地 Codex 中打开仓库，引用 Issue 内容，让 Codex 在新分支中修改文件。

## PR 应该写什么

PR 必须说明：

- 更新了什么。
- 为什么更新。
- 影响哪些目录或使用方式。
- 如何验证。
- 有哪些风险和待确认点。

## 合并后

合并后根据变更类型判断是否需要：

- 更新 `CHANGELOG.md`。
- 创建 Release。
- 在飞书同步说明。
- 把 `artifacts/` 中的内容整理进入正式 `docs/`、`prompts/` 或 `workflows/`。
