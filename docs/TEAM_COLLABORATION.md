# 团队协作规范

## 角色分工

| 角色 | GitHub ID | 职责 |
|------|-----------|------|
| PM | @weizheng | 产品规划、PRD、优先级 |
| 前端 | @xxx | 页面实现、PR Review |
| 设计 | @xxx | Figma 设计稿、设计 QA |

---

## 分支命名规范

```
feature/xxx          # 新功能
bugfix/xxx           # Bug 修复
hotfix/xxx           # 紧急修复
release/v1.0.0       # 发布分支
docs/xxx             # 文档更新
```

---

## Commit 规范

```
feat:     新功能
fix:      Bug 修复
docs:     文档变更
style:    代码格式（不影响功能）
refactor: 重构
test:     测试相关
chore:    构建/工具变更
```

示例：
```bash
git commit -m "feat: 新增航班筛选功能"
git commit -m "fix: 修复价格显示为负数的问题"
git commit -m "docs: 更新发布流程文档"
```

---

## Code Review 规范

1. **PR 大小**: 尽量 < 400 行改动，大 PR 拆分成多个
2. **Review 人数**: 至少 1 人 Approve 才能合并
3. **Review 重点**:
   - 功能逻辑是否正确
   - 是否有安全隐患
   - 是否符合设计稿
   - 是否有测试覆盖

---

## 问题优先级

| 优先级 | 定义 | 响应时间 |
|--------|------|----------|
| P0 | 线上故障、数据问题 | 立即处理 |
| P1 | 重要功能阻塞 | 24 小时内 |
| P2 | 一般性问题 | 3 天内 |
| P3 | 优化建议 | 1 周内 |

---

## 沟通渠道

- **日常讨论**: GitHub Discussions
- **任务管理**: GitHub Projects（看板）
- **文档**: Wiki / docs/
- **紧急联系**: 飞书群
