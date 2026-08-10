# 项目代码管理规范

> 本文件是本项目的默认代码管理约定。所有开发人员、实施人员、运维人员及 AI 助手在修改代码前都应先阅读本文件。
>
> 如项目存在特殊流程，请在“项目特例”章节明确记录；未记录的情况按本文执行。

## 1. 分支模型

项目通常保留三条长期主分支：

| 分支 | 用途 | 基本要求 |
| --- | --- | --- |
| `dev` | 日常开发集成 | 汇总已完成自测的开发内容 |
| `test` | 测试、联调和业务验收 | 只接收准备测试或验收的版本 |
| `main` / `master` | 生产基线 | 只保存已经确认可以发布的版本 |

所有代码修改在开始前，必须先创建独立的开发分支，不直接在长期主分支上开发。

常用开发分支：

- `feature/<事项编号>-<简短说明>`：新功能、需求和一般改进。
- `fix/<问题编号>-<简短说明>`：缺陷修复。
- `hotfix/<问题编号>-<简短说明>`：经负责人批准的紧急生产修复。
- `docs/<简短说明>`：仅文档修改。
- `refactor/<简短说明>`：不改变业务行为的代码重构。

示例：

```text
feature/ABC-123-customer-import
fix/BUG-204-tax-rounding
hotfix/INC-018-login-error
```

## 2. 标准开发流程

推荐流程如下：

```text
从最新目标分支创建 feature/fix 分支
    ↓
开发、小步提交、自测
    ↓
通过 PR 或本地命令合并到 dev/test/main/master
    ↓
测试、验收、发布并保留回退点
```

默认情况下，开发分支先合并到 `dev`，再按以下顺序逐级提升：

```text
feature/fix → dev → test → main/master
```

如果项目流程要求开发分支直接合并到 `test` 或 `main/master`，必须满足以下条件：

1. 已明确目标分支和原因。
2. 已完成相应测试与代码审查。
3. 已获得项目负责人或发布负责人的同意。
4. 已准备可执行的回退方案。

## 3. 创建开发分支

开始开发前先更新目标分支，再创建新分支：

```bash
git switch dev
git pull --ff-only origin dev
git switch -c feature/<事项编号>-<简短说明>
```

修复问题时，将 `feature/` 替换为 `fix/`。如果实际目标是 `test` 或 `main/master`，应从对应的最新目标分支创建开发分支。

创建分支后先确认：

```bash
git status
git branch --show-current
```

## 4. 提交规范

一次提交只处理一个清晰目的。提交前必须检查实际修改：

```bash
git status
git diff
git diff --staged
```

推荐使用以下提交格式：

```text
<类型>(<范围>): <简短说明>
```

常用类型：

- `feat`：新增功能。
- `fix`：修复缺陷。
- `docs`：修改文档。
- `refactor`：代码重构。
- `test`：增加或调整测试。
- `chore`：构建、配置或日常维护。
- `perf`：性能优化。

示例：

```text
feat(customer): add customer import validation
fix(invoice): correct tax rounding
docs(readme): document local merge workflow
```

禁止使用无法说明目的的提交信息，例如 `update`、`fix bug`、`test` 或 `修改一下`。

## 5. 推送与 Pull Request

首次推送开发分支：

```bash
git push -u origin HEAD
```

建议优先通过 PR 合并。PR 至少应说明：

- 修改目的和对应的 Issue/需求。
- 主要改动范围。
- 已执行的测试及结果。
- 风险、影响范围和兼容性。
- 发布步骤与回退方式。
- 截图、日志或其他必要证据。

创建 PR 前再次确认目标分支。除项目另有约定外，普通开发 PR 的目标分支应为 `dev`。

禁止在 PR 中提交或粘贴真实令牌、密码、私钥、客户数据及生产敏感信息。

## 6. 使用本地命令处理分支合并

### 6.1 将目标分支合入开发分支

此方法用于更新开发分支，或在本地解决 PR 冲突。以下以 `dev` 和 `feature/ABC-123` 为例：

```bash
# 1. 更新目标分支
git switch dev
git pull --ff-only origin dev

# 2. 切换到开发分支
git switch feature/ABC-123

# 3. 将目标分支合入开发分支
git merge dev

# 4. 如有冲突，修改冲突文件并完成验证
git status
git diff
git add <已解决的文件>
git commit

# 5. 推送更新后的开发分支
git push -u origin HEAD
```

