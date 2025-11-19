---
author: 🔳 Turing Post
category: articles
source: reader
date: 2025-11-18
URL: https://www.turingpost.com/p/fod104?utm_source=www.turingpost.com&utm_medium=newsletter&utm_campaign=fod-104-ai-holy-shit-moments-of-the-year-and-what-s-still-not-there-yet&_bhlid=a5bcac79777986f96b516a0a01ce1be08f4e9ab3
---
🔳 Turing Post #reader

## Summary
short interviews from the AI Engineer World Fair, plus our regular curated selection of the most relevant AI news and research papers

## Highlights
It’s funny but a significant “wow” moment for one person might still feel like a “not there yet” to another. We also talked about what parts of their jobs they’d *actually* be happy to hand over to AI. ([View Highlight](https://read.readwise.io/read/01jxd6951b776vt6sp1tn7k9c5))

• **Code Generation & Planning:** The ability of models (specifically LLMs) to generate entire programs from scratch, write code for planning, and use tools effectively unlocks new applications. ([View Highlight](https://read.readwise.io/read/01jxd6a8dfjrx507p90rxza4k6))

• **Models Joining the Team:** Realizing models are now smart enough to join a software engineering team, write code, understand assignments, and make a plan was a "holy shit" moment indeed. ([View Highlight](https://read.readwise.io/read/01jxd69vd0k2z79qg9km3wkhew))

• **Autonomous Agents & Multi-Agent Systems:** Fully autonomous workflows and making agents communicate with each other introduce significant complexities and require more work. Multi-agent conversation and planning (MCP) is the largest track at the conference, but most people haven't put it in production yet and are skeptical. ([View Highlight](https://read.readwise.io/read/01jxd6av1tc3sawj099nh6m7jn))

• **Reinforcement Learning for Workflows:** Applying reinforcement learning to personal workflows without being an expert is exciting but not yet widely accessible. ([View Highlight](https://read.readwise.io/read/01jxd6b3r0y7g86zz1ddwer6kt))

• **Connecting Data to Reasoning Models:** The necessary ability to go from logs and user interaction data into valuable datasets, features, or directly piping back into reasoning models is talked about but not yet available, although some believe it will be there in the next year. ([View Highlight](https://read.readwise.io/read/01jxd6bkdz5nwtkz9qf41dwyp5))

The papers seem to study different phenomena. One investigates the limits of reasoning, the other of memorization. But what everybody missed is this: **they describe the same underlying breakdown – a model’s coping mechanism when pushed past its fundamental capacity.**
In the *Illusion of Thinking* paper, the model’s **processing capacity** – its effective “CPU” – is overloaded by puzzles that demand deep, multi-step reasoning. The model’s response is to **abort the task mid-thought**, reducing reasoning effort as complexity increases. This leads to a visible *reasoning collapse*.
In the *Memorization* paper, the model’s **storage capacity** – its “Hard Drive” – is saturated by large training sets. The model can’t memorize everything, so it begins to **compress aggressively by generalizing**. This triggers the double descent phenomenon and reduces the model’s ability to recall specifics. ([View Highlight](https://read.readwise.io/read/01jxd6g4eqxr6pdzcrwdk2h7g6))

**Same failure, different modality.** Whether the pressure comes from too many steps or too much data, the result is the same: **the model simplifies, guesses, or shuts down – all while still outputting something that looks fluent and confident.**
Reasoning collapse and forced generalization aren’t separate problems. **They’re two faces of the same coin: how finite architectures break under load.** ([View Highlight](https://read.readwise.io/read/01jxd6gyabr9wtwj31v5vbyx2v))

**Same failure, different modality.** Whether the pressure comes from too many steps or too much data, the result is the same: **the model simplifies, guesses, or shuts down – all while still outputting something that looks fluent and confident.**
Reasoning collapse and forced generalization aren’t separate problems. **They’re two faces of the same coin: how finite architectures break under load.** ([View Highlight](https://read.readwise.io/read/01jxd6h4b19g5ad6x77838qw51))

