---
author: Timothy B. Lee
category: articles
source: reader
date: 2025-11-18
URL: https://www.understandingai.org/p/openai-just-unleashed-an-alien-of?r=gz7vv&utm_medium=ios&triedRedirect=true
---
Timothy B. Lee #reader

## Summary
It's not easy to stump OpenAI's new o1 models.

## Highlights
Reinforcement learning takes a different approach. Rather than trying to perfectly reproduce every token in the training data, reinforcement learning grades a response based on whether it ultimately got to the right answer. This kind of feedback becomes more essential as the number of reasoning steps increases.
So if reinforcement learning is so great, why doesn’t everyone use it? One reason is that reinforcement learning can suffer from a problem called sparse rewards. If an LLM has only produced five tokens of a 100-token answer, there may be no way for the reinforcement learning algorithm to know if it’s on track toward a correct answer. So a model trained entirely with reinforcement learning might never get good enough to start receiving positive feedback.
Whatever its faults, imitation learning can at least give feedback on every token. This makes it a good choice for the early phases of training when a nascent model can’t even produce coherent sentences. Once the model is able to produce good answers some of the time, then reinforcement learning can help it improve more quickly.
The other challenge is that reinforcement learning requires an objective way to judge a model’s output. ([View Highlight](https://read.readwise.io/read/01jjdd2j9xcnbzhpv7ds3k7z2x))

I’m quite impressed by the o1 models, but I do want to point out something that all of my examples have in common: they contain all necessary information within the four corners of a relatively short problem statement.
Most problems in the real world aren’t like this. Human workers spend decades accumulating knowledge that makes us more effective at our jobs. Sometimes solving a problem requires remembering facts from a conversation we had, or a research paper we read, months or years ago. Sometimes we’re missing key information and have to figure out what to read or who to talk to in order to get it.
I don’t think OpenAI is close to mastering this kind of problem. ([View Highlight](https://read.readwise.io/read/01jjdd5nzmevar3mya4ch40qnd))

