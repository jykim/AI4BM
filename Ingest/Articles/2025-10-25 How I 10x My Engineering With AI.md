---
author: Kieran Klaassen
category: articles
source: reader
date: 2025-11-18
URL: https://every.to/source-code/the-three-ways-i-work-with-llms
---
Kieran Klaassen #reader

## Summary
What used to take me a week of coding now happens in hours. The secret is knowing which AI workflow fits your problem.

## Highlights
This might sound like [vibe coding](https://every.to/source-code/i-rebuilt-sparkle-in-14-days-with-ai) on the surface, but there’s an important distinction in terms of intention. Vibe coding works from the outside in: You tell the AI what you want the software to do and let it figure out [how to get there](https://every.to/working-overtime/i-tried-ai-coding-tools-now-i-want-to-learn-to-code). My approach is inside-out: I already know both the destination and the route. I've decided on the architecture, the patterns, and the specific implementation details. I'm just delegating the mechanical act of translating those decisions into syntax. The AI is my hands, not my brain. ([View Highlight](https://read.readwise.io/read/01k8cne35nxc2f7s9bfv1e9khd))

The key advantage is speed without sacrificing quality or accuracy. I speak, and the AI translates my intentions into code. It feels like pair programming with a skilled partner who never gets tired. ([View Highlight](https://read.readwise.io/read/01k8cne5prc9x170q1x9qhap8f))

This mode works best when the stakes are low and the direction is clear. I'm not relying on the AI for big architectural decisions—I'm using it to implement solutions I could code myself but prefer to delegate.
**I reach for this workflow when:**
1. I know exactly what “done” looks like.
2. I'm working on a single, focused task.
3. I need to build efficiently without breaking flow.
This is the mode I default to when I'm already mid-sprint or almost done and just need to keep moving. ([View Highlight](https://read.readwise.io/read/01k8cnggr6pnvmca45ybf922yy))

**Parallel progress with Claude Code, Devin, or Cursor agents: The CTO's method**
My most experimental (and exciting) workflow involves working on multiple features simultaneously, much like a CTO overseeing several engineering teams. I'm convinced this represents the future of software development, though it's currently the hardest approach to master because it’s new. It’s experimental.There aren’t any established best practices yet, because we haven’t had time yet to find them.
Here’s when the CTO method makes sense:
1. You have multiple components that are not dependent on each other to build.
2. Each component has clear boundaries and specifications.
3. You've already done the architectural thinking up front.
I start by breaking down my day into discrete tasks, creating detailed specifications for each, and then delegating them to separate AI agents—either using Devin (which creates full pull requests), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) with [git worktrees](https://git-scm.com/docs/git-worktree), OpenAI’s [Codex](https://every.to/chain-of-thought/vibe-check-codex-openai-s-new-coding-agent), or [Cursor Background Agents](https://docs.cursor.com/background-agent) working on different parts of the codebase. ([View Highlight](https://read.readwise.io/read/01k8cnjf4h4bz9grsnr312hmv0))

