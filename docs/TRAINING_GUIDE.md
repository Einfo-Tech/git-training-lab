# Git 实战训练手册

## 练习 1：克隆并认识仓库

```bash
git clone git@github.com:Techeek/git-training-lab.git
cd git-training-lab
git branch -a
git remote -v
git log --oneline --graph --decorate --all -12
```

目标：分清本地分支、远程跟踪分支和远程仓库。

## 练习 2：从 dev 创建开发分支

```bash
git switch dev
git pull --ff-only
git switch -c feature/<姓名或事项编号>-welcome
```

修改 `participants.md`，增加一行自己的姓名或代号，然后提交并推送：

```bash
git add participants.md
git commit -m "docs(participants): add training participant"
git push -u origin HEAD
```

在 GitHub 创建 Pull Request：`feature/* → dev`。

## 练习 3：代码修改与自动测试

修改 `src/discount.py`，为折扣比例增加范围校验；运行：

```bash
python3 -m unittest discover -s tests -v
```

提交 PR 时填写变更目标、测试结果、风险和回退方式。

## 练习 4：版本提升

由培训讲师依次演示：

1. `feature/* → dev`：开发集成。
2. `dev → test`：测试版本提升。
3. `test → main`：生产版本提升。

每次提升都使用 PR，并核对源分支、目标分支和检查结果。

## 练习 5：解决冲突

两位学员分别使用 `exercise/conflict-a` 和 `exercise/conflict-b`，修改 `docs/team-rules.md` 的同一行，然后尝试依次合入 `dev`。

解决冲突时先确认双方意图，再删除冲突标记并运行测试。

## 练习 6：撤销错误提交

在个人练习分支创建一个可识别的错误提交，然后使用：

```bash
git log --oneline -5
git revert <错误提交>
git push
```

观察历史中原提交和撤销提交都被保留。
