# 使用指南

## 一、本地运行单元测试

克隆仓库后，在项目根目录执行：

```bash
pip install pytest
pytest -v
```

预期输出：

```text
test_calculator.py::test_add PASSED                        [ 50%]
test_calculator.py::test_multiply PASSED                   [100%]
============================== 2 passed in 0.02s ==============================
```

## 二、测试工作流 `test.yml`

```yaml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest
      - name: Run tests
        run: pytest -v
```

关键点：

- `on: [push, pull_request]`：推送到任意分支、或向仓库发起 Pull Request 时都会触发；
- 每个 `step` 都是一个独立的 shell 步骤，任意一步返回非 0 退出码，整个 job 即失败；
- `pytest` 的退出码就是测试结果：全部通过返回 `0`，有失败用例返回 `1`。

## 三、部署工作流 `deploy.yml`

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install MkDocs Material
        run: pip install mkdocs-material
      - name: Build MkDocs site
        run: mkdocs build
      - name: Deploy to GitHub Pages
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          branch: gh-pages
          folder: site
```

关键点：

- `paths` 过滤器让部署只在文档发生变化时触发，避免每次改代码都重新发布站点；
- `permissions: contents: write` 是必需的，部署动作需要向仓库推送 `gh-pages` 分支；
- `mkdocs build` 会把 Markdown 渲染成静态站点，产物默认位于 `site/` 目录；
- 部署动作把 `site/` 的内容提交到 `gh-pages` 分支，GitHub Pages 再从该分支取文件对外提供访问。

## 四、本地预览文档

```bash
pip install mkdocs-material
mkdocs serve
```

然后打开 <http://127.0.0.1:8000/> 即可实时预览，修改 Markdown 后页面会自动刷新。
