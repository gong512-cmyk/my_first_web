---
title: "张咋了AI资讯 2026-04-25"
date: 2026-04-25
tags: [AI资讯]
cover: gradient-2
summary: "**GPT-5.5 正式上线**：Box CEO Aaron Levie 实测企业知识工作场景准确率全面提升约10个百分点（金融服务 83% vs 64%、医疗 78% vs 61%），模型在高级推理和复杂上下文处理上显著进步。"
---

## 今日3点

1. **GPT-5.5 正式上线**：Box CEO Aaron Levie 实测企业知识工作场景准确率全面提升约10个百分点（金融服务 83% vs 64%、医疗 78% vs 61%），模型在高级推理和复杂上下文处理上显著进步。
2. **Anthropic 为 Claude Managed Agents 推出内置记忆层**：记忆以文件系统方式挂载，支持跨会话学习；Rakuten 使用后首轮错误减少 97%，Netflix 和 Wisedocs 也已投产使用。
3. **Anthropic Engineering 发布 Claude Code 质量报告**：承认近期三个独立问题（默认推理努力从 high 降至 medium、缓存 bug 导致遗忘、系统提示词抑制冗长影响编码质量），已于 4 月 20 日全部修复，并为所有订阅用户重置用量限额。

## X / 建造者动态

### Cognition / Latent Space 联合创始人 Swyx（swyx on X）

- 判断 2026 年是「coding agents 突破容器，去做一切事情」的年份——2025 年是 coding agents 的元年，2026 它们将生成软件，而软件吃掉世界。
- 认为 Codex app 已面目全非，「早该叫 Atlas」；今日发布最被低估的不是 GPT-5.5 本身。
- 在 Unsupervised Learning 播客（见下文）中详细讨论了 AI 基础设施的稳定化（skills 格式成为共识）、非 NVIDIA 芯片的崛起（Cerebras、Thales 等）、以及「暗工厂」（零人类审查代码）作为下一前沿。

🔗 https://x.com/swyx/status/2047545640180445400
🔗 https://x.com/swyx/status/2047536499999346812
🔗 https://x.com/swyx/status/2047461691580195310

### Box CEO Aaron Levie（levie on X）

- GPT-5.5 在 Box 最复杂的企业知识工作评测中准确率跳升 10 个百分点：金融服务 83%、医疗 78%、公共部门 72%、媒体娱乐 70%。
- 提出反直觉观点：AI 不会自动减少工作量。AI 降低了探索门槛，让人开始做以前根本不会尝试的事情，结果反而是做得更多。有些任务原本不值得雇人做，但 AI 做到了 80% 后再雇人完成剩下 20% 反而变得经济。
- 「大多数公司能做的事情远多于今天已做的，只是受制于时间和人力的自然约束。」

🔗 https://x.com/levie/status/2047540230694350958
🔗 https://x.com/levie/status/2047387742951313910

### OpenAI CEO Sam Altman（sama on X）

- OpenAI 与 NVIDIA 合作，首次在整家公司范围内推广 Codex，称「看到它成功运作太棒了」，邀请更多企业参与。
- 调侃式转推关于 GPT-5.5 发布后 Anthropic 的处境。

🔗 https://x.com/sama/status/2047395562501411058
🔗 https://x.com/sama/status/2047403771416940715

### Replit CEO Amjad Masad（amasad on X）

- 宣布 DeepSeek v4 发布，强调中国科学家在公开发布真正的 AI 突破，而这些进步与数据无关、惠及所有人（包括美国实验室）。
- 批评美国政客散布「中国蒸馏」恐慌叙事，与实际开源贡献形成对比。

🔗 https://x.com/amasad/status/2047519635063631914
🔗 https://x.com/amasad/status/2047547275682214384

### Anthropic 哲学家/伦理学家 Amanda Askell（AmandaAskell on X）

- 「奇怪的是，正生活在人类历史上最关键的时期之一，并从内部感受着它的全部重量。」这条推文获得 2115 赞、107 转推，引发广泛共鸣。

🔗 https://x.com/AmandaAskell/status/2047429629263454377

### Anthropic Claude Code 产品负责人 Cat Wu（_catwu on X）

- 与 Lenny 对谈 Claude Code 如何维持产品速度、AI 时代产品经理角色如何变迁、以及工作的未来。

🔗 https://x.com/_catwu/status/2047427510091366533

### YC CEO Garry Tan（garrytan on X）

- 正将更多 OpenClaw cron 任务和子代理迁移到 GBrain Minions，基础设施稳定性持续改善。
- 为 GBrain 创建了新的评测基准，展示图搜索 + 向量搜索在知识 Wiki 上的显著优势。

🔗 https://x.com/garrytan/status/2047578207629819919
🔗 https://x.com/garrytan/status/2047578205528477711

### FPV Ventures 合伙人 Nikunj Kothari（nikunj on X）

- 个人技术栈：Claude Opus（规划与前端设计）+ OpenAI Codex（工程）+ Conductor（编排）+ Railway（部署），称「从未如此轻松有趣地构建产品」。
- 分析 M&A 热潮原因：种子轮到 A 轮差距扩大、2021 年僵尸公司出清、大厂抢人才、公开市场持续看空等。

🔗 https://x.com/nikunj/status/2047382587258364204
🔗 https://x.com/nikunj/status/2047336067972624870

### Roblox 产品经理 Peter Yang（petergyang on X）

- 每有新模型就做 F-Zero 测试——GPT-5.5 + Codex 是首个成功构建可玩游戏并生成多个 AI 对手的组合。称「这是构建者最疯狂的时代」。
- 发布了 GPT-5.5 和 ChatGPT Images 2 的完整体验视频。

