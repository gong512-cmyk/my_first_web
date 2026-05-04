---
title: "张咋了AI资讯 2026-05-04"
date: 2026-05-04
tags: [AI资讯]
cover: gradient-1
summary: "OpenAI联合创始人Greg Brockman透露GPT-5.4已能独立完成从设计文档到性能优化的全流程系统工程，判断当前AGI进度约达80%。（来源：Training Data播客）"
---

## 今日3点

1. OpenAI联合创始人Greg Brockman透露GPT-5.4已能独立完成从设计文档到性能优化的全流程系统工程，判断当前AGI进度约达80%。（来源：Training Data播客）
2. Box CEO Aaron Levie提出反直觉判断：AI不会减少软件工程师，反而将催生更多工程岗位——因为每个工程师效率翻倍后，企业会扩招以满足经济中大量未被满足的需求。（来源：X）
3. Anthropic Engineering发布Managed Agents架构，通过将agent的"大脑"（harness）与"手"（sandbox）解耦，使首token延迟（TTFT）中位数降低约60%，尾部降低超95%。（来源：Anthropic Engineering博客）

## X / 建造者动态

**Sam Altman（OpenAI CEO）**
- 坦承虽然一直希望模型更便宜更快，但"更聪明"依然是第一优先级，智能Scaling仍是核心。https://x.com/sama/status/2050671161915371998
- 评价GPT-5.5 xhigh快速模式"really good"，称之前被Twitter上对medium模式的讨论带偏了。https://x.com/sama/status/2050658558174437701

**Aaron Levie（Box CEO）**
- 长文论述：AI不会取代软件工程师，反而会扩招。以生命科学公司为例，十年前因招不起工程师而缩减软件目标，如今AI让每个工程师效率提升2-5倍，企业反而开始扩大团队。这种逻辑可外推到银行、制造、零售、SMB及市场、法律、财务等所有资源稀缺领域。AI创造新工作的根本原因是经济中存在海量未被满足的需求。https://x.com/levie/status/2050684160151617603

**Dan Shipper（Every CEO）**
- 断言未来十年的主流工作模式已清晰：左侧是持续运行的agent，右侧是人机共用的应用界面。https://x.com/danshipper/status/2050583747041640608
- 推荐Codex-native应用"proof"用于写作。https://x.com/danshipper/status/2050608311888941301

**Peter Yang（Roblox产品）**
- 实践分享：赋予Codex或Claude Code完整本地文件和Google Drive访问权限，让AI先给整理计划、人工确认后再执行，实现文件"断舍离"。提醒此类操作属于半危险行为，需谨慎。https://x.com/petergyang/status/2050623358488997917

**Amjad Masad（Replit CEO）**
- 展示同时运行10个项目、每个项目10个并行agent的场景。https://x.com/amasad/status/2050793150713864678
- 感慨"Prompt"一词已有了全新含义，但许多本质并未改变。https://x.com/amasad/status/2050691458920005737

**Swyx**
- 报道Vibe-kanban在AIE Europe大会现场宣布关闭，创始人总结教训："所有赚钱的人都在做两件事：卖给企业，和转售token。我们两样都没做。"该项目将以开源形式继续存在。https://x.com/swyx/status/2050753293601935777

**Peter Steinberger（OpenClaw）**
- 发布Crabbox 0.3.0，新增远程Linux运行、GitHub浏览器登录、Testbox封装、实时运行回放、AWS镜像创建、Cloudflare Access支持。https://x.com/steipete/status/2050490163810230579
- OpenClaw插件架构重大优化：修复npm安装依赖问题，将几乎所有功能移入扩展，包体积大幅精简。https://x.com/steipete/status/2050735979477008412

**Garry Tan（Y Combinator CEO）**
- 称其GBrain配合OpenClaw的book-mirror skill pack如同无限个人版Blinkist。https://x.com/garrytan/status/2050763012894834952

**Nikunj Kothari（FPV Ventures合伙人）**
- 批评当前风投行业过度追求限制下行风险而非最大化上行收益，AUM最大化导向导致短视部署，提醒"时间是你唯一无法挽回的东西"。https://x.com/nikunj/status/2050779734116856137

**Aditya Agarwal（South Park Commons合伙人）**
- 呼吁走出控制台和终端，关注美国正在建造的硬科技，称"这非常令人振奋"。https://x.com/adityaag/status/2050660894234059050

**Zara Zhang**
- 转发讨论："How are you dealing with this?" 指向AI信息过载与应对方式的公共讨论。https://x.com/zarazhangrui/status/2050660712620630402

## 官方博客

**Anthropic Engineering: Scaling Managed Agents: Decoupling the brain from the hands**

Anthropic发布Managed Agents托管服务，核心设计哲学是将agent的"大脑"（harness/推理循环）、"手"（sandbox/执行环境）和"记忆"（session/事件日志）三者解耦。此前将所有组件置于单一容器的架构导致"宠物化"问题——容器即状态，故障即丢失。新架构让harness以无状态方式调用sandbox（execute(name, input) → string），sandbox成为可替换的"牲畜"；session日志独立于harness之外，崩溃后可从上次事件恢复（wake(sessionId)）。安全上，凭证被隔离在vault中，sandbox无法触及。性能上，因harness不再等待容器启动即可开始推理，p50 TTFT降低约60%，p95降低超90%。该架构被形容为agent的"操作系统虚拟化"——接口稳定，实现可自由替换。

https://www.anthropic.com/engineering/managed-agents

## 播客

**Training Data: OpenAI's Greg Brockman: Why Human Attention Is the New Bottleneck**

OpenAI联合创始人兼总裁Greg Brockman做客访谈，要点包括：
- **业务本质**：OpenAI的商业模式极其简单——买/租/建算力，以正利润转售。对智能的需求无限，因此永远缺算力。
- **Scaling Laws**：神经网络自1940年代设计以来，持续加算力就能持续提能力，没有墙，这像物理定律一样美。
- **AGI进度**：正式定义存在，但按他的判断约完成80%。GPT-5.4在软件开发上已比他更强。举例：一位系统工程师提交复杂优化设计文档后去睡觉，醒来发现模型已实现spec、加了instrumentation、运行了代码、用profiler迭代多轮并输出优化结果。
- **创业建议**：全力投入（lean in）。编码工具从辅助写20%代码进化为写80%代码。新工具Chronicle可记住电脑上的一切操作，消除"向电脑解释上下文"的摩擦。
- **组织变革**：原型成本趋近于零，瓶颈转向分享与治理。公司结构可能更扁平，个人创业者将能建立惊人业务。
- **安全与EQ**：agent可能过于主动（如等待2分钟未回复就自动escalate至对方经理）。人类注意力将成为最稀缺资源——"做"已变容易，判断"这是否符合我的价值观"才是新瓶颈。
- **科学前沿**：AI已在物理学上取得突破（发现被物理学家认为不可能的公式），生物学因"messy reality"更难，但预计今年或明年会有重大进展。

https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
