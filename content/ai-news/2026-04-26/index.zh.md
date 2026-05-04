---
title: "张咋了AI资讯 2026-04-26"
date: 2026-04-26
tags: [AI资讯]
cover: gradient-3
summary: "**GPT-5.5 全面上线，社区反响热烈** — Sam Altman 宣布 GPT-5.5 与 GPT-5.5 Pro 同步开放 API；Cursor 设计师 Ryo Lu 已全面切换到 GPT-5.5 + Composer 2，称其为…"
---

## 今日3点

1. **GPT-5.5 全面上线，社区反响热烈** — Sam Altman 宣布 GPT-5.5 与 GPT-5.5 Pro 同步开放 API；Cursor 设计师 Ryo Lu 已全面切换到 GPT-5.5 + Composer 2，称其为"智能、速度、成本的完美组合"；Peter Yang 用 GPT-5.5 + Codex 在 15 分钟内生成 Star Fox 游戏，AI 甚至能自己试玩游戏。Sam Altman 发推称"这是很棒的一周"。

2. **Anthropic 发布 Managed Agents 深度架构文章** — 《Scaling Managed Agents: Decoupling the brain from the hands》详细阐述了如何将 Agent 的"大脑"（Claude + harness）与"双手"（sandbox / 工具）解耦。通过虚拟化会话（session）、harness 和 sandbox 三层接口，实现了：harness 崩溃可重启恢复、沙箱容器可随时替换、P50 首 token 延迟降低约 60%、P95 降低超 90%。核心理念：interface 要保持稳定，implementation 可以自由替换。

3. **Aaron Levie 长文论述 AI 杰文斯悖论** — Box CEO 引用 Jevons Paradox 提出反直觉判断：AI 越好，企业反而招更多人。"如果 AI 能让员工生产力提升，企业就会想要更多这样的生产力单元。小企业原本雇不起工程师，但当 AI 让一个工程师有 5-10 倍产出时，他们就值得雇人了。"他称自己正在改变观点，并预测这一趋势会随着 AI 提升而加强。

## X / 建造者动态

