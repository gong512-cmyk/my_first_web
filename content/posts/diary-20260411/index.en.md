---
title: "Diary 2026-04-11"
date: 2026-04-11
tags: [VPS, proxy, hysteria2, clash.verge, Karpathy, LLM-Wiki, Obsidian, knowledge-base]
cover: gradient-3
summary: "Set up a VPS proxy independently, breaking free from paid services; also discovered that Karpathy's LLM Wiki method aligns perfectly with my own knowledge base project."
---

If I had to sum up today in a phrase, it would be "building infrastructure." One path outward, one path inward.

The outward path: I finally did something I had been wanting to tackle but always felt slightly intimidated by—setting up a proxy on a VPS for scientific internet access. I used hysteria2 for the server side and clash.verge for the client, deployed on a US server, working through the whole process step by step with AI guidance. When it finally connected, I have to admit, it felt pretty good.

Breaking free from paid services is not just about saving money. More importantly, every piece of this setup was built by my own hands. If something breaks, I know where to look. If I want to tweak a parameter, I know where it lives. Stability is still an open question—whether the configuration is fully correct needs time to verify—but the framework is standing.

The inward path: in the afternoon, I came across Ian's write-up testing Karpathy's LLM Wiki method. Reading through it, I had this uncanny feeling: wait, this is exactly what I am building.

The method is beautifully simple. A `raw/` directory for source materials—Claude reads but never writes there. A `wiki/` directory for Claude's digested notes, organized by topic. An `index.md` for global navigation, a `log.md` recording every operation. Then three trigger phrases baked into `CLAUDE.md`: "add to wiki" auto-archives and merges, "what do I know about X" searches the wiki before answering, "lint wiki" checks for dead links and contradictions. Obsidian for visualization, Claude Code as the brain. Notes shift from "I write for myself" to "Claude maintains, I query anytime."

This is essentially the same thing I am building with my Obsidian knowledge base: a raw layer plus a knowledge layer. Materials are never lost, and you never have to organize them yourself. Seeing someone else walk this same path, and walk it so clearly, gave me a real sense of reassurance.

From setting up a proxy to setting up a knowledge base—today was all about "build it once, enjoy the peace of mind for a long time." The direction feels right.

## Key actions
- Independently set up a VPS proxy (hysteria2 server + clash.verge client)
- Successfully accessed the internet through the proxy
- Studied Karpathy's LLM Wiki method, cross-referencing with my own knowledge base architecture

## Fragments
- First time completing this kind of network configuration independently with AI guidance—the sense of achievement outweighs the practical benefit
- Paid alternatives and stability still need ongoing observation
- Karpathy's LLM Wiki method and my own knowledge base are the same thing at their core: a raw layer + a knowledge layer. Materials are never lost, and you never have to organize them yourself
- That is the nature of infrastructure—it takes effort to build, but once it is up, it saves you hassle for a long, long time
