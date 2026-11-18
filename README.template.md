# AI Trending Archive

[![Daily AI Trending](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml/badge.svg)](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml)

Track and archive AI projects discovered on GitHub Trending.

<!-- SUMMARY -->

## Features

- Daily updates at **09:17 (UTC+8)** with GitHub Actions.
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

Run **Actions → Daily AI Trending → Run workflow** for a manual update. Monthly archives are generated automatically; projects are listed only once by their first-seen month.

Edit `README.template.md` to change this page. Run `python -m unittest discover -s tests -v` to test locally.

## New This Month

<!-- ENTRIES -->
