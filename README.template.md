# AI Trending Archive

[![Daily Github Trending](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/schedule_daily.yml/badge.svg)](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/schedule_daily.yml)

Track and archive AI projects discovered on GitHub Trending.

<!-- SUMMARY -->

## Features

- Daily updates at **09:00 (UTC+8)** with GitHub Actions.
- Daily Trending lists for all languages, Go, Python, JavaScript, Java, C, C++, and TypeScript.
- AI projects across multiple languages, including LLMs, agents, machine learning, and model infrastructure.
- Deduplicated entries with first-seen dates, monthly archives, and daily JSON snapshots.
- No API keys or third-party dependencies required.

## Getting Started

Requires Python **3.12+**.

```bash
git clone https://github.com/zengzzzzz/ai-trending-archive.git
cd ai-trending-archive
python scraper.py
```

Edit `config.json` to customize languages, keyword filters, and repository inclusion or exclusion. Use `--since weekly` or `--since monthly` for other Trending periods.

Projects are filtered by repository names and descriptions, so results may include false matches or miss relevant projects. Original project descriptions are preserved.

## Automation

Run **Actions → Daily Github Trending → Run workflow** for a manual update. Run **Actions → Monthly Github Trending Archive → Run workflow** to archive completed months. Monthly archiving runs at **08:00 (UTC+8) on the first day of each month**; projects are listed once by their first-seen month.

Edit `README.template.md` to change this page. Run `python -m unittest discover -s tests -v` to test locally.

## New This Month

<!-- ENTRIES -->
