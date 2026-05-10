# 航旅 AI PM 工作流

> 航班预订智能助手产品研发团队协作仓库

## 目录结构

```
├── docs/                 # 产品文档
│   ├── PRD/             # 产品需求文档
│   ├── design/          # 设计交付物
│   └── research/        # 调研报告
├── releases/            # 版本发布包
├── scripts/             # 自动化脚本
└── .github/
    ├── workflows/       # CI/CD 流水线
    ├── ISSUE_TEMPLATE/  # Issue 模板
    └── PULL_REQUEST_TEMPLATE/  # PR 模板
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