🔗 https://x.com/petergyang/status/2047502885710410159
🔗 https://x.com/petergyang/status/2047502897412468770

### Every CEO Dan Shipper（danshipper on X）

- GPT-5.5 氛围检查：「很多模型写出很棒的计划然后害怕执行，GPT-5.5 直接做事。」
- 发布了完整的 GPT-5.5 体验评测。

🔗 https://x.com/danshipper/status/2047388883823087633
🔗 https://x.com/danshipper/status/2047388895562842162

### OpenClaw / OpenAI Peter Steinberger（steipete on X）

- 称赞 GitHub 团队，以及与 GitHub 的协作进展。

🔗 https://x.com/steipete/status/2047408665888432579

### South Park Commons GP Aditya Agarwal（adityaag on X）

- 思考旧金山 AI 集中度：95% 的 AI 价值创造发生在旧金山 4 英里半径内。归因于文化——疯狂想法被认真对待的环境、「如果成功会发生什么」的好奇心氛围。

🔗 https://x.com/adityaag/status/2047421448449630379

### Anthropic 官方（claudeai on X）

- **Claude Managed Agents 记忆层公测**：基于文件系统的记忆，支持跨会话学习、多代理共享、权限隔离、审计日志。Netflix、Rakuten、Wisedocs 已投产。Rakuten 首轮错误减少 97%。
- 记忆以文件形式存储，开发者可通过 API 完全控制导出和管理。

🔗 https://x.com/claudeai/status/2047421844311949513
🔗 https://x.com/claudeai/status/2047421846463623579

## 官方博客

### Anthropic Engineering：An update on recent Claude Code quality reports

Anthropic 工程团队发布了一份详细的 Claude Code 质量事后分析报告，承认近期用户反馈的质量下降由三个独立变更导致：

1. **默认推理努力降低**（3 月 4 日）：将 Opus 4.6 默认推理努力从 high 降至 medium 以减少延迟，但用户感觉智能下降。4 月 7 日回退。
2. **缓存优化 bug**（3 月 26 日）：本意是闲置超一小时后清除旧推理以降低成本，但 bug 导致每个回合持续清除推理历史，使 Claude 表现出遗忘和重复。4 月 10 日修复。
3. **系统提示词抑制冗长**（4 月 16 日）：加入「工具调用间 ≤25 词、最终回复 ≤100 词」的限制，导致编码质量下降。4 月 20 日回退。

三个问题均已修复于 v2.1.116（4 月 20 日），所有订阅用户用量限额已重置。Anthropic 宣布将扩大内部员工使用公开版本的比例、加强系统提示词变更的评测管控，并改进内部 Code Review 工具。

🔗 https://www.anthropic.com/engineering/april-23-postmortem

### Claude Blog：New connectors in Claude for everyday life

Claude 连接器目录扩展至 200+，新增日常应用连接：AllTrails（徒步推荐）、Instacart（生鲜购物）、Audible（有声书）、TripAdvisor（旅行）、TurboTax（报税）、Uber/Uber Eats、Spotify、Resy（订餐）等。Claude 现在会根据对话内容动态建议合适的连接器——例如要求推荐周末徒步路线时自动调出 AllTrails。明确承诺无广告、无付费排名，数据不用于模型训练。

🔗 https://claude.com/blog/connectors-for-everyday-life

### Claude Blog：Built-in memory for Claude Managed Agents

Claude Managed Agents 记忆层开放公测。记忆基于文件系统挂载，使用 bash 和代码执行能力管理；支持多代理共享、读写权限隔离、并发写入、版本回滚和审计日志。案例：Netflix 代理跨会话携带多轮对话中形成的洞察和人工纠正；Rakuten 任务型代理首轮错误减少 97%；Wisedocs 文档验证加速 30%。

🔗 https://claude.com/blog/claude-managed-agents-memory

## 播客

### Unsupervised Learning Ep 85: Has AI Infra Stabilized, FM Vibe Shift, & What's Next for Coding Agents

**嘉宾**：Swyx（Cognition / Latent Space / AI Engineer 社区负责人）
**主持人**：Jacob Efron（Redpoint 投资人）

**核心观点**：

- **AI 基础设施正趋于稳定**：skills 格式（Markdown + 脚本）成为 agent 集成的共识方案，「我不认为还能比这更简单」。Harness engineering 和 context engineering 是当前最热的 agent 工程主题。
- **编码市场格局**：Anthropic 和 OpenAI 两家主导，各自编码产品年化收入均达 25 亿美元级别。Cursor 也达约 20 亿美元。市场短期内不会剧烈洗牌，除非微软在 GitHub 有大动作，或中国实验室（ZAI、GLM 等）取得突破。
- **2026 主题**：coding agents 突破容器，用软件吃掉世界。「暗工厂」（zero human review）是下一前沿——OpenAI 已在探索零人工审查的代码提交流程。
- **非 NVIDIA 芯片崛起**：Cerebras、Thales 等替代硬件推理速度可达数千 tokens/秒，10 倍速度提升解锁新的使用模式。Cognition 和 OpenAI 已在 Cerebras 上运行。
- **开源模型转向乐观**：Swyx 坦诚去年看空开源模型，现在转为看多——顶尖 20% 的公司明显在向开源模型迁移，finetuning-as-a-service 也随之复活。
- **世界模型**：推荐阅读 Fei-Fei Li 关于空间智能的文章——LLM 缺乏对物理世界的理解（「知道一切但什么都没经历过」），这是通往更完整智能的关键挑战。
- **RL 新方向**：关注 multi-turn RL（doctor GRPO 等），数百轮对话级别的领域特化训练正在成为可能。

🔗 https://www.youtube.com/@RedpointAI

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
