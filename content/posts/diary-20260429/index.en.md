---
title: "Diary 2026-04-29"
date: 2026-04-29
tags: [diary, voice-input, open-source, tmux, dialect, domestic-models]
cover: gradient-3
summary: "Designed a voice-input app PRD and completed front-end compilation based on the opentypeless open-source project; received a Claude account ban notice in the evening and decided to switch fully to domestic AI models."
---

I spent the entire day on voice-input software design and development.

Starting from product requirements, the most critical need was clear: existing voice-input software has almost no support for local dialects, and I needed an architecture that could expose a model fine-tuning interface. After a long design session, the first version of the PRD took shape.

Just as I was about to start building from scratch, I remembered — it's the internet era. Check GitHub first. Sure enough, I found a project called opentypeless. I re-adapted the functionality on top of it, rewrote the design document, and then used tmux to remote-control the Mac mini from my phone to complete the front-end compilation. First time genuinely leveraging an open-source project for local compilation. GitHub being called "the first place communism worked" clicked in a concrete way today.

In the evening, an email from Anthropic arrived: my Claude account was banned. Looking back, the likely cause was frequently routing Claude through domestic models. Using overseas AI services from China has always been a squeeze — if it's gone, it's gone. Domestic models can handle most tasks now. Time to switch fully.

## Key actions
- Designed voice-input software product plan, completed first-version PRD
- Re-adapted functionality based on opentypeless open-source project, rewrote design document
- Completed front-end compilation from phone via tmux remote session
- Open-sourced a web-translation software project on GitHub
- Received Claude account ban notice; decided to switch to domestic models

## Fragments
- Dialect support is the core need — existing apps barely handle local dialects; model fine-tuning interface is essential
- First time completing a large compilation project on Mac mini remotely from a phone via tmux; survived network interruptions
- First time genuinely leveraging a GitHub open-source project for local compilation — the power of open-source collaboration is real
- The Claude ban ended up being a catalyst, accelerating the decision to go domestic

## AI take
> From idea to PRD to compilation in a single day — that's a complete product launch cycle. Two firsts in one day — mobile remote compilation and open-source project reuse — both landed cleanly. The Claude ban at the end became a catalyst. Sometimes constraints force better paths.
