---
title: "张咋了AI资讯 2026-05-02"
date: 2026-05-02
tags: [AI资讯]
cover: gradient-3
summary: "**Claude Security 公测 + Claude Code 桌面版大改版** — Anthropic 本周连发重磅：Claude Security 正式进入公测，利用 Opus 4.7 对代码库进行漏洞扫描，支持定时扫描、目录级粒…"
---

## 今日3点

1. **Claude Security 公测 + Claude Code 桌面版大改版** — Anthropic 本周连发重磅：Claude Security 正式进入公测，利用 Opus 4.7 对代码库进行漏洞扫描，支持定时扫描、目录级粒度、CSV/Markdown 导出和 Webhook 通知；同时 Claude Code 桌面版全面重构，新增多会话并行管理、集成终端与文件编辑器、拖拽布局，适配 Agent 并行工作流。
2. **Codex 大幅升级，向通用知识工作拓展** — Sam Altman 亲自宣布 Codex 大升级，强调非编码场景的计算机操作能力。Swyx 在 AI Engineer 闭门演讲中称"Agent 突破隔离"是年度主题，他用 OpenClaw、Devin、Townie 运营团队，已服务约百万月活开发者。
3. **Agent 原生经济倒逼软件商业模式重构** — Box CEO Aaron Levie 发表长文：Agent 将成为软件最大用户群体，所有软件必须支持 Headless API 访问；传统座椅定价难以覆盖 Agent 用量，按量消费模式将成为主流。

## X / 建造者动态

### Andrej Karpathy（前 Tesla AI 总监、OpenAI 创始成员）
在 Sequoia Ascent 2026 炉边谈话中提出三个 LLM 新边疆：(1) menugen 类应用可完全由 LLM 原生运行，无需传统代码；(2) 用 install.md 替代 install.sh，LLM 作为"英语解释器"智能适配安装环境；(3) LLM 知识库处理非结构化数据，这是传统代码无法实现的功能。他进一步解释 LLM"锯齿能力"的根源——不仅与领域可验证性有关，还与经济性相关：前沿实验室根据收入/TAM 决定 RL 训练数据分布。**"你要么在数据分布的铁轨上飞驰，要么在丛林里用砍刀开路。"** 最后描绘 Agent 原生经济：产品拆解为传感器、执行器与逻辑三层，由 1.0/2.0/3.0 计算范式分工协作。
- 原文链接：https://x.com/karpathy/status/2049903821095354523

### Swyx（AI Engineer 创始人）
在 AI Engineer EU 闭幕演讲中提出 **"'Agent 突破隔离'是年度主题"**，并展示如何用 Agent 运营 AI Engineer 团队，以极小的团队规模免费服务全球约百万月活开发者。个人使用 OpenClaw，团队使用 Devin 和 Townie。"这不是关于某一个 Agent，而是关于所有 Agent，以及你可能还不够努力在日常知识工作中使用它们。"
- 原文链接：https://x.com/swyx/status/2050068468498842058

### Aaron Levie（Box CEO）
发表长文论述 Agent 时代的软件商业模式。核心判断：**Agent 将成为软件最大用户，不用 UI、只调 API。** 三点预测：(1) 人类座椅不会消失，但每个座椅必须附带充足的 API 用量额度供 Agent 调用；(2) Agent 可能需要自己的"座椅"，但定价不能按人头——一家公司可能用 1 个 Agent 也可能用 1000 个；(3) 超出座椅额度的 Headless 用量将走向按量消费模式。**"整体增长空间几乎无限——Agent 对数据的操作量将远超人类今天使用数据和工具的方式。"**
- 原文链接：https://x.com/levie/status/2050051426446152159

### Sam Altman（OpenAI CEO）
宣布 Codex 迎来重大升级，特别强调非编程类计算机操作能力。同时调侃"Artificial Goblin Intelligence"已实现。
- 原文链接：https://x.com/sama/status/2049946120441520624

### Cat Wu（Anthropic Claude Code 团队）
宣布 Claude Security 进入公开测试阶段，已集成到 Web 版 Claude Code 中。指向代码仓库即可获得经过验证的漏洞发现，并在同一工作流中修复。
- 原文链接：https://x.com/_catwu/status/2049964403177689130

### Ryo Lu（Cursor 设计师）
发表深度设计哲学思考：**"无观点本身就是一种强烈的观点"。** 伟大系统的设计不是堆砌功能，而是将概念缩减到本质——核心概念应该少而持久，系统应该能在不破坏底层逻辑的前提下折叠成多种形态。**"简单在内核，开放于边缘，这才是终极观点。"** 同时将 Cursor SDK 集成到 ryOS 中，实现"通过聊天编辑操作系统"。
- 原文链接：https://x.com/ryolu_/status/2049866003287576978

