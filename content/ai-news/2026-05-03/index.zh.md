---
title: "张咋了AI资讯 2026-05-03"
date: 2026-05-03
tags: [AI资讯]
cover: gradient-4
summary: "**Anthropic 公开 Claude Code 质量事故复盘**：三月起用户反馈 Claude Code 变笨，Anthropic 追溯到三次独立变更——推理强度默认从 high 降到 medium、会话缓存 bug 导致推理记录被持…"
---

## 今日3点

1. **Anthropic 公开 Claude Code 质量事故复盘**：三月起用户反馈 Claude Code 变笨，Anthropic 追溯到三次独立变更——推理强度默认从 high 降到 medium、会话缓存 bug 导致推理记录被持续清除、系统提示词限制 verbosity 导致编码质量下降。三个问题已于 4 月 20 日全部修复，所有用户用量限额已重置。
2. **Codex /goal 功能引爆开发者体验**：OpenAI Codex 的 /goal 功能获得超 2000 赞，被多位建造者称为"太香了"，开发者社区反馈强烈。
3. **Baseten CEO 预告年营收将破 10 亿美元**：AI 推理基础设施公司 Baseten 过去一年增长 30 倍，CEO Tuhin Srivastava 表示今年营收预期超过 10 亿美元，95% 的 token 都跑在客户定制模型上，GPU 供给紧张"比大家想象的还要严重"。

## X / 建造者动态

