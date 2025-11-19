---
author: Hamel Husain
category: articles
source: reader
date: 2025-11-18
URL: https://hamel.dev/blog/posts/evals/
---
Hamel Husain #reader

## Summary
How to construct domain-specific LLM evaluation systems.

## Highlights
Like software engineering, success with AI hinges on how fast you can iterate. You must have processes and tools for:
1. Evaluating quality (ex: tests).
2. Debugging issues (ex: logging & inspecting data).
3. Changing the behavior or the system (prompt eng, fine-tuning, writing code)
**Many people focus exclusively on #3 above, which prevents them from improving their LLM products beyond a demo.**[1](https://hamel.dev/blog/posts/evals/#fn1) Doing all three activities well creates a virtuous cycle differentiating great from mediocre AI products (see the diagram below for a visualization of this cycle). ([View Highlight](https://read.readwise.io/read/01jkh7bcbqfv90vhzbggyydwe2))

Rigorous and systematic evaluation is the most important part of the whole system. That is why “Eval and Curation” is highlighted in yellow at the center of the diagram. You should spend most of your time making your evaluation more robust and streamlined.
There are three levels of evaluation to consider:
• Level 1: Unit Tests
• Level 2: Model & Human Eval (this includes debugging)
• Level 3: A/B testing ([View Highlight](https://read.readwise.io/read/01jkh7dmyevk6tmp4pt8qx14k1))

Evaluation systems create a flywheel that allows you to iterate very quickly. It’s almost always where people get stuck when building AI products. I hope this post gives you an intuition on how to go about building your evaluation systems. Some key takeaways to keep in mind:
• Remove ALL friction from looking at data.
• Keep it simple. Don’t buy fancy LLM tools. Use what you have first.
• You are doing it wrong if you aren’t looking at lots of data.
• Don’t rely on generic evaluation frameworks to measure the quality of your AI. Instead, create an evaluation system specific to your problem.
• Write lots of tests and frequently update them.
• LLMs can be used to unblock the creation of an eval system. Examples include using a LLM to:
• Generate test cases and write assertions
• Generate synthetic data
• Critique and label data etc.
• Re-use your eval infrastructure for debugging and fine-tuning. ([View Highlight](https://read.readwise.io/read/01jkh7xyy1r5er90hx1ez9nxzy))

