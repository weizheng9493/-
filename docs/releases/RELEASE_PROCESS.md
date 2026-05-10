# 发布流程规范

## 1. 版本命名规则

```
v{major}.{minor}.{patch}
```

- **major**: 不兼容的重大变更
- **minor**: 向后兼容的新功能
- **patch**: 向后兼容的问题修复

示例：`v1.2.3`

---

## 2. 发布检查清单

### 发布前
- [ ] 所有关联 PR 已合并到 main
- [ ] CHANGELOG 已更新
- [ ] 本地测试通过
- [ ] Review 通过

### 发布中
- [ ] 创建 GitHub Release
- [ ] 填写版本号和发布说明
- [ ] 附件上传（releases/ 目录）
- [ ] 打标签 `git tag`

### 发布后
- [ ] 飞书通知已发送
- [ ] Wiki 文档已同步更新
- [ ] 团队成员已确认

---

## 3. Git 命令

```bash
# 1. 确保 main 最新
git checkout main
git pull origin main

# 2. 创建发布分支
git checkout -b release/v1.0.0

# 3. 更新版本信息
# - 修改 CHANGELOG.md
# - 修改 docs/VERSION

# 4. 提交 PR
git add .
git commit -m "chore: 准备发布 v1.0.0"
git push origin release/v1.0.0
# → 去 GitHub 发起 PR → Review → Merge

# 5. 合并后打标签
git checkout main
git pull origin main
git tag -a v1.0.0 -m "feat: 航班搜索结果页优化"
git push origin v1.0.0

# 6. GitHub Actions 自动触发 Release
```

---

## 4. 飞书通知模板

```
🚀 新版本发布

📦 版本: v1.0.0
📝 更新内容:
   - 航班搜索结果页优化
   - 修复价格显示 bug

🔗 Release: https://github.com/weizheng9493/-/releases/v1.0.0
```

---

## 5. Hotfix 流程

```bash
# 紧急修复走 hotfix 分支
git checkout main
git checkout -b hotfix/v1.0.1

# 修复完成后
git checkout -b release/v1.0.1
# → PR → Merge → 打标签
```
