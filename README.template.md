# AI Trending Archive

[![Daily AI Trending](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml/badge.svg)](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml)

每天发现 GitHub Trending 上的 AI 开源项目，自动去重、记录首次发现日期，并按月归档。

<!-- SUMMARY -->

## 功能

- 每天北京时间 **09:17** 自动更新，也可以在 Actions 页面手动运行。
- 同时扫描全语言、Python、TypeScript、JavaScript、Jupyter Notebook、C++、Rust、Go 的日榜。
- 覆盖 LLM、生成式 AI、Agent、MCP、机器学习、视觉语音、RAG 和模型基础设施。
- README 展示本月首次发现的项目；`archived/YYYY-MM.md` 保存月度记录，同一项目跨月不重复收录。
- `data/daily/YYYY-MM-DD.json` 保存每日完整匹配结果、榜单来源、排名和当期新增 Star；`data/repositories.json` 保存首次及最近发现日期。
- 使用 GitHub Actions 自带的 `GITHUB_TOKEN` 提交更新；无需配置个人 Token、模型 API Key 或付费服务。

## 收录规则与局限

数据来自 [GitHub Trending](https://github.com/trending)，**不是 GitHub 官方 AI 分类榜单**。程序只从配置的 Trending 榜单中，根据仓库名称及简介的中英文关键词筛选项目；不使用模型评分，不扫描整个 GitHub，也不代表 AI 项目的完整排名。`config.json` 中的分类可以多选。

关键词规则可能误收或漏收，尤其是简介未提及 AI 的仓库。可以调整分类的正则表达式，或者用 `include_repositories` / `exclude_repositories` 指定 `owner/repo`；人工收录仍需项目出现在扫描的榜单中。`period_stars` 是来源榜单显示的当期增量，不是本程序自行计算的日增量；没有显示时记录为 `null`。

当天重复运行会合并结果，同一项目只保留一条首次收录记录。任一来源抓取失败、响应被拦截或页面结构变化导致无仓库卡片时，本次运行失败并保留现有归档。未出现新的 AI 项目时仍会保存当天快照。

月度文件在每日更新时自动生成，首次跨月运行时 README 自动切换到新月份，不需要额外的清空 README 任务。GitHub 定时任务可能延迟；公共仓库连续 60 天无活动时，GitHub 可能停用定时工作流，可到 Actions 页面重新启用。

## 本地运行

需要 Python **3.12 或更新版本**，仅使用标准库。

```bash
git clone https://github.com/zengzzzzz/ai-trending-archive.git
cd ai-trending-archive
python -m unittest discover -s tests -v
python scraper.py
```

默认使用 `config.json` 的日榜。也可以抓取周榜、月榜，或通过修改 `periods` 同时抓取多个周期：

```bash
python scraper.py --since weekly
python scraper.py --since monthly
```

README 由 `README.template.md` 生成，修改项目说明时请编辑模板。分类和语言来源在 `config.json` 中配置。

## 自动运行

工作流 `.github/workflows/update.yml` 每天抓取、更新并提交数据，仅在文件变化时提交。新仓库首次推送会立即触发一次；也可以在 **Actions → Daily AI Trending → Run workflow** 手动触发。离线测试在每次 push 和 pull request 时运行。

如果 fork 后需要启用自动归档，请先在 Actions 页面启用工作流。工作流已经声明 `contents: write`；如组织策略限制写入权限，需要由仓库管理员允许 Actions 写入。

## 致谢

参考 [zengzzzzz/golang-trending-archive](https://github.com/zengzzzzz/golang-trending-archive) 的每日抓取、去重收录和月度归档功能，以及其上游 [aneasystone/github-trending](https://github.com/aneasystone/github-trending)。

## 本月新发现

<!-- ENTRIES -->