### Amjad Masad（Replit CEO）
提出 **"Prompt → LLC"** 概念，强调 Replit 将自身作为零号客户使用产品，追求极致的 AI 驱动 ROI。
- 原文链接：https://x.com/amasad/status/2049934937688854993

### Peter Steinberger（OpenClaw 创始人）
宣布 OpenClaw 群聊体验大幅改善，推荐用户升级体验；同时公布了与 NVIDIA、OpenAI、Microsoft、GitHub、腾讯混元、Convex、Atlassian、Blacksmith 等合作的安全生态建设成果。
- 原文链接：https://x.com/steipete/status/2049988836160074022

### Garry Tan（YC CEO）
推荐 GBrain 作为 Hermes Agent / OpenClaw 的知识增强方案：**"安装在 Karpathy 风格知识维基之上，将带来巨大回报。"** GBrain 采用 MIT 开源许可，已明显区别于 Mempalace 等传统检索方案，更适配个人 AI 场景。
- 原文链接：https://x.com/garrytan/status/2050096324100682097

### Amanda Askell（Anthropic 哲学家/伦理学家）
公开谴责网络上关于她的虚假内容越来越多，称"廉价地胡说很容易，但亲身体验时还是很奇怪"。同时强调自己的 AI 伦理与对齐工作是顶尖级别的有趣和重要。
- 原文链接：https://x.com/AmandaAskell/status/2050020603323904369

### 其他值得关注

- **Guillermo Rauch（Vercel CEO）**：用 2 个 prompt 让 v0 生成了"如果 Vercel 收购 GitHub 会怎样"的趣味设计。[链接](https://x.com/rauchg/status/2049959307941179678)
- **Dan Shipper（Every CEO）**：实验用 Codex + Chronicle 做专注追踪器。[链接](https://x.com/danshipper/status/2049913064561258986)
- **Nikunj Kothari（FPV Ventures）**：预测 MCP/CLI 工具表明大型模型将成为生活编排核心——"先是终端，然后是计算机操作，很快是整个操作系统。"[链接](https://x.com/nikunj/status/2049871924105531672)

## 官方博客

### Claude Blog：Redesigning Claude Code on desktop for parallel agents
Claude Code 桌面版迎来重大重新设计。核心变化：新增侧边栏管理多个并行会话，支持按状态/项目/环境筛选和分组；加入拖拽布局、集成终端和文件编辑器；新增侧聊功能（⌘+;）可在不污染主线程的情况下分支对话；三种视图模式（Verbose/Normal/Summary）控制工具调用的透明度；SSH 支持扩展至 Mac。底层已为可靠性和速度重建，现在支持流式响应。所有 Pro/Max/Team/Enterprise 用户可用。
- 原文链接：https://claude.com/blog/claude-code-desktop-redesign

## 播客

### Training Data：Demis Hassabis on Building DeepMind, AlphaFold, and the Final Stretch to AGI
DeepMind 创始人 Demis Hassabis 在 Sequoia 对话中回顾了从象棋天才到 AGI 探索者的完整路径。核心观点：

**AGI 时间线**：坚持 2030 年前后实现 AGI 的判断，"我们 2010 年预测是 20 年任务，现在来看整个领域基本在轨道上。"

**创业心得**：**"你想领先时代五年，而不是五十年。"** 他在 Elixir Studios 时尝试在奔腾处理器上模拟百万人口城市，过于超前导致困难——这个教训贯穿了 DeepMind 的研发节奏。

**AI for Science 路线图**：AlphaFold 之后，Isomorphic Labs 正在构建相邻的生化技术栈，目标是 **"将药物发现从平均十年缩短到几个月甚至几周"**。如果能实现硅基探索（in silico）覆盖 99% 工作，"所有疾病都可能触手可及"。

**信息本质论**：Hassabis 认为信息（而非物质或能量）是宇宙最基本的构成——这一哲学立场直接支撑了 DeepMind 以 AI 理解世界的终极使命。

**AI 与意识**：**"我强烈建议我们先构建工具——极其智能、有用且精确的工具——然后再跨过下一个卢比孔河。"** 关于意识问题，他认为自我觉知、自他区分、时间连续性可能是必要条件但不充分。

**最欣赏的思想家**：康德（"心灵创造现实"）和斯宾诺莎（"宇宙深层奥秘的灵性面向"）。如果选一位历史科学家作为策略游戏队友，选冯·诺依曼——"你想要一个博弈论专家。"

🎧 完整节目：https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