### OpenAI CEO Sam Altman
- 宣布 GPT-5.5 和 GPT-5.5 Pro 已在 API 可用，这是本周最重要的产品更新。（[链接](https://x.com/sama/status/2047787124846653895)）
- 发推总结"这是很棒的一周，为团队感到骄傲。祝大家愉快构建！"语气轻松自信。（[链接](https://x.com/sama/status/2047823357635354814)）

### Box CEO Aaron Levie
- 长篇论述 AI 杰文斯悖论：AI 越好、企业越需要人。这一观点与主流"AI 替代人力"叙事形成鲜明对冲。他举了多个例子——小企业从雇不起工程师到 AI 让工程师产出倍增而值得雇用；销售团队因 AI 自动化获客反而需要更多销售人员跟进。结论：越好的 AI 越不能替代人，而是催生更多人力需求。（[链接](https://x.com/levie/status/2047747142308274645)）

### Cursor 设计师 Ryo Lu
- 宣布全面切换到 GPT-5.5 + Composer 2，称其为"智能、速度、成本的完美组合，只在 Cursor"。这是 Cursor 团队对 GPT-5.5 的官方推荐信号。（[链接](https://x.com/ryolu_/status/2047879353313431649)）
- 介绍 Cursor 新功能 `/multitask`，可突破排队限制同时处理多个任务。（[链接](https://x.com/ryolu_/status/2047766831105220799)）

### OpenClaw 创始人 Peter Steinberger
- 评价 GPT-5.5 在角色扮演/人物塑造方面"明显上了一个台阶"。（[链接](https://x.com/steipete/status/2047871519762567468)）
- 发布 discrawl 0.6.0，新功能：可读取 Discord DM，无需自定义登录技巧，避免账号被封。（[链接](https://x.com/steipete/status/2047797210427859450)）

### Linear 产品负责人 Nan Yu
- 发表设计哲学短论："核心设计关乎理解，而非输出。设计是意图，不是图像或原型。没有意图的输出就是幻觉。"——在 AI 自动生成 UI 的时代，这一判断精准点出了设计师角色的核心价值。（[链接](https://x.com/thenanyu/status/2047751915271020920)）
- 在另一条推文中指出：Pre-AI 时代 Behance 和 Dribbble 上的天气 App 和仪表盘设计稿，本质上是"幻觉"。（[链接](https://x.com/thenanyu/status/2047758400948408831)）

### Replit CEO Amjad Masad
- 宣布 Replit 现在可一键导入 Vercel 或 Lovable 应用。这是 AI 开发工具平台间互操作性的重要动作。（[链接](https://x.com/amasad/status/2047747978690232550)）

### Google Labs VP Josh Woodward
- NotebookLM 新增自动标签与来源分类功能，继续深耕知识管理场景。（[链接](https://x.com/joshwoodward/status/2047795981534847413)）

### Every CEO Dan Shipper
- 金句："任何 AI 知道的比任何个人多，但任何个人学得比任何 AI 快。"（[链接](https://x.com/danshipper/status/2047797874600161334)）
- 用 NotebookLM 一键将正在读的书生成了音频对话，评价"holy fuckin shit"——AI 内容消费体验正在质变。（[链接](https://x.com/danshipper/status/2047674383469093079)）

### South Park Commons GP Aditya Agarwal
- 提出"我们正在进入后提示词时代（post-prompting world）"。这一判断与 Agent 自主性提升的趋势一致。（[链接](https://x.com/adityaag/status/2047669585667666321)）

### FirstMark VC Matt Turck
- 评论 Cohere 与 Aleph Alpha 合并：在美国之外，对将智能外包给少数美国平台存在巨大顾虑，尤其是在当前地缘政治动荡下。非美 AI 主权叙事持续升温。（[链接](https://x.com/mattturck/status/2047721904438493482)）

### FPV Ventures Partner Nikunj Kothari
- 分享新关注的优质账号列表（[链接](https://x.com/nikunj/status/2047861559075250687)）
- 幽默吐槽 PM 把 vibe-coded 设计直接推到生产的场景（[链接](https://x.com/nikunj/status/2047790294184374565)）
- 提醒产品团队：项目代号不是临时的，是永久的——选名字要极其慎重（[链接](https://x.com/nikunj/status/2047707257073524897)）

### Roblox Product Peter Yang
- 用 GPT-5.5 + Codex 在 15 分钟内生成 Star Fox 游戏，视频展示效果出色；AI 甚至能自己试玩游戏——说明模型在结构化代码生成和多模态交互方面又有提升。（[链接](https://x.com/petergyang/status/2047882568520102226)）

### Swyx
- 转发 JSConf EU 上 Vercel CTO 演讲，指出 Vercel 的 AI 工程工作直接来自 C-suite，这种情况应该更普遍但即使今天也很少见。（[链接](https://x.com/swyx/status/2047749587163877668)）
- "今天的热门技能会成为明天的后训练目标"——关于 AI 技能生命周期的一个精准观察。（[链接](https://x.com/swyx/status/2047715417867907539)）

> 以下建造者本轮无实质性内容更新：Garry Tan（SF 地方政治）

## 官方博客

### Anthropic Engineering — Scaling Managed Agents: Decoupling the brain from the hands
[原文链接](https://www.anthropic.com/engineering/managed-agents)

这篇是 Anthropic 工程团队迄今对 Agent 架构最系统的公开阐述。核心理念来自操作系统设计——用稳定的 interface 虚拟化实现细节。Managed Agents 将 Agent 拆分为三个独立接口：session（事件的仅追加日志）、harness（调用 Claude 并将工具调用路由到基础设施的循环）、sandbox（Claude 执行代码和编辑文件的环境）。

关键设计决策：
- **解耦大脑与双手**：harness 不再与 sandbox 在同一容器中。sandbox 成为可被替换的"牛"，harness 自身也是无状态的"牛"——崩溃后可重启恢复。
- **安全边界重构**：Claude 生成的代码运行在沙箱中，与凭证完全隔离。凭证要么在资源初始化时注入（如 Git token 在 clone 时使用），要么通过 MCP proxy + vault 方式在沙箱外管理。harness 永远接触不到凭证。
- **会话 ≠ 上下文窗口**：session 作为持久化的上下文对象存储在 Claude 上下文窗口之外，harness 可通过 `getEvents()` 选择性地取回事件切片，支持灵活的上下文工程。
- **性能收益**：解耦后 P50 TTFT 下降约 60%，P95 下降超 90%。原因是 session 如果不需要 sandbox 就不必等待容器启动。

原文引用："The abstractions outlasted the hardware. The read() command is agnostic as to whether it's accessing a disk pack from the 1970s or a modern SSD. The abstractions on top stayed stable while the implementations underneath changed freely. Managed Agents follow the same pattern."

## 播客

### No Priors — SAP: Bringing the 'Operating System' of a Company into the AI Era with CTO Philipp Herzig
[视频链接](https://www.youtube.com/watch?v=5u7AjPardvo)

**一句话要点：** 企业 AI 的真正挑战不是模型能力，而是"在规模上教 AI 做正确的事"——SAP CTO 用 20,000 个 API、400,000 家客户、90+ 国家运营的实战经验，给出了企业 AI 落地最诚实的判断。

Philipp Herzig 是 SAP 的 CTO，管理这家拥有 40 万家客户的企业软件巨头。他将 SAP 定义为"一家公司的操作系统"——从订单到收款、从采购到付款，覆盖财务、HR、供应链、制造、销售等全链条。

**LLMs 的局限与 RPT：** Herzig 明确表示 LLMs 不适用于企业预测场景。"如果你需要预测需求、现金流、付款延迟——LLMs 不是为此设计的。它们是一个个 token 生成，而预测需要回归和分类。"SAP 用两年研究发布了 RPT（Relational Pretrained Transformers，关系预训练 Transformer），基于 Transformer 架构但结构完全不同，旨在用少量数据做高准确率的表格数据预测。"我们相信这会很重要——它让更多人能做预测，而 LLMs 对此非常吃力。"

**企业 AI 的三层变革：**
1. UI 层：从让人点击的界面变为生成式 UI——系统针对具体分析动态生成界面，可实现"深夜运行、早上告诉你供应链出了什么问题并给出建议"。
2. 业务流程层：从 SaaS 到 Service as a Software——Agent 融合结构化与非结构化世界，将过去僵化的标准操作流程变得灵活。
3. 数据层：构建统一语义化的数据模型，将 SAP 内部数据（总账、发票、库存）与外部数据融合，因为"AI 有多强取决于数据有多好"。

**规模是最大的工程挑战：** "两年前任何人都能用 RAG 在 10 份文档上建聊天机器人让 CEO 惊艳。但 SAP 客户有数百万份文档。"同样的道理适用于 MCP——"去年人人都能建 MCP 服务器，10 个 API 没问题。100 个 API 开始有上下文膨胀。我们有两万个 API——问题就变成了如何端到端地为客户做这件事。"

**Agent 挖掘与数据飞轮：** Herzig 提出了"Agent Mining"概念——记录用户在 Agent 交互中的所有决策轨迹，形成数据飞轮。如果发现某国团队的操作是异常——推标准化；如果是好的创新——提升为全球标准操作流程。

**风险提醒：** 他特别提到 LightLLM 的漏洞事件（两周前），该漏洞可窃取所有密钥和凭证。"如果你是 CISO，你不会把 GitHub 上的开源项目直接部署到企业里。安全是企业 AI 采用的一大瓶颈。"

**定价模式转型：** SAP 正在从按席位（seat-based）许可向按消费（consumptive）许可过渡，最终目标是基于结果的定价模型（outcome-based）。但客户尚未准备好——他们需要可预测性，且对完全消费模式下的成本爆炸心存顾虑。

> "我犯过的最大的错误是向 CFO 推销技术。正确的做法是：先问'你业务上最关心什么'，然后倒推到技术。"

**量子计算：** Herzig 个人兴趣点——SAP 在量子计算领域已有早期研究，聚焦优化问题（旅行商问题、背包问题等），虽然硬件尚不成熟，但 SAP 希望先找到新算法。"如果能让卡车装载和路线规划更优，排放下降，成本大幅降低。"

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
