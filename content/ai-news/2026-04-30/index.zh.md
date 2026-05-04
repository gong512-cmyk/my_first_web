---
title: "张咋了AI资讯 2026-04-30"
date: 2026-04-30
tags: [AI资讯]
cover: gradient-3
summary: "**Claude 连接创意工具全家桶**：Blender、Autodesk Fusion、Adobe Creative Cloud、Ableton、Splice、Canva、SketchUp 等全部上线连接器，Claude 可直接操作这些专…"
---

## 今日3点

1. **Claude 连接创意工具全家桶**：Blender、Autodesk Fusion、Adobe Creative Cloud、Ableton、Splice、Canva、SketchUp 等全部上线连接器，Claude 可直接操作这些专业软件。
2. **Steinberger 用 Codex 搭建自愈代码流水线**：每次合并自动触发 Codex 审查，发现缺陷再启动修复 Codex，最多循环 5 轮，上线 10 分钟就抓到一个 bug。
3. **Aaron Levie 断言：软件不会消失，而是要膨胀 100 倍**：Agent 是技术人有史以来最大的杠杆，世界将迎来 100 倍以上的软件需求。

## X / 建造者动态

### Claude (Anthropic)
Anthropic 今天密集发布创意工具连接器：Blender 连接器可在对话中调试场景、构建工具、批量修改对象；Autodesk Fusion 连接器支持对话式 3D 建模；同时上线 Adobe Creative Cloud、Ableton、Splice、Canva、Affinity、SketchUp、Resolume 等连接器，并加入 Blender 开发基金。这是 Claude 向专业创意工作流全面渗透的信号。
- [Blender 连接器](https://x.com/claudeai/status/2049143438281445811) (34K+ 赞)
- [Fusion 连接器](https://x.com/claudeai/status/2049143440508616863)
- [更多连接器](https://x.com/claudeai/status/2049143442601546054)

### Peter Steinberger (OpenClaw)
Steinberger 在 main 分支上用 Codex 搭建了自动审查-修复循环：每次提交落地后 Codex 自动审查，发现回归或安全问题就再启动一个 Codex 实例修复，然后由审查 Agent 检查修复质量，最多循环 5 次。系统上线 10 分钟就抓到了他自己的一个缺陷。
- [自愈流水线](https://x.com/steipete/status/2049356949523730699)
- [10 分钟抓到 bug](https://x.com/steipete/status/2049290741013262522)
- [I smell a leak](https://x.com/steipete/status/2049290265026773172) (3.5K 赞)

### Aaron Levie (Box CEO)
Levie 连发两条长帖论述 Agent 时代与软件工作的关系：软件岗位不会消失，Agent 是技术人有史以来最大的个人杠杆；世界不会因为 Agent 减少软件需求，而是将迎来 100 倍以上的软件量——从遗留系统迁移、SMB 开发、安全补丁到流程自动化，全都需要 Agent 去做，每个 Agent 都需要一个懂技术的人来启动、管理和编排。
- [Agent 是最大杠杆](https://x.com/levie/status/2049333853777764495)
- [100 倍软件](https://x.com/levie/status/2049163935182733396)

### Sam Altman (OpenAI)
Altman 连续发布链接引发大量互动（单条最高 9K+ 赞），并预告"enjoy the next few updates"，暗示 OpenAI 即将有密集发布。提到 ajambrosino 正在"mogmogging"。
- [预告更新](https://x.com/sama/status/2049315574120055054)
- [链接](https://x.com/sama/status/2049241518540808440) (9K+ 赞)

### Guillermo Rauch (Vercel CEO)
Rauch 宣布扩大 Vercel Labs 团队，使命是"构建 AI 时代的开发者工具"——从为人构建工具转向为 Agent 构建工具。团队已发布 agent-browser、portless、skills、chat、just-bash、json-render 等项目，累计下载量超 2280 万次。
- [Vercel Labs 招聘](https://x.com/rauchg/status/2049216048831025232)

### Amjad Masad (Replit CEO)
Masad 指出 GitHub 面临 bot 流量冲击，免费服务模式将难以为继；建议探索微支付方案（每次 git push 几美分），可用 Bitcoin 实现无需 KYC 的开放支付。此外他还在准备支持一位"教育界 GOAT"重新发明教育。
- [GitHub 微支付](https://x.com/amasad/status/2049242460078100638)
- [支持教育创新](https://x.com/amasad/status/2049245424624820412) (3.5K 赞)

### Dan Shipper (Every CEO)
Shipper 在 Codex 内部直接使用 PostHog 浏览数据、写查询、触发 Agent 写 PR，提出"Codex-native"概念：未来会有专门为 Agent 内置浏览器设计的应用——Agent 和人类共享上下文、同时操作。这是巨大的新软件品类。
- [PostHog + Codex](https://x.com/danshipper/status/2049236793761976357)
- [Codex-native 概念](https://x.com/danshipper/status/2049223943735726150)

### Thariq (Claude Code, Anthropic)
Claude Code 团队正在集中修复最恼人的 bug，正在打磨无闪烁渲染器以作为默认渲染器上线。他公开征集社区的"白鲸 bug"（长期未解决的痛点），单条获得 1000+ 赞和 341 条回复。
- [征集白鲸 bug](https://x.com/trq212/status/2049234228290961690) (1K+ 赞)
- [无闪烁渲染器](https://x.com/trq212/status/2049234229926695188)

### Zara Zhang (Builder)
Zara 建议让 AI 生成 SVG 而非图片——矢量插图可以无缝融入设计风格，配合 HTML 幻灯片效果极佳。她还分享了一种新工作流：不再用 GUI 构建 Web 应用，而是分享 GitHub 仓库让对方 Agent 按需定制 UI。
- [SVG > 图片](https://x.com/zarazhangrui/status/2049258231042805806)
- [代码仓库即产品](https://x.com/zarazhangrui/status/2049186121314415054)

### Peter Yang (Roblox)
Yang 认为独立 AI 构建者正迎来黄金时代，"世界就是他们的游乐场"。他还转发了 Shpigford 的个人 Agent 配置思路，准备移植到自己的 OpenClaw 中。
- [独立构建者时代](https://x.com/petergyang/status/2049345724559847585)

### Garry Tan (YC CEO)
Tan 提醒：如果你已经厌倦了"Agent"这个词，2026 年会是你的"永恒九月"——Agent 讨论只会更多不会更少。他还纪念了 AlphaGo 十周年。
- [Agent 永恒九月](https://x.com/garrytan/status/2049351894007710031)

### Nan Yu (Linear)
Linear 产品负责人感叹"拥有过剩算力的奢侈"。
- [算力奢侈](https://x.com/thenanyu/status/2049075513444999515)

### Aditya Agarwal (South Park Commons)
前 Dropbox CTO 对某项目发出高度赞赏，认为"awesome 到无法形容"。
- [赞叹](https://x.com/adityaag/status/2049259492727234748)

## 官方博客

无新博客内容。

## 播客

无新播客内容。

---
Generated through the Follow Builders skill: https://github.com/zarazhangrui/follow-builders
