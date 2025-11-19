---
author: anthropic.com
category: articles
source: reader
date: 2025-11-18
URL: https://share.google/PT2cOHDmVK4wAx8UL
---
anthropic.com #reader

## Summary
On the the engineering challenges and lessons learned from building Claude's Research system

## Highlights
Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously. Systems with multiple agents introduce new challenges in agent coordination, evaluation, and reliability. ([View Highlight](https://read.readwise.io/read/01jxpkfr80kc3nbcgketg9wj9c))

This unpredictability makes AI agents particularly well-suited for research tasks. Research demands the flexibility to pivot or explore tangential connections as the investigation unfolds. The model must operate autonomously for many turns, making decisions about which directions to pursue based on intermediate findings. A linear, one-shot pipeline cannot handle these tasks. ([View Highlight](https://read.readwise.io/read/01jxpkhkjmxw5wrv3qspx098pa))

The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent. Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations. ([View Highlight](https://read.readwise.io/read/01jxpkhcvjvx440643kzvkdkvf))

Once intelligence reaches a threshold, multi-agent systems become a vital way to scale performance. For instance, although individual humans have become more intelligent in the last 100,000 years, human societies have become *exponentially* more capable in the information age because of our *collective* intelligence and ability to coordinate. Even generally-intelligent agents face limits when operating as individuals; groups of agents can accomplish far more. ([View Highlight](https://read.readwise.io/read/01jxpkhw7bkcg87t2n4fjh7689))

Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. For example, when asked to identify all the board members of the companies in the Information Technology S&P 500, the multi-agent system found the correct answers by decomposing this into tasks for subagents, while the single agent system failed to find the answer with slow, sequential searches. ([View Highlight](https://read.readwise.io/read/01jxpkjp4qc7nmtzjzfhmgzyqs))

Multi-agent systems work mainly because they help spend enough tokens to solve the problem. In our analysis, three factors explained 95% of the performance variance in the [BrowseComp](https://openai.com/index/browsecomp/) evaluation (which tests the ability of browsing agents to locate hard-to-find information). ([View Highlight](https://read.readwise.io/read/01jxpkm8e3t8sv6e6ba8j5k0r5))

The latest Claude models act as large efficiency multipliers on token use, as upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7. Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents. ([View Highlight](https://read.readwise.io/read/01jxpkn5xgbfe6cvxfn7kvvg54))

There is a downside: in practice, these architectures burn through tokens fast. In our data, agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats. For economic viability, multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance. ([View Highlight](https://read.readwise.io/read/01jxpkns80nrgqbzvxywxf1fwy))

**Scale effort to query complexity.** Agents struggle to judge appropriate effort for different tasks, so we embedded scaling rules in the prompts. Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities. ([View Highlight](https://read.readwise.io/read/01jxpksxvykmx1f2ra3thyeske))

**Let agents improve themselves**. We found that the Claude 4 models can be excellent prompt engineers. When given a prompt and a failure mode, they are able to diagnose why the agent is failing and suggest improvements. We even created a tool-testing agent—when given a flawed MCP tool, it attempts to use the tool and then rewrites the tool description to avoid failures. ([View Highlight](https://read.readwise.io/read/01jxpkv8fd354jk9g2ze42dq1b))

**Guide the thinking process.** [Extended thinking mode](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking), which leads Claude to output additional tokens in a visible thinking process, can serve as a controllable scratchpad. The lead agent uses thinking to plan its approach, assessing which tools fit the task, determining query complexity and subagent count, and defining each subagent’s role. ([View Highlight](https://read.readwise.io/read/01jxpkvwrhtpcn3d02g178k5k6))

But multi-agent systems don't work this way. Even with identical starting points, agents might take completely different valid paths to reach their goal. One agent might search three sources while another searches ten, or they might use different tools to find the same answer. Because we don’t always know what the right steps are, we usually can't just check if agents followed the “correct” steps we prescribed in advance. Instead, we need flexible evaluation methods that judge whether agents achieved the right outcomes while also following a reasonable process. ([View Highlight](https://read.readwise.io/read/01jxpkx6mh2533vrj8jmb0r3c8))

**Start evaluating immediately with small samples**. In early agent development, changes tend to have dramatic impacts because there is abundant low-hanging fruit. A prompt tweak might boost success rates from 30% to 80%. With effect sizes this large, you can spot changes with just a few test cases. ([View Highlight](https://read.readwise.io/read/01jxpkxwgd4ntj58shg4mgkjtj))

**LLM-as-judge evaluation scales when done well.** Research outputs are difficult to evaluate programmatically, since they are free-form text and rarely have a single correct answer. LLMs are a natural fit for grading outputs. We used an LLM judge that evaluated each output against criteria in a rubric: factual accuracy (do claims match sources?), citation accuracy (do the cited sources match the claims?), completeness (are all requested aspects covered?), source quality (did it use primary sources over lower-quality secondary sources?), and tool efficiency (did it use the right tools a reasonable number of times?). ([View Highlight](https://read.readwise.io/read/01jxpkyngj61w9hhe79hvpcse9))

