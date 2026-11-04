# 欢迎来到 MkDocs 文档站

这是「开源软件开发与设计」**实验二：GitHub Action 和 GitHub Pages 使用**的文档站点。

整个站点由 MkDocs + Material 主题生成，并通过 **GitHub Actions 自动构建、自动部署**到 GitHub Pages，
无需在本地手动执行任何发布命令。

## 这个站点演示了什么

<div class="grid cards" markdown>

- :material-test-tube: **持续集成**

    ---

    每次 `git push` 之后，GitHub 会自动在云端启动一台 Ubuntu 运行器，
    执行 `pytest` 单元测试，并把结果反馈到提交记录上。

- :material-rocket-launch: **持续部署**

    ---

    当 `docs/` 目录或 `mkdocs.yml` 发生变化时，部署工作流会自动构建静态站点，
    并把产物推送到 `gh-pages` 分支，由 GitHub Pages 对外托管。

</div>

## 站内导航

- [关于](about.md)：实验背景与仓库结构
- [指南](guide.md)：工作流配置说明与本地使用方法
- [API](api.md)：`calculator` 模块的接口说明

!!! tip "试试点击右上角的搜索框"
    站点内置了中文全文搜索，可以直接搜索「工作流」「部署」等关键词。
