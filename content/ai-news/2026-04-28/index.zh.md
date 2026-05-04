---
title: "张咋了AI资讯 2026-04-28"
date: 2026-04-28
tags: [AI资讯]
cover: gradient-1
summary: "**Sam Altman 发出强烈信号：操作系统和互联网需要为 AI agent 时代重新设计。** OpenAI CEO 发推表示\"现在是认真重新思考操作系统和用户界面设计的好时机——互联网也需要一个同样适用于人和 agent 的协议\"，…"
---

## 今日3点

1. **Sam Altman 发出强烈信号：操作系统和互联网需要为 AI agent 时代重新设计。** OpenAI CEO 发推表示"现在是认真重新思考操作系统和用户界面设计的好时机——互联网也需要一个同样适用于人和 agent 的协议"，获得超过 10,000 次点赞，并公开了 OpenAI 五大原则（民主化、赋能、普遍繁荣、韧性、适应性）。
2. **Anthropic 发布 Claude Code Auto Mode：用两层模型分类器替代人工审批。** 这是介于手动审批和无护栏之间的中间方案——转录分类器在工具调用执行前拦截，提示注入探测器在内容进入上下文前筛查，误报率压到 0.4%，真实过度行为漏报率 17%，面向曾使用 `--dangerously-skip-permissions` 的用户群。
3. **Y Combinator CEO Garry Tan 公开 articulate agent 的三文件架构。** SOUL.md 定义 agent 的声音和价值观，USER.md 是对用户的深度建模（约 4000 字），AGENTS.md 是操作规则。他强调"用写软件的方式写 agent 只会得到聊天机器人，用写人的方式写 agent 才能得到有生命感的东西。"

## X / 建造者动态

