---
author: Shawn swyx Wang
category: articles
source: reader
date: 2025-11-18
URL: https://www.latent.space/p/s3
---
Shawn swyx Wang #reader

## Summary
Annotated notes on Andrej's talk at YC AI Startup School 2025

## Highlights
Some things work extremely well (by human standards) while some things fail catastrophically (again by human standards), and it's not always obvious which is which, though you can develop a bit of intuition over time. ([View Highlight](https://read.readwise.io/read/01jykqygfw5gn42m32pk7gjj7g))

T**he big one I think is the present lack of "cognitive self-knowledge", which requires more sophisticated approaches in model post-training instead of the naive "imitate human labelers and make it big" solutions that have mostly gotten us this far** ([View Highlight](https://read.readwise.io/read/01jykqz5fk9m8xzks4tgmtekj9))

I like to talk explain it as LLMs are a bit like a coworker with Anterograde amnesia - they don't consolidate or build long-running knowledge or expertise once training is over and all they have is short-term memory ([View Highlight](https://read.readwise.io/read/01jykqzhpptdbjf9n25xt3dbx1))

We're missing (at least one) major paradigm for LLM learning. Not sure what to call it, possibly it has a name - **system prompt learning**?
Pretraining is for knowledge.
Finetuning (SL/RL) is for habitual behavior. ([View Highlight](https://read.readwise.io/read/01jykr1nwemw10yz0dydw926sy))

It feels more like taking notes for yourself, i.e. **something like the "Memory" feature but not to store per-user random facts, but general/global problem solving knowledge and strategies.** ([View Highlight](https://read.readwise.io/read/01jykr1kj1hvfj0yf7wvefqwzj))

Note that **this paradigm is also significantly more powerful and data efficient because a knowledge-guided "review" stage is a significantly higher dimensional feedback channel than a reward scaler.** ([View Highlight](https://read.readwise.io/read/01jykr25jh3ha69fbm14kk2wk3))

**It should come from System Prompt learning, which resembles RL in the setup, with the exception of the learning algorithm (edits vs gradient descent)**. ([View Highlight](https://read.readwise.io/read/01jykr2zcjageg5dnzenfdzj8s))

In the Generation <-> verification cycle, we a need full workflow of partial autonomy - the faster the loop the better:
• **To improve verification**: Make it easy, fast to win
• **To improve generation**: Keep AI on tight leash ([View Highlight](https://read.readwise.io/read/01jykr4bn2eqh9kv8add7h9cm4))

