---
title: "Diary 2026-04-14"
date: 2026-04-14
tags: [AI-era, decision-fatigue, workflow, safety-net-thinking]
cover: gradient-1
summary: "Spent the morning reflecting on why better AI makes people more tired, distilling three types of mental drain and a practical fallback framework to cope."
---

This morning I did not write a single line of code. Instead, I sat with a bigger question: as AI keeps getting better, why do people keep getting more tired?

A blogger I follow put it in a way that landed hard. The ultimate reason, he said, is that most of us used to be executors. Now we have become commanders and schedulers. And being a commander involves three of the most mentally draining activities there are.

First, decision fatigue. The information explosion forces you to make frequent choices and judgments in very short time windows. Every decision chips away at your mental reserves, and the accumulation is brutal. Second, memory overflow. AI's high-speed responses funnel a torrent of information toward you—several times what a normal workload would produce—and your brain is forced to carry far more than it is built for. Third, attention switching. You have to rapidly toggle between decisions, memories, and different task roles. Every switch has a cost, and the switching frequency today is higher than it has ever been.

At its core, AI has driven the cost of execution to near zero—but you are still the one responsible for the outcome. And AI execution is fundamentally probabilistic. It does not guarantee correctness every time. Which means you are not just managing tasks. You are managing uncertainty.

Once I worked through this, a coping framework started to form.

The key is establishing a "fallback behavior": let AI try repeatedly, and let the human make the final fallback decision. As long as things are moving in the right direction, the imperfections and rough edges along the way can be handled by the fallback mechanism. This is essentially a fault-tolerance design—accepting that AI execution is probabilistic, and freeing human mental energy from micro-corrections so it can be reserved for macro judgment.

With this in place, the whole process might feel a bit more natural, a bit lighter. Not doing less work—just spending the effort where it actually counts.

On a more practical note, I also fixed the OpenClaw memory system's CLI diagnostic command today—switched the embedding provider from ollama to openai with an Ollama endpoint—and then ran a full health check on the memory systems of all three agents (Xiao Min / Xiao Zhao / Xiao Gang). All clear.

## Key actions
- Fixed the OpenClaw memory system CLI diagnostic command (switched embedding provider from ollama to openai + Ollama endpoint)
- Completed a full memory system health check for all three agents (Xiao Min, Xiao Zhao, Xiao Gang)

## Fragments
- The ultimate reason AI progress makes people more tired: the human role has shifted from executor to commander/scheduler
- The three most mentally draining activities: decision fatigue, memory overflow, attention switching
- We used to aim for getting things right in one shot; now AI execution costs near zero, but we still own the result
- Coping strategy: establish a fallback behavior, let AI try repeatedly, human makes the fallback decision, accept imperfections in the process
- Fallback thinking is fault-tolerance design—freeing human energy from micro-corrections and reserving it for macro judgment