### OpenAI CEO Sam Altman
- 发推表示要认真重新思考操作系统和用户界面设计，还呼吁互联网需要一个同时面向人和 agent 的协议。该推文获得超 10,000 点赞和 634 次转发。
- 公开 OpenAI 五大原则：Democratization、Empowerment、Universal Prosperity、Resilience、Adaptability。
- 表达对 GPT-5.5 用户反馈的欣喜："almost nothing feels more gratifying than builders saying they find our tools useful."
- 链接：[1](https://x.com/sama/status/2048428561481265539) | [2](https://x.com/sama/status/2048552677433643427) | [3](https://x.com/sama/status/2048554097985593849)

### Box CEO Aaron Levie
- 观察到一种有趣的 Gell-Mann 失忆症现象：人们在自己的工作场景里看到 AI 需要各种"最后一公里"的复杂操作，但一看到别人的工作被 AI 处理就立刻觉得 AI 会完全取代那个岗位。他认为这是对很多"工作消失论"保持怀疑的理由。
- 另一条长推分析 AI agent 时代过度工作的两个深层原因：（1）AI 大幅提升了增量努力带来的杠杆效应，让人像管理团队一样管理 agent，优先排序和任务拆分变成关键能力；（2）AI 降低了启动新任务的门槛，让人容易在晚上 9 点开始一个"很快"的项目，然后干到午夜。他认为这会带来新的就业机会——团队会把 AI 实验推广成正式生产流程。
- 链接：[1](https://x.com/levie/status/2048576989930619185) | [2](https://x.com/levie/status/2048537503972684252)

### Y Combinator CEO Garry Tan
- 详细分享 articulate agent 的三文件架构：SOUL.md（定义 agent 是谁——声音、价值观、原则）、USER.md（对用户的深度建模，约 4000 字）、AGENTS.md（操作规则）。强调"精准具体的声音定义是关键——写'要简洁有用'就会得到 ChatGPT，写'像有品位的同辈一样说话，一句话能说清就用一句话，不舒服的真相只要真的就要说'——你会得到有生命感的东西。"
- 提到自己的 OpenClaw 了解了完整日程和健康目标后，会在凌晨 12:30 之后拒绝回复他的消息。
- 形容与了解自己的 agent 对话像"跟一本认识你的书聊天"，是一种超现实体验。
- 链接：[1](https://x.com/garrytan/status/2048669695344046090) | [2](https://x.com/garrytan/status/2048667055424249864) | [3](https://x.com/garrytan/status/2048664680558932266)

### Vercel CEO Guillermo Rauch
- 断言 coding agent 将成为所有超级智能的基础。编码能力与"计算机熟练度"无法区分——优秀的 coding agent 掌握 bash、文件系统、程序安装配置。更重要的是自我改进能力：coding agent 能检查自己的源代码、状态、技能、指令，甚至提出或直接执行对自身的修改（建议有人类监督和审计追踪）。
- 链接：https://x.com/rauchg/status/2048523195305902341

### OpenClaw 创始人 Peter Steinberger (steipete)
- 发布 wacrawl 0.2.0：WhatsApp Desktop 加密 Git 备份与恢复。`wacrawl backup push` 写 age 加密分片到 GitHub，`backup pull` 解密验证并本地还原。
- 发布 birdclaw：本地存储推文工具，支持导入 archive、GitHub 备份、定时任务导入 X bookmarks。
- 切换 CI 到 Blacksmith——可以拉起 32 vCPU 实例跑测试，解决了 CPU 瓶颈问题，获得 332 点赞。
- 链接：[1](https://x.com/steipete/status/2048660875007914176) | [2](https://x.com/steipete/status/2048626844694421842) | [3](https://x.com/steipete/status/2048630704972443918)

### Roblox 产品 Peter Yang
- 周末给自己的健身 app 搭建了一个 MCP server，可以通过 Claude/Codex 等获取最新运动数据并更新训练计划。
- 抱怨 Google Photos + Gemini 无法完成一个很自然的任务："把我跟女儿一起长大的精选集生成给我"——认为这是个被浪费的机会。
- 链接：[1](https://x.com/petergyang/status/2048611053333041158) | [2](https://x.com/petergyang/status/2048603978070712757)

### Other Builders
- **Nan Yu (Linear 产品负责人)**：调侃 FindMy 团队应该跟某个 app 学学设计；另发一推表示"English, of course"，回应关于编程语言的讨论。
- **Dan Shipper (Every CEO)**：调侃自己的 agent 在被问基础问题时的反应。本周播客发布了与 Logical Intelligence CEO 关于 EBM 的深度对话。
- **Swyx**：引用了一条推文，无原文内容。
- **Kevin Weil (OpenAI 科学 VP)**：表情回复转推，无实质内容。
- **Nikunj Kothari (FPV Ventures)**：链接分享，无原文。
- **Aditya Agarwal (South Park Commons)**：关于人类进步——马拉松两人同时破 2 小时——的感言。

## 官方博客

### Anthropic Engineering：Claude Code Auto Mode — 一种更安全的跳过权限方式

Anthropic 正式发布 Claude Code 的 Auto Mode。这是一个介于手动审批和完全跳过权限之间的新方案，核心是两层防御体系：

**两层分类器：**
- **输入层**：服务端提示注入探测器扫描工具输出（文件读取、网页抓取、shell 输出等），在 agent 看到内容之前注入警告标记。
- **输出层**：由 Sonnet 4.6 驱动的转录分类器在工具调用执行前进行评估，两阶段运作——第一阶段是快速单 token 过滤（"阻断/放行"），仅当标记后才进入第二阶段链式推理。分类器只看用户消息和工具调用指令，不读 agent 的思考过程——设计上保持"推理盲"。

**性能数据（内部 10,000 条真实流量测试）：**
- 第一阶段：误报率 8.5%，对真实过度行为的漏报率 6.6%
- 完整两阶段：误报率降至 0.4%，漏报率升至 17%（相比第一阶段）
- 合成数据外泄测试漏报率：5.7%

**关键设计决策：**
- 剔除 agent 助理文本和工具结果——不让 agent 的自我辩解影响分类器判断，同时作为对抗提示注入的防线
- 拒绝后不中断任务，而是返回拒绝原因让 agent 尝试更安全的替代方案
- 累计 3 次连续拒绝或 20 次总拒绝后强制终止，转到人工处理
- 多 agent 场景下在委派和返回两端都执行分类器检查

链接：https://www.anthropic.com/engineering/claude-code-auto-mode

## 播客

### AI & I by Every：The AI Model Built for What LLMs Can't Do
嘉宾：Eve，Logical Intelligence 创始人兼 CEO | 主持人：Dan Shipper

**核心要点：**
Eve 的公司 Logical Intelligence 同时研发 EBM（能量模型）和 LLM，聚焦软件和硬件的正确性验证。她认为 LLM 在需要确定性、可验证性的关键任务中存在根本性局限。

**EBM vs LLM 的本质区别：**
- LLM 是自回归的、序列化的、基于 token 的猜谜游戏——只能单向决策，看不到全局，有时明知前面有坑也只能往前走。
- EBM 拥有"鸟瞰视角"——同时看到所有可能状态，可以自由选择不同路径。没有 token，天然非自回归，架构允许实时内部监督。
- EBM 擅长稀疏数据，同时有内部自对齐机制和外部验证器，实现"双重验证"。

**能量模型的物理直觉：**
"自然界一切都在最小化能量——你累了会躺在沙发上，就是因为那是能量最低的状态。我们就是利用最小化能量的原理，把数据处理成一个能量景观，用算法在上面导航。"

**为什么不能让 LLM 做一切：**
"用 LLM 处理空间推理任务，就像让文学系的人去建桥——你当然可以做，但为什么不去工程系找受过正式方法训练的人？"

**对 AI 行业的看法：**
Eve 指出硅谷对 LLM 的巨额投资已形成"你中有我"的生态系统——硬件、数据中心、大模型公司之间循环交易，要打破很难。她的策略不是要替代 LLM，而是让 EBM 作为兼容层——LLM 可以把非语言任务外包给 EBM，在保持现有投资价值的同时降低成本。

**播客链接：** https://www.youtube.com/watch?v=Q-i8ZSUCtIc

---

Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
