---
title: "Diary 2026-04-05"
date: 2026-04-05
tags: [multi-agent, OpenClaw, skill debugging, AI models]
cover: gradient-1
summary: "Deep dive into OpenClaw's multi-agent skill—after multiple rounds of debugging, successfully ran a three-role collaboration pipeline: search, analysis, and review."
---

After getting back from the hometown trip, I dove straight into OpenClaw's multi-agent skill.

The core idea is genuinely interesting: automatically decompose a complex task into a DAG task graph, then distribute it across agents running different models to collaborate in parallel. In plain terms—multiple AIs each doing their own job simultaneously. Some search, some analyze, some review. Everything converges into a single finished output.

Nice on paper. Getting it to actually work was another story. From v1 to v5, I hit four or five roadblocks. The biggest headache was Xiaomi's MiMo model—its tool-calling kept failing when trying to write files. After a lot of trial and error, I bypassed the issue by redirecting bash output instead. Not elegant, but it works.

The framework is now running end-to-end—the full three-role pipeline of search, analysis, and review completed successfully in one chain. Whether it actually delivers in real-world use remains to be tested with genuine tasks. Also worth noting: several models are on monthly subscriptions, so I need to keep an eye on renewal dates.

## Key actions

- Deep research into OpenClaw's multi-agent skill and its DAG task decomposition mechanism
- Multiple debugging rounds (v1 through v5), fixed MiMo model tool-calling file write failures by switching to bash redirects
- Successfully ran the complete three-role collaboration pipeline: search → analysis → review
- Confirmed several models are on monthly billing cycles—need to track renewal dates

## Fragments

One takeaway from the debugging process: a well-designed framework is one thing, real-world effectiveness is another. Multi-agent systems sound beautiful in theory—parallelism, division of labor, collaboration—but in practice, the coordination overhead between agents and the instability of individual models are the real bottlenecks. I need to throw a few real tasks at this thing and see whether it's a productivity tool or just a cool-looking toy.
