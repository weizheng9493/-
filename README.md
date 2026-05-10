# 航旅 AI PM 工作流

> 航班预订智能助手产品研发团队协作仓库

这个仓库用于把航旅 AI PM 的工作流、Agent Skills、提示词、文档、案例和团队成员提交的智能体产物，按产品化方式持续管理。

## 目标

- 把工作流当成一个可迭代产品管理，而不是零散文档。
- 所有正式变更必须通过 Pull Request 提交、说明更新点，并经过审核后合并。
- 团队成员可以提交自己或智能体生成的 Markdown、代码、脚本、原型、分析材料等，但需要放入约定目录并补充来源、用途和风险说明。
- 每次正式发布通过版本号、`CHANGELOG.md` 和 GitHub Release 记录，确保团队知道当前可用版本和变更范围。

## 目录结构

```text
├── AGENTS.md                         # Codex / 智能体在本仓库工作的规则
├── CONTRIBUTING.md                   # 团队提交规范
├── CHANGELOG.md                      # 版本更新记录
├── docs/                             # 正式产品文档和流程说明
│   ├── PRD/                          # 产品需求文档
│   ├── design/                       # 设计交付物
│   ├── research/                     # 调研报告
│   ├── TEAM_COLLABORATION.md         # 团队协作规范
│   └── releases/                     # 发布流程文档
├── workflows/                        # 工作流定义和操作流程
├── prompts/                          # 可复用提示词模板
├── artifacts/                        # 团队成员和智能体生成的待沉淀产物
├── examples/                         # 示例提交和样例材料
├── releases/                         # 版本发布包
├── scripts/                          # 自动化脚本
├── .github/                          # PR、Issue、CODEOWNERS、CI/CD 配置
└── hanglv-ai-pm-agent-skills/         # 航旅 AI PM Agent Skills
```

## 工作流

1. **问题发现** → Issue 提出 → `hanglv-problem-radar-agent`
2. **竞品分析** → `hanglv-competitor-analysis-agent`
3. **问题诊断** → `hanglv-diagnosis-agent`
4. **PRD 撰写** → `hanglv-prd-agent`
5. **设计交付** → `hanglv-design-delivery-agent`
6. **前端实现** → PR → `hanglv-frontend-implementation-agent`
7. **设计 QA** → `hanglv-frontend-qa-agent`
8. **发布上线** → Release → 飞书通知

## 团队协作规则

1. 不直接向 `main` 分支提交。
2. 所有新增、修改、删除都通过 Pull Request。
3. PR 必须写清楚更新点、原因、影响范围、验证方式和风险。
4. 至少 1 名 reviewer 审核通过后才能合并。
5. 对工作流、规则、Agent Skill、发布文档的修改，需要更严格审核。
6. 智能体生成内容可以提交，但必须说明输入来源、生成工具、适用场景和待确认风险。

## 常见提交入口

| 你要提交什么 | 放在哪里 |
| --- | --- |
| 正式说明文档 | `docs/` |
| 工作流步骤 | `workflows/` |
| 可复用提示词 | `prompts/` |
| 智能体生成的 Markdown、代码、分析结果 | `artifacts/<提交人>/<日期-主题>/` |
| 示例 | `examples/` |
| Agent Skill | `hanglv-ai-pm-agent-skills/` |
| 发布包 | `releases/` |

## 标准流程

```text
创建分支
→ 新增或修改文件
→ 提交 commit
→ push 到 GitHub
→ 创建 Pull Request
→ reviewer 审核
→ 合并到 main
→ 必要时更新 CHANGELOG 并创建 Release
```

## 给团队成员的最小操作方式

如果你不熟悉命令行，可以在 GitHub 网页上操作：

1. 进入目标目录。
2. 点击 `Add file`。
3. 上传文件或新建文件。
4. 选择 `Create a new branch for this commit and start a pull request`。
5. 填写 PR 模板。
6. 等待审核。

## 发布流程

```bash
# 1. 创建发布分支
git checkout -b release/v1.0.0

# 2. 更新版本号和 CHANGELOG
# 3. 提交 PR → Review → Merge

# 4. 打标签
git tag -a v1.0.0 -m "feat: 航班搜索结果页优化"
git push origin v1.0.0

# 5. GitHub 自动生成 Release
```

## 团队成员

- PM: @weizheng
- 前端: @xxx
- 设计: @xxx

## 链接

- [Wiki 知识库](https://github.com/weizheng9493/-/wiki)
- [Projects 看板](https://github.com/weizheng9493/-/projects)
- [Discussions 讨论区](https://github.com/weizheng9493/-/discussions)