合并方向是：

```text
dev → feature/fix
```

解决冲突时，不要盲目选择“保留全部”。必须理解双方修改目的，运行相关测试后再提交。

### 6.2 将开发分支本地合入目标分支

仅在项目允许本地合并，且操作者具有对应权限时使用：

```bash
# 1. 更新目标分支
git switch dev
git pull --ff-only origin dev

# 2. 合并开发分支，并保留明确的合并记录
git merge --no-ff feature/ABC-123

# 3. 运行项目要求的测试并检查结果
git status

# 4. 推送目标分支
git push origin dev
```

合并方向是：

```text
feature/fix → dev/test/main/master
```

将开发分支本地合入 `test` 或 `main/master` 前，必须完成项目要求的测试、审批和回退准备。受保护分支可能禁止直接推送，此时必须使用 PR。

## 7. 冲突处理原则

出现冲突时按以下顺序处理：

1. 使用 `git status` 确认冲突文件。
2. 理解当前分支和目标分支各自修改的目的。
3. 手工确认最终应保留的业务逻辑。
4. 删除冲突标记：`<<<<<<<`、`=======`、`>>>>>>>`。
5. 运行格式检查、自动化测试和必要的人工验证。
6. 使用 `git add` 和 `git commit` 记录解决结果。
7. 推送分支并在 PR 中说明冲突处理方式。

无法确定正确业务结果时，应停止合并并联系原作者或项目负责人，不得由 AI 或操作者猜测。

## 8. 测试、验收与发布

不同阶段的验证不可相互替代：

- 开发自测：证明当前修改在开发环境中基本可用。
- 自动化测试：证明已覆盖的行为未发生预期外变化。
- `test` 验证/UAT：证明测试场景和业务验收要求得到满足。
- 生产验收：证明实际生产环境中的目标流程正常。

合并到 `main/master` 前至少确认：

- 需求和验收标准已明确。
- 代码审查已完成。
- 必要测试已通过并有结果记录。
- 配置、数据库变更和依赖变更已说明。
- 发布负责人和发布时间已确认。
- 备份、tag、镜像或其他回退点已经准备。

建议发布时创建版本标签：

```bash
git tag -a v<版本号> -m "release v<版本号>"
git push origin v<版本号>
```

## 9. 安全与仓库卫生

以下内容禁止提交到代码仓库：

- API Token、访问令牌、密码和 Cookie。
- SSH 私钥、证书私钥和未加密密钥文件。
- `.env`、生产配置和数据库备份中的敏感内容。
- 客户个人信息、生产业务数据和未脱敏日志。
- 构建缓存、运行时文件、大型临时文件和本机配置。

项目必须维护适合自身技术栈的 `.gitignore`。示例配置文件应使用脱敏占位符，例如 `.env.example`。

如果敏感信息已经提交：

1. 立即停止继续传播。
2. 撤销或轮换相关凭据。
3. 联系仓库管理员评估历史清理方式。
4. 不要只删除当前文件后就认为问题已经解决。

## 10. 禁止事项

- 禁止直接在长期主分支上开始开发。
- 禁止未经确认直接合并到 `main/master`。
- 禁止跳过必要测试、审批或业务验收。
- 禁止对共享分支执行强制推送。
- 禁止提交无关文件、运行时产物或真实敏感数据。
- 禁止在工作区存在未知修改时直接覆盖、清理或重置。

## 11. 快速命令参考

```bash
# 查看状态和当前分支
git status
git branch --show-current

# 从最新 dev 创建开发分支
git switch dev
git pull --ff-only origin dev
git switch -c feature/<事项编号>-<简短说明>

# 检查、暂存和提交
git diff
git add <文件>
git diff --staged
git commit -m "feat(scope): description"

# 推送当前分支
git push -u origin HEAD

# 在开发分支中合入最新 dev
git switch dev
git pull --ff-only origin dev
git switch feature/<事项编号>-<简短说明>
git merge dev
git push -u origin HEAD
```

---

维护本文件时，应同时通知项目成员，并在 PR 中说明规范变更及其生效范围。
