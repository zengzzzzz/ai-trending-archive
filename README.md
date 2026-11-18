# AI Trending Archive

[![Daily AI Trending](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml/badge.svg)](https://github.com/zengzzzzz/ai-trending-archive/actions/workflows/update.yml)

每天发现 GitHub Trending 上的 AI 开源项目，自动去重、记录首次发现日期，并按月归档。

最近更新：**2026-11-18（北京时间）** · 累计收录 **51** 个项目 · 本月新发现 **51** 个 · 今日发现 **51** 个 AI 项目

[当天 JSON 快照](data/daily/2026-11-18.json) · [完整项目索引](data/repositories.json) · [历史月度归档](archived/README.md)

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

* 【2026-11-18】[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) - Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。  
  `Go` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/Wei-Shaw/sub2api?style=social)

* 【2026-11-18】[vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) - Fully autonomous AI Agents system capable of performing complex penetration testing tasks  
  `Go` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=social)

* 【2026-11-18】[vllm-project/vllm-ascend](https://github.com/vllm-project/vllm-ascend) - Community maintained hardware plugin for vLLM on Huawei Ascend  
  `Python` · 检索、向量与模型基础设施 · ![Stars](https://img.shields.io/github/stars/vllm-project/vllm-ascend?style=social)

* 【2026-11-18】[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code & Codex — cinematic, editable product promos with Remotion: 124 shot recipe cards, 150 motion previews, beat sync, sound design, Motion Workbench & JianYing (CapCut CN) export.  
  `TypeScript` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/Vincentwei1021/video-shotcraft?style=social)

* 【2026-11-18】[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) - An Open Source Machine Learning Framework for Everyone  
  `C++` · 机器学习与深度学习 · ![Stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social)

* 【2026-11-18】[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) - Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.  
  `Go` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/TencentCloud/CubeSandbox?style=social)

* 【2026-11-18】[Tencent/LoopForge](https://github.com/Tencent/LoopForge) - Self-hosted workflows for coding-agent delivery. Orchestrate CodeBuddy, Codex and Claude Code with scripts and human approval gates. Includes Local workflows for coding assistants.  
  `Go` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/Tencent/LoopForge?style=social)

* 【2026-11-18】[SaladDay/cc-switch-cli](https://github.com/SaladDay/cc-switch-cli) - ⭐️ A cross-platform CLI All-in-One assistant tool for Claude Code, Codex & Gemini CLI.  
  `Rust` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/SaladDay/cc-switch-cli?style=social)

* 【2026-11-18】[qwdwqfwq/topconf-paper-figure-gallery](https://github.com/qwdwqfwq/topconf-paper-figure-gallery) - 3,516 curated Figure 1 / teasers from ICLR, ICML, NeurIPS, CVPR, ACL, AAAI (2023-2026), with tier badges and FigureForge retrieval-augmented figure drafting  
  `JavaScript` · 检索、向量与模型基础设施 · ![Stars](https://img.shields.io/github/stars/qwdwqfwq/topconf-paper-figure-gallery?style=social)

* 【2026-11-18】[QuantumNous/new-api](https://github.com/QuantumNous/new-api) - Open-source AI gateway. Self-hosted LLM gateway with OpenAI-, Claude- and Gemini-compatible APIs, model routing, access control, usage tracking and cost accounting.  
  `Go` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/QuantumNous/new-api?style=social)

* 【2026-11-18】[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - A collection of MCP servers.  
  `Unknown` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=social)

* 【2026-11-18】[pugarte7/spanish-top-tech-companies](https://github.com/pugarte7/spanish-top-tech-companies) - MCP con las mejores ofertas tech de España, para que tus agentes puedan aplicar por ti de forma automática.  
  `JavaScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/pugarte7/spanish-top-tech-companies?style=social)

* 【2026-11-18】[pingdotgg/t3code](https://github.com/pingdotgg/t3code) - The best way to control Claude Code, Codex and more from any computer or phone  
  `TypeScript` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/pingdotgg/t3code?style=social)

* 【2026-11-18】[openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) - OpenVINO™ is an open source toolkit for optimizing and deploying AI inference  
  `C++` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/openvinotoolkit/openvino?style=social)

* 【2026-11-18】[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) - Secure, Fast, and Extensible Sandbox runtime for AI agents.  
  `Go` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=social)

* 【2026-11-18】[openai/whisper](https://github.com/openai/whisper) - Robust Speech Recognition via Large-Scale Weak Supervision  
  `Python` · 视觉、语音与多模态 · ![Stars](https://img.shields.io/github/stars/openai/whisper?style=social)

* 【2026-11-18】[obra/superpowers](https://github.com/obra/superpowers) - An agentic skills framework & software development methodology that works.  
  `Shell` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/obra/superpowers?style=social)

* 【2026-11-18】[NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) - Multi-tier framework for evaluating AI agent skills and plugins with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.  
  `Python` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/NVIDIA/SkillEvaluator?style=social)

* 【2026-11-18】[NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) - 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.  
  `Jupyter Notebook` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/NirDiamant/GenAI_Agents?style=social)

* 【2026-11-18】[n8n-io/n8n](https://github.com/n8n-io/n8n) - Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.  
  `TypeScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/n8n-io/n8n?style=social)

* 【2026-11-18】[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) - AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary  
  `Python` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/mvanhorn/last30days-skill?style=social)

* 【2026-11-18】[mrdbourke/zero-to-mastery-ml](https://github.com/mrdbourke/zero-to-mastery-ml) - All course materials for the Zero to Mastery Machine Learning and Data Science course.  
  `Jupyter Notebook` · 机器学习与深度学习 · ![Stars](https://img.shields.io/github/stars/mrdbourke/zero-to-mastery-ml?style=social)

* 【2026-11-18】[Minglink/dsh-infinite-gen-5](https://github.com/Minglink/dsh-infinite-gen-5) - DeepSeek v4.1 flash 最强逆向工具（无限五代） 求 Star 收藏 ⭐欢迎大家提交项目的改进  
  `JavaScript` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/Minglink/dsh-infinite-gen-5?style=social)

* 【2026-11-18】[microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) - 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all  
  `Jupyter Notebook` · 机器学习与深度学习 · ![Stars](https://img.shields.io/github/stars/microsoft/ML-For-Beginners?style=social)

* 【2026-11-18】[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) - This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.  
  `Jupyter Notebook` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social)

* 【2026-11-18】[microsoft/BitNet](https://github.com/microsoft/BitNet) - Official inference framework for 1-bit LLMs  
  `C++` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/microsoft/BitNet?style=social)

* 【2026-11-18】[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) - 12 Weeks, 24 Lessons, AI for All!  
  `Jupyter Notebook` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners?style=social)

* 【2026-11-18】[Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) - 《动手学大模型Dive into LLMs》系列编程实践教程  
  `Jupyter Notebook` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/Lordog/dive-into-llms?style=social)

* 【2026-11-18】[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) - Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages  
  `JavaScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/Leonxlnx/taste-skill?style=social)

* 【2026-11-18】[leepokai/Codync](https://github.com/leepokai/Codync) - Open source Grok Bot alternative, Bring your own agent and subscription: message Claude Code, Codex, Gemini CLI, Cursor, Copilot and 40+ AI agents as bots on your own computer, from iPhone, Mac, Windows, Linux or terminal. Agent-agnostic and free. Also a Muse and Dots alternative. Built in Rust.  
  `Rust` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/leepokai/Codync?style=social)

* 【2026-11-18】[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) - Local video editor for coding agents: 42 FFmpeg tools with a machine-readable contract and an MCP server, for Claude Code, Cursor and Codex. Cut, captions, reframe, loudness, platform exports. No cloud, no API keys.  
  `Python` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/kajisho5/ffmpeg-skill?style=social)

* 【2026-11-18】[jingyaogong/minimind](https://github.com/jingyaogong/minimind) - 🧠 两小时从 0 训出你的 64M 大模型。Train your own 64M LLM from scratch in 2 hours.  
  `Python` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)

* 【2026-11-18】[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) - Clone any website with one command using AI coding agents  
  `TypeScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/JCodesMore/ai-website-cloner-template?style=social)

* 【2026-11-18】[huggingface/transformers](https://github.com/huggingface/transformers) - 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  
  `Python` · 机器学习与深度学习, 视觉、语音与多模态 · ![Stars](https://img.shields.io/github/stars/huggingface/transformers?style=social)

* 【2026-11-18】[google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) - PaperOrchestra is a multi-agent framework for automated AI research paper writing.  
  `Python` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/google-research/paper-orchestra?style=social)

* 【2026-11-18】[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) - A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor.  
  `TypeScript` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/google-labs-code/stitch-skills?style=social)

* 【2026-11-18】[github/awesome-copilot](https://github.com/github/awesome-copilot) - Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot.  
  `JavaScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/github/awesome-copilot?style=social)

* 【2026-11-18】[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) - LLM inference in C/C++  
  `C++` · LLM 与生成式 AI, 检索、向量与模型基础设施 · ![Stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=social)

* 【2026-11-18】[gepa-ai/gepa](https://github.com/gepa-ai/gepa) - Optimize prompts, code, and more with AI-powered Reflective Optimization  
  `Jupyter Notebook` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/gepa-ai/gepa?style=social)

* 【2026-11-18】[ethanplusai/sellbird](https://github.com/ethanplusai/sellbird) - Sellbird (formerly Harvey): the open-source outreach platform that runs on your Claude or ChatGPT plan. Finds companies and decision makers, verifies emails, writes personal cold email, sends it and handles the replies.  
  `Python` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/ethanplusai/sellbird?style=social)

* 【2026-11-18】[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) - A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.  
  `Python` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/elementalsouls/Claude-BugHunter?style=social)

* 【2026-11-18】[dream-num/univer](https://github.com/dream-num/univer) - Build your own AI office with Univer Office SDK. Bring editing, calculation, collaboration, and file processing into your product for people and AI agents. Built on an extensible open-source core.  
  `TypeScript` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/dream-num/univer?style=social)

* 【2026-11-18】[Dodaios/Dodaios](https://github.com/Dodaios/Dodaios) - One workspace for everything you do with AI: Claude Code, Codex and seven more coding agents side by side, one assistant that runs them, voice, and docs. Open source, on your computer, on your own plans and keys. Formerly Personal Jarvis.  
  `Python` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/Dodaios/Dodaios?style=social)

* 【2026-11-18】[datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) - 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程  
  `Jupyter Notebook` · LLM 与生成式 AI, 视觉、语音与多模态 · ![Stars](https://img.shields.io/github/stars/datawhalechina/self-llm?style=social)

* 【2026-11-18】[datawhalechina/diy-llm](https://github.com/datawhalechina/diy-llm) - Covers pre-training data, Tokenizer, Transformer, MoE,distributed training, Scaling Laws, inference & alignment .6 progressive code assignments for full-stack LLM learning \| 涵盖预训练数据、分词器、Transformer、MoE、分布式训练、缩放定律、推理与对齐，6 项渐进代码作业，掌握 LLM 全栈知识  
  `Jupyter Notebook` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/datawhalechina/diy-llm?style=social)

* 【2026-11-18】[DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) - LLM Zoomcamp - a free online course about real-life applications of LLMs. In 10 weeks you will learn how to build an AI system that answers questions about your knowledge base. Register here 👇🏼  
  `Jupyter Notebook` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/DataTalksClub/llm-zoomcamp?style=social)

* 【2026-11-18】[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) - Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local  
  `TypeScript` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=social)

* 【2026-11-18】[bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) - 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码  
  `Python` · AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/bojieli/ai-agent-book?style=social)

* 【2026-11-18】[anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) - An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.  
  `Python` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/anthropics/claude-code-security-review?style=social)

* 【2026-11-18】[alibaba/open-code-review](https://github.com/alibaba/open-code-review) - Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.  
  `Go` · LLM 与生成式 AI · ![Stars](https://img.shields.io/github/stars/alibaba/open-code-review?style=social)

* 【2026-11-18】[affaan-m/ECC](https://github.com/affaan-m/ECC) - The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.  
  `JavaScript` · LLM 与生成式 AI, AI Agent 与开发工具 · ![Stars](https://img.shields.io/github/stars/affaan-m/ECC?style=social)
