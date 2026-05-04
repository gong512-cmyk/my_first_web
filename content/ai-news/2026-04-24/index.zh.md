---
title: "张咋了AI资讯 2026-04-24"
date: 2026-04-24
tags: [AI资讯]
cover: gradient-1
summary: "**OpenAI ChatGPT自定义agents上线，知识工作进入headless时代**：Sam Altman称大多数公司都会采用。Box CEO Aaron Levie展示Box作为知识源与ChatGPT agents集成，通过MCP…"
---

## 今日3点

1. **OpenAI ChatGPT自定义agents上线，知识工作进入headless时代**：Sam Altman称大多数公司都会采用。Box CEO Aaron Levie展示Box作为知识源与ChatGPT agents集成，通过MCP和CLI安全访问企业内容，认为这是软件走向headless的最大新闻，将让知识工作agents普及到大众。
   - https://x.com/sama/status/2047017964105597009
   - https://x.com/levie/status/2047028112626749645

2. **"AI三明治"理论：人类是面包，AI是夹心**：Quora GM Kieran Klaassen在Every播客中提出，人类应在工作流两端（开头定框架、结尾做打磨）深度参与，中间执行层可信任AI。他创建的Compound Engineering通过"plan-work-review-compound"四步法，将经验复用回代码库，让一人抵五人。
   - https://www.youtube.com/watch?v=G0LTv8hQ5Cs
   - https://x.com/danshipper/status/2047027507397005367

3. **Vercel安全调查披露近1PB日志分析结果**：CEO Guillermo Rauch公布，威胁行为者通过分发恶意软件广泛窃取开发者token，攻击范围超出最初的Context.ai事件。Vercel已联合Microsoft、AWS、Wiz加强防护，并通知其他潜在受害者轮换凭证。
   - https://x.com/rauchg/status/2047150411170320808

## X / 建造者动态

**Sam Altman (OpenAI CEO)**
- 评论ChatGPT自定义agents："These are cool! I think most companies will want to use them."
  - https://x.com/sama/status/2047017964105597009

**Aaron Levie (Box CEO)**
- 详细展示ChatGPT agents与Box集成：自定义sales assistant可安全访问企业内容回答问题并生成内容，通过MCP和CLI调用Box工具。认为这是headless软件和知识工作agents的重大突破。
  - https://x.com/levie/status/2047028112626749645

**Guillermo Rauch (Vercel CEO)**
- 公布安全调查深度分析：处理近1PB日志，发现威胁者通过恶意软件窃取Vercel账户等服务商的token，获取后快速枚举非敏感环境变量。已扩大与Microsoft、AWS、Wiz合作，并通知其他受害者。
  - https://x.com/rauchg/status/2047150411170320808

**Amjad Masad (Replit CEO)**
- 发布白皮书：结合静态分析工具可让当前LLM性能显著提升（部分场景90%+）。
- Replit Security Agent正在持续审核应用安全。
- Replit Agent现已可从Gemini Enterprise直接调用。
  - https://x.com/amasad/status/2047156858214035590
  - https://x.com/amasad/status/2047150876423516384
  - https://x.com/amasad/status/2047149103294091301

**Kieran Klaassen (Quora GM / Compound Engineering作者)**
- 在Every播客中阐述"AI三明治"和Compound Engineering哲学：plan、work、review、compound四步法。核心洞察是work阶段已基本解决，人类应专注于开头的ideate/brainstorm和结尾的polish，让AI处理中间执行。
  - https://www.youtube.com/watch?v=G0LTv8hQ5Cs

**Ryo Lu (Cursor设计)**
- 长文警告"overcooking"（过度设计）：AI使添加功能的成本趋近于零，导致产品在"合理"的累积中失去焦点。每个决定单独看都有道理，但合在一起就是混乱。需要的是看穿混乱、回归本质、敢于削减。
  - https://x.com/ryolu_/status/2046957675079237668

**Garry Tan (YC CEO)**
- 分享技能设计经验：更少但更"厚"的技能（fewer fatter skills）使resolver更短，减少上下文膨胀。当遇到相邻技能时，他会要求AI将其DRY成更大的参数化技能。
  - https://x.com/garrytan/status/2047184243164651648
  - https://x.com/garrytan/status/2047183884266402275

**Peter Yang**
- 提出"Craft > slop"：AI生成很好，但craft在于最后10%——手动应用你的品味，做出能为之骄傲的东西。很多人从不 bother。
  - https://x.com/petergyang/status/2047124883071816189

**Josh Woodward (Google VP / Gemini)**
- Gemini App推出"对话分支"（Conversation branching）功能，已开始20% rollout。
  - https://x.com/joshwoodward/status/2047147030351642914

**Swyx**
- 提出GPT-Image-2-Thinking的最佳理解框架：它不是单纯的图像模型，而是拥有搜索和Photoshop工具的图像AGENT，能在agent循环中搜索、合成、自我审查。类比Gemini Flash Vision通过agentic loop颠覆image-to-text基准。
  - https://x.com/swyx/status/2047140362771132544

**Dan Shipper (Every CEO)**
- 发布与Kieran的播客，讨论LLM已比大多数工程师写得好，人类还剩下什么？答案是：我们是面包。
  - https://x.com/danshipper/status/2047027507397005367

**Aditya Agarwal (South Park Commons GP)**
- 分享"owner mode"领导力：承担风险与不确定性，快速学习并通过判断力赢得信任。
  - https://x.com/adityaag/status/2047024961571692747

**Nikunj Kothari**
- 判断"每个像素都将实时生成，只是时间问题"，点赞相关demo。
  - https://x.com/nikunj/status/2047024714116419665

**Peter Steinberger**
- 分享高密度React组件截图（8 components per line）并表达喜爱。
  - https://x.com/steipete/status/2046991196786979210

**Claude (Anthropic)**
- Claude Cowork新增交互式图表和diagram功能，beta版面向所有付费计划用户。
  - https://x.com/claudeai/status/2047047633416397076

## 官方博客

**Claude Blog: Redesigning Claude Code on desktop for parallel agents**
- Anthropic重新设计Claude Code桌面版，支持并行agents和新侧边栏。开发者现在可以在多个repo中同时启动任务，通过拖拽布局自定义工作区，集成终端和文件编辑器，支持SSH到Mac和Linux远程机器。新增三种视图模式（Verbose/Normal/Summary）和实时流式响应。
  - https://claude.com/blog/claude-code-desktop-redesign

## 播客

**AI & I by Every: The AI Sandwich: Where Humans Excel in an AI World**
- Quora GM Kieran Klaassen与Every CEO Dan Shipper对谈，提出"AI三明治"理论：人类是面包（开头定框架+结尾打磨），AI是夹心（中间执行）。Kieran详细介绍Compound Engineering四步法：Plan（规划）→ Work（AI执行）→ Review（审查）→ Compound（将经验复用回系统）。核心判断：Work阶段已基本解决，人类应在ideate/brainstorm和最终polish环节深度参与，这样才能做出有品味、有个人印记的作品。
  - https://www.youtube.com/watch?v=G0LTv8hQ5Cs

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
