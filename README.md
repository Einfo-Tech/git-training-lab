# Git Training Lab

公司内部 Git 实战训练仓库，用于练习从开发分支到测试分支、再到生产主分支的完整协作流程。

## 分支模型

- `main`：生产基线，只接收已经通过测试的版本。
- `test`：测试与验收分支，只接收从 `dev` 提升的版本。
- `dev`：日常集成分支，开发分支通过 Pull Request 合入这里。
- `feature/*`、`fix/*`：围绕单一任务创建的短生命周期分支。

## 推荐流程

```text
feature/* 或 fix/* → dev → test → main
```

详细练习见 [docs/TRAINING_GUIDE.md](docs/TRAINING_GUIDE.md)。

> 本仓库只放训练数据。禁止放入真实令牌、私钥、客户数据或生产连接信息,测试。
