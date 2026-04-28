---
title: "Diary 2026-04-13"
date: 2026-04-13
tags: [VPS, Hermes, Agent, WeChat, hysteria2, AI-subscription]
cover: gradient-4
summary: "Infrastructure day: deployed Hermes Agent on Tencent VPS, got WeChat IM working, added hysteria2 proxy, and scoped out a cost-effective AI subscription plan."
---

Today was a hands-on, get-things-built kind of day. The theme stayed on infrastructure, but stepped up a level—from building channels to deploying services.

I did two things on the Tencent VPS. First, I installed Hermes Agent and got it running, and also got the WeChat IM integration working. This means the agent can send and receive messages through WeChat—bringing AI capability directly into a daily communication tool. Second, I added a hysteria2 server on the same VPS for remote proxy access, and that came up smoothly as well.

Both services went from zero to fully working in one shot. Honestly, even I was a bit surprised by the efficiency. There is a real satisfaction in that rhythm of "install one, it works, move to the next"—way better than the grind of chasing down obscure config issues.

I also started seriously thinking about a long-term AI model subscription plan. Right now I am leaning toward opencode-go ($10/month) + GitHub Copilot ($39/month). The value proposition is really strong. opencode-go covers daily coding and agent orchestration, while Copilot's autocomplete and PR review experience keeps getting more polished. Combined, that is under $50 a month—a stark contrast to Zhipu's nearly 500 yuan monthly bill.

But subscriptions are exactly the kind of thing you should not impulse-buy. I will observe a bit longer, let the picture stabilize, then decide. Pragmatist's approach: cover the strongest toolchain at the lowest cost.

## Key actions
- Installed Hermes Agent on Tencent VPS and got it running
- Debugged and verified Hermes Agent to WeChat IM communication
- Added hysteria2 proxy server on Tencent VPS, successfully tested
- Evaluated AI subscription plan: opencode-go $10/mo + GitHub Copilot $39/mo

## Fragments
- The opencode-go + Copilot combo looks very cost-effective, but I want to observe more before committing
- Both services went from scratch to working in one pass—that rhythm feels really good
- Cover the strongest toolchain at the lowest cost. Pragmatism first