**Peter Steinberger**（OpenClaw / OpenAI）对 Codex /goal 功能大加赞赏，称"slaps"，获 2020 赞、110 回复，是当日最高互动推文。他还分享了 Codex 的新玩法和与 xAI 互动的趣事。[推文链接](https://x.com/steipete/status/2050275598178586921)

**Aaron Levie**（Box CEO）从 Atlassian 财报出发分析 Agent 时代的软件逻辑：当 Agent 数量是人类的 100 倍时，底层系统（安全、合规、工作流、数据存储）的需求只会更大。他还指出硅谷之外的企业 AI 应用核心是"加速现有工作"而非裁员，AI 削减的成本很快会被竞争压力重新投入增长。[推文链接](https://x.com/levie/status/2050295657836277764) [推文链接](https://x.com/levie/status/2050240083325030404)

**Zara Zhang** 提出一个有趣视角：很多人把编程 Agent 当员工使唤，但她把 Agent 当联合创始人——不是下命令，而是描述问题、说明现状、征求建议。[推文链接](https://x.com/zarazhangrui/status/2050326543797469415)

**Sam Altman** 重返 Twitter，发了三条推文，其中 "/hatch clippy" 暗示 OpenAI 可能推出新的 AI 助手形象，获 1115 赞和 352 回复。[推文链接](https://x.com/sama/status/2050402088266694689)

**Claude** 官方宣布 Code with Claude 开发者大会下周回归，涵盖 Claude Code 入门到进阶内容。[推文链接](https://x.com/claudeai/status/2050252933866930339)

**Peter Yang**（Roblox 产品经理）分享了对 Codex 的深度使用体验，发现第一个 bug，同时自嘲花 3000 美元买了 MacBook Pro "跑本地模型"实际上主要在跑 Codex。[推文链接](https://x.com/petergyang/status/2050406287008268450)

**Nikunj Kothari**（FPV Ventures 合伙人）展示了用 Railway + Claude 构建的房屋报告工具，每份报告成本 8-9 美元，目前 ARR 已达 36,500 美元。[推文链接](https://x.com/nikunj/status/2050353986742698400)

**Amjad Masad**（Replit CEO）庆祝 Replit 成立 10 周年，宣布全天免费 24 小时。[推文链接](https://x.com/amasad/status/2050479551537619413)

**Dan Shipper**（Every CEO）提出一个值得玩味的判断：模型比任何单个人类知道得更多，但任何单个人类比模型学得更快。[推文链接](https://x.com/danshipper/status/2050304359024759242)

**Aditya Agarwal**（South Park Commons 合伙人）一句话警告：杀死公司最好的方式就是把注意力放在产品以外的一切。[推文链接](https://x.com/adityaag/status/2050229509840900434)

**Swyx** 提出一个 Chrome 扩展需求：在所有网页图片输入框上叠加文字生成、手绘和 AI 生成功能，并喊话 Devin 来做。[推文链接](https://x.com/swyx/status/2050460622706626740)

**Garry Tan**（YC CEO）针对加州资产没收提案发出警告，认为这会逼走富人、摧毁税基。[推文链接](https://x.com/garrytan/status/2050365216421241152)

## 官方博客

### Anthropic Engineering

**An update on recent Claude Code quality reports**

Anthropic 公开了 Claude Code 质量下降的完整事后复盘。三月起用户反馈 Claude Code "变笨"，调查后发现是三次独立变更的叠加效应：

1. **3 月 4 日**：将默认推理强度从 high 改为 medium（为减少延迟），4 月 7 日回滚。影响 Sonnet 4.6 和 Opus 4.6。
2. **3 月 26 日**：缓存优化 bug 导致闲置会话的推理记录在后续每轮对话中都被清除，Claude 表现出"健忘"和重复行为。4 月 10 日修复。影响 Sonnet 4.6 和 Opus 4.6。
3. **4 月 16 日**：系统提示词中添加"限制 verbosity"指令（tool 间文本 ≤25 词，最终回复 ≤100 词），在与其它提示词变更叠加后导致编码质量下降 3%。4 月 20 日回滚。影响 Sonnet 4.6、Opus 4.6 和 Opus 4.7。

Anthropic 表示将采取多项措施防止类似问题：增加内部员工使用公开版本的比例、扩大评估套件、对系统提示词变更增加 ablation 测试和渐进发布流程。所有订阅用户用量限额已重置。

[原文链接](https://www.anthropic.com/engineering/april-23-postmortem)

### Claude Blog

**New connectors in Claude for everyday life**

Claude 新增 16 个生活类连接器，包括 AllTrails、Instacart、Audible、Tripadvisor、Uber、Spotify 等。Claude 会在对话中自动推荐相关连接器，用户可以在一个对话中串联多个应用完成任务。Claude 无广告、无付费植入，连接器目录已超 200 个。

[原文链接](https://claude.com/blog/connectors-for-everyday-life)

**Built-in memory for Claude Managed Agents**

Claude Managed Agents 推出内置记忆功能（公测版）。记忆以文件形式存储，支持导出、API 管理、审计日志和版本回滚。多个 agent 可并发访问同一记忆存储而不互相覆盖。Netflix 用它让 agent 跨会话保持上下文；Rakuten 的长时任务 agent 通过记忆将首轮错误率降低 97%；Wisedocs 的文档验证流程加速 30%。

[原文链接](https://claude.com/blog/claude-managed-agents-memory)

## 播客

### No Priors — Baseten CEO Tuhin Srivastava on the AI Inference Crunch, Custom Models, and Building the Inference Cloud

Baseten CEO Tuhin Srivastava 在 No Priors 上分享了 AI 推理市场的深度观察。核心观点：

**推理是"最后的市场"**：即使实现 AGI，剩下的也全是推理。Baseten 过去一年增长 30 倍，今年营收预期超 10 亿美元。公司分布在 18 个云服务商、90 个集群上，日常利用率维持在 90% 以上。

**95% 是定制模型**：几乎没有客户在跑"原版"开源模型，都在做质量或性能层面的定制化。Post-training 和推理是同一枚硬币的两面——推理产生数据，数据驱动 post-training，post-training 又优化推理。

**应用层会存在**：应用层的护城河在于"只有你能拿到的用户信号"。以 Abridge（医疗 AI 记录）为例，临床医生的编辑和后续操作构成的工作流是前沿模型公司无法触及的。

**GPU 供给比想象的更紧张**："市场上有很多不靠谱的供应商"，真正靠谱的云服务商大约十几家，顶级的只有 3-4 家。GPU 合同期限拉长到 3-5 年，需要 20-30% 预付。

**中国开源模型的观点**：这些模型非常优秀，网络隔离足以防止数据外流。美国也需要有自己的开源模型，这既是必要的也是必然的。DeepSeek 级别的模型能以 Anthropic/OpenAI 20% 的成本跑出相当甚至更好的延迟和可靠性。

[视频链接](https://www.youtube.com/watch?v=XAbKflCncDo)

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
