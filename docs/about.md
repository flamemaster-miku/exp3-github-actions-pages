# 关于本实验

## 实验目的

1. **GitHub Actions 使用**
    - 创建基本的 GitHub Actions 工作流配置文件；
    - 触发工作流运行并观察其执行过程；
    - 验证工作流是否成功执行。
2. **GitHub Pages 使用**
    - 掌握使用 GitHub Actions 实现静态网站（MkDocs 文档）的自动化构建与部署；
    - 最终通过 GitHub Pages 托管可访问的文档网站。

## 仓库结构

```text
.
├── calculator.py                  # 被测试的简单计算器模块
├── test_calculator.py             # pytest 单元测试
├── mkdocs.yml                     # MkDocs 配置文件
├── docs/                          # Markdown 文档源文件
│   ├── index.md                   # 首页
│   ├── about.md                   # 关于（本页）
│   ├── guide.md                   # 指南
│   └── api.md                     # API 说明
└── .github/
    └── workflows/
        ├── test.yml               # 单元测试工作流
        └── deploy.yml             # MkDocs 自动部署工作流
```

## 技术栈

| 组件 | 版本 / 说明 |
| --- | --- |
| 运行器 | `ubuntu-latest`（GitHub 托管） |
| Python | 3.11 |
| 测试框架 | pytest |
| 文档框架 | MkDocs + Material for MkDocs |
| 部署动作 | `JamesIves/github-pages-deploy-action@v4` |
| 托管 | GitHub Pages（`gh-pages` 分支） |
