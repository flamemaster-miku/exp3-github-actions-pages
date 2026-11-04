# 实验二：GitHub Action 与 GitHub Pages 使用

本项目是「开源软件开发与设计」实验二的实践仓库，用于演示：

1. **GitHub Actions**：每次 push / pull_request 时自动运行 pytest 单元测试；
2. **GitHub Pages + MkDocs**：通过 GitHub Actions 自动构建 MkDocs Material 文档站点，并部署到 `gh-pages` 分支对外访问。

## 目录结构

```
.
├── calculator.py              # 被测试的简单计算器模块
├── test_calculator.py         # pytest 单元测试
├── .github/workflows/
│   ├── test.yml               # 单元测试工作流
│   └── deploy.yml             # MkDocs 自动部署工作流
├── docs/                      # Markdown 文档源文件
└── mkdocs.yml                 # MkDocs 配置文件
```

## 本地运行测试

```bash
pip install pytest
pytest -v
```

## 文档站点

<https://flamemaster-miku.github.io/exp3-github-actions-pages/>
