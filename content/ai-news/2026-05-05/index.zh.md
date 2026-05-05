---
title: "张咋了AI资讯 2026-05-05"
date: 2026-05-05
tags: [AI资讯]
cover: gradient-2
summary: "Andrej Karpathy 提出 Software 3.0 范式——编程从写代码转向给 Agent 发指令，提示词即代码，上下文窗口就是新的程序杠杆。"
---

## 今日3点

1. Andrej Karpathy 提出 Software 3.0 范式——编程从写代码转向给 Agent 发指令，提示词即代码，上下文窗口就是新的程序杠杆。
2. Sam Altman 称 Agents SDK 2.0 被低估，同时长文致敬 Greg Brockman 的技术才华与坚持。
3. Aaron Levie 长推拆解企业 Agent 落地的真实复杂度：数据打通、权限控制、流程文档化、评估体系建设，每一环都是硬仗。

## X / 建造者动态

**Andrej Karpathy**（前 OpenAI 创始成员、前 Tesla AI 总监）

Karpathy 在 Training Data 播客中系统阐述了从 vibe coding 到 agentic engineering 的演进。他指出去年 12 月是 Agent 能力的质变点——模型输出的代码块不再出错，他可以无限信任地让 Agent 完成整个项目。他将软件发展划分为三个阶段：Software 1.0 是显式规则编程，Software 2.0 是用数据集训练神经网络，Software 3.0 则是通过提示词在上下文窗口中"编程"，让 LLM 作为解释器执行。他以 OpenClaw 安装和 MenuGen 应用为例，说明大量传统代码在 Software 3.0 范式下其实"不应该存在"——神经网络可以直接完成端到端的输入输出转换。他进一步预测，未来可能出现"完全神经化的计算机"，神经网络成为主进程，CPU 退化为协处理器。Karpathy 特别强调可验证性（verifiability）决定 Agent 的适用边界：模型在可验证领域（数学、代码）表现突出，在非验证领域则参差不齐。他给创业者的建议是，寻找可验证但实验室尚未覆盖的垂直领域，通过自建强化学习环境做微调。他还区分了 vibe coding（抬高能力地板）和 agentic engineering（保持专业质量天花板）——后者才是真正的工程学科，优秀的 Agentic Engineer 提速远超 10 倍。最后，他认为人类在 taste、判断和 oversight 上的价值不会降低，因为 Agent 目前仍是"实习生水平"，会犯低级错误。

- https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8

**Sam Altman**（OpenAI CEO）

Altman 发了一条简短的推文："Agents SDK 2.0 is underrated"，直接为自家产品站台。同时他发布长文致敬 Greg Brockman，称"无法想象没有 Greg 的 OpenAI"，并补充说他之前写的文章"没有充分突出 Greg 的技术才华和 sheer determination"。

- https://x.com/sama/status/2050998576671859003
- https://x.com/sama/status/2050964008480723059

**Aaron Levie**（Box CEO）

Levie 发表长推指出，企业 Agent 落地的复杂度被严重低估。从聊天范式转向参与实际工作流，企业需要完成：跨系统数据安全接入、权限与范围控制、流程文档化、人机协作新流程设计、为顶级流程建立评估体系，以及持续跟进快速变化的 Agent 架构最佳实践。他认为这将在咨询公司、Agent 厂商和内部工程角色中创造大量新工作，垂直 AI Agent 是巨大机会。

- https://x.com/levie/status/2051057677984469277

他还转发了一条关于"应把 AI 当作工具而非生命体"的推文并评论：混淆 AI 的本质只会让我们用永远无法完全成立的类比把自己逼疯。

- https://x.com/levie/status/2051009208393589096

**Garry Tan**（Y Combinator CEO）

Tan 连续发文强调个人 AI 栈的重要性。他称 GBrain 开源的原因是"智能爆炸意味着自建上下文比以往任何时候都更重要"。他的愿景是：个人 AI 的终极目标是让个体人类在 AI 增强下完成重要工作，而不被剥削性机构捕获——自由编写提示词、拥有自己的数据，这是新的战场。他还介绍了 GBrain 的功能：支持多仓库、多 MCP 端点、OAuth 和 Bearer Token，管理员面板可通过 OpenClaw 或 Hermes 一键获取。

- https://x.com/garrytan/status/2051110206466302136
- https://x.com/garrytan/status/2051099735176659256
- https://x.com/garrytan/status/2051089704658010321

**Zara Zhang**（Builder、Follow Builders 作者）

Zhang 转发并推荐了一条关于人机 Agent 交互的演示视频，称这是她"一段时间以来见过的最酷的 demo"。她还引用一条推文并评论：AI 前你造不起小东西，因为软件开发成本太高，必须通过委员会；现在只有你和一个编码 Agent，它不需要被说服，会欣然建造任何疯狂的想法——所以去造那些在大厂评审会上会被拒绝的东西吧。

- https://x.com/zarazhangrui/status/2051192270632993176
- https://x.com/zarazhangrui/status/2051155065331941873

**Amjad Masad**（Replit CEO）

Masad 展示 Replit 上的 Agent 并行数据：10 个活跃、198 个草稿、700+ 已完成。他称"互联网上没有任何地方的 Agent 并行度比 Replit 更高"。他还分享了一天马拉松式 vibe coding 的成果。

- https://x.com/amasad/status/2051167532523074015
- https://x.com/amasad/status/2051007848440877242

**Peter Yang**（Roblox Product）

Yang 分享了一个实用技巧：用 Amphetamine 应用保持 MacBook 合盖时 Agent 继续运行。他还提到自己"屈服了"下载了 Hermes，向社区征求 Hermes 与 OpenClaw 的诚实对比。

- https://x.com/petergyang/status/2050963126234034387
- https://x.com/petergyang/status/2051129249348894754

**Peter Steinberger**（OpenClaw）

Steinberger 发布了 RepoBar 0.4.0，增加了 SQLite 缓存、API 速率限制可视化、Issues/PR 加载优化等功能。他还预告了新的 Claw Beta 版本。

- https://x.com/steipete/status/2051088325100831046
- https://x.com/steipete/status/2051033065367970195

**Swyx**（Latent Space）

Swyx 分享了 Training Data 播客在 YouTube 免费观看的链接，并提到自己花三年时间完成了第二篇短篇小说。

- https://x.com/swyx/status/2051115027210346936
- https://x.com/swyx/status/2051025640657449249

**Dan Shipper**（Every CEO）

Shipper 表示本周没有 Mythos 通讯，但暗示有有趣的内容即将发布。

- https://x.com/danshipper/status/2050997402514161781

**Nikunj Kothari**（FPV Ventures）

一条励志推文：关于坚持的力量。

- https://x.com/nikunj/status/2051096096110502063

## 官方博客

今日无新博客文章。

## 播客

**Training Data: Andrej Karpathy: From Vibe Coding to Agentic Engineering**

Karpathy 做客 Training Data 首期节目，深入探讨从 vibe coding 到 agentic engineering 的范式转换。核心观点：Software 3.0 时代，编程变成给 Agent 发指令，提示词即代码；大量传统应用代码在神经网络端到端能力面前显得多余；未来可能出现"神经网络为主、CPU 为辅"的计算机架构；可验证性决定 Agent 能力边界；vibe coding 抬高地板，agentic engineering 保持专业天花板。

- https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
