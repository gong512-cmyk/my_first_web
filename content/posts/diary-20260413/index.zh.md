---
title: "日记 2026-04-13"
date: 2026-04-13
tags: [VPS, Hermes, Agent, 微信, hysteria2, AI订阅]
cover: gradient-4
summary: "基础设施搭建日：在腾讯 VPS 成功部署 Hermes Agent 并打通微信通信，加装 hysteria2，评估 AI 订阅方案。"
---

今天是动手能力拉满的一天，主题依然是基础设施，但比前两天更进一步——从「搭通道」升级到了「搭服务」。

在腾讯 VPS 上做了两件事。第一，安装 Hermes Agent 并调试成功，同时与微信的 IM 通信也调通了。这意味着 Agent 可以通过微信收发消息，把 AI 能力接入日常通讯工具里。第二，在这台 VPS 上加装了 hysteria2 服务器，用于远程科学上网，同样一次调通。

两套服务从零搭建到全部调试通过，效率让我自己都有点意外。这种「装一个、通一个」的节奏感，比反复折腾排查问题舒服太多了。

另外开始认真考虑 AI 模型订阅的长期方案。目前初步倾向于 opencode-go（10 刀/月）+ GitHub Copilot（39 刀/月）的组合。这个搭配的性价比极高——opencode-go 覆盖日常编码和 Agent 编排，Copilot 补全和 PR review 的体验也越来越成熟。加起来一个月不到 50 刀，对比目前智谱近 500 块人民币的月费，差距很明显。

不过订阅这种事，冲动消费是大忌。再观察观察，等方案稳定下来再说。务实派的做法：用最低成本覆盖最强工具链。

## 关键操作
- 腾讯 VPS 安装 Hermes Agent，调试成功
- Hermes Agent 与微信 IM 通信调试通过
- 腾讯 VPS 加装 hysteria2 科学上网服务器，调试成功
- 评估 AI 模型订阅方案：opencode-go 10 刀 + GitHub Copilot 39 刀

## 碎片想法
- opencode-go + GitHub Copilot 的组合性价比很高，但还需要观察再决定
- 两套服务从零搭到一次调通，这种节奏感很舒服
- 用最低成本覆盖最强工具链，务实优先
