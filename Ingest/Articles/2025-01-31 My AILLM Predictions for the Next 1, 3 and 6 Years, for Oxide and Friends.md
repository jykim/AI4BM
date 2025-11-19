---
author: simonwillison.net
category: articles
source: reader
date: 2025-11-18
URL: https://simonwillison.net/2025/Jan/10/ai-predictions/#one-year-agents-fail-to-happen-again
---
simonwillison.net #reader

## Summary
The Oxide and Friends podcast has an annual tradition of asking guests to share their predictions for the next 1, 3 and 6 years. Here’s 2022, 2023 and 2024. This …

## Highlights
My AI/LLM predictions for the next 1, 3 and 6 years, for Oxide and Friends
10th January 2025
The [Oxide and Friends](https://oxide-and-friends.transistor.fm/) podcast has an annual tradition of asking guests to share their predictions for the next 1, 3 and 6 years. Here’s [2022](https://github.com/oxidecomputer/oxide-and-friends/blob/master/2022_01_03.md), [2023](https://github.com/oxidecomputer/oxide-and-friends/blob/master/2023_01_09.md) and [2024](https://github.com/oxidecomputer/oxide-and-friends/blob/master/2024_01_08.md). This year they invited me to participate. I’ve never been brave enough to share *any* public predictions before, so this was a great opportunity to get outside my comfort zone!
We recorded the episode live using Discord on Monday. It’s now available [on YouTube](https://www.youtube.com/watch?v=-pk6VokHpGY) and [in podcast form](https://oxide-and-friends.transistor.fm/).
Play: Oxide and Friends 1/6/2025 -- Predictions 2025
Here are my predictions, written up here in a little more detail than the stream of consciousness I shared on the podcast.
I should emphasize that I find the very idea of trying to predict AI/LLMs over a multi-year period to be completely absurd! I can’t predict what’s going to happen a week from now, six years is a different universe.
With that disclaimer out of the way, here’s an expanded version of what I said.
• [One year: Agents fail to happen, again](https://simonwillison.net/2025/Jan/10/ai-predictions/#one-year-agents-fail-to-happen-again)
• [One year: ... except for code and research assistants](https://simonwillison.net/2025/Jan/10/ai-predictions/#one-year-code-research-assistants)
• [Three years: Someone wins a Pulitzer for AI-assisted investigative reporting](https://simonwillison.net/2025/Jan/10/ai-predictions/#three-years-someone-wins-a-pulitzer-for-ai-assisted-investigative-reporting)
• [Three years part two: privacy laws with teeth](https://simonwillison.net/2025/Jan/10/ai-predictions/#three-years-part-two-privacy-laws-with-teeth)
• [Six years utopian: amazing art](https://simonwillison.net/2025/Jan/10/ai-predictions/#six-years-utopian-amazing-art)
• [Six years dystopian: AGI/ASI causes mass civil unrest](https://simonwillison.net/2025/Jan/10/ai-predictions/#six-years-dystopian-agi-asi-causes-mass-civil-unrest)
• [My total lack of conviction](https://simonwillison.net/2025/Jan/10/ai-predictions/#my-total-lack-of-conviction)
One year: Agents fail to happen, again [#](https://simonwillison.net/2025/Jan/10/ai-predictions/#one-year-agents-fail-to-happen-again)
I wrote about how [“Agents” still haven’t really happened yet](https://simonwillison.net/2024/Dec/31/llms-in-2024/#-agents-still-haven-t-really-happened-yet) in my review of Large Language Model developments in 2024.
I think we are going to see a *lot* more froth about agents in 2025, but I expect the results will be a great disappointment to most of the people who are excited about this term. I expect a lot of money will be lost chasing after several different poorly defined dreams that share that name.
What are agents anyway? Ask a dozen people and you’ll get a dozen slightly different answers—I collected and [then AI-summarized a bunch of those here](https://gist.github.com/simonw/beaa5f90133b30724c5cc1c4008d0654).
For the sake of argument, let’s pick a definition that I can predict won’t come to fruition: the idea of an AI assistant that can go out into the world and semi-autonomously act on your behalf. I think of this as the **travel agent** definition of agents, because for some reason everyone always jumps straight to flight and hotel booking and itinerary planning when they describe this particular dream.
Having the current generation of LLMs make material decisions on your behalf—like what to spend money on—is a *really bad idea*. They’re too unreliable, but more importantly they are too **gullible**.
If you’re going to arm your AI assistant with a credit card and set it loose on the world, you need to be confident that it’s not going to hit “buy” on the first website that claims to offer the best bargains!
I’m confident that reliability is the reason we haven’t seen LLM-powered agents that have taken off yet, despite the idea attracting a huge amount of buzz since right after ChatGPT first came out.
I would be very surprised if any of the models released over the next twelve months had enough of a reliability improvement to make this work. Solving gullibility is an astonishingly difficult problem.
(I had [a particularly spicy rant](https://www.youtube.com/watch?v=-pk6VokHpGY&t=1206s) about how stupid the idea of sending a “digital twin” to a meeting on your behalf is.)
One year: ... except for code and research assistants [#](https://simonwillison.net/2025/Jan/10/ai-predictions/#one-year-code-research-assistants)
There are two categories of “agent” that I do believe in, because they’re proven to work already.
The first is **coding assistants**—where an LLM writes, executes and then refines computer code in a loop.
I first saw this pattern demonstrated by OpenAI with their [Code Interpreter](https://simonwillison.net/tags/code-interpreter/) feature for ChatGPT, released back in March/April of 2023.
You can ask ChatGPT to solve a problem that can use Python code and it will write that Python, execute it in a secure sandbox (I think it’s Kubernetes) and then use the output—or any error messages—to determine if the goal has been achieved.
It’s a beautiful pattern that worked great with early 2023 models (I believe it first shipped using original GPT-4), and continues to work today.
Claude added their own version in October ([Claude analysis](https://simonwillison.net/2024/Oct/24/claude-analysis-tool/), using JavaScript that runs in the browser), Mistral have it, Gemini has a version and there are dozens of other implementations of the same pattern.
The second category of agents that I believe in is **research assistants**—where an LLM can run multiple searches, gather information and aggregate that into an answer to a question or write a report.
[Perplexity](https://www.perplexity.ai/) and [ChatGPT Search](https://openai.com/index/introducing-chatgpt-search/) have both been operating in this space for a while, but by far the most impressive implementation I’ve seen is Google Gemini’s [Deep Research](https://blog.google/products/gemini/google-gemini-deep-research/) tool, which I’ve had access to for a few weeks.
With Deep Research I can pose a question like this one:
> Pillar Point Harbor is one of the largest communal brown pelican roosts on the west coast of North America.
> 
> find others ([View Highlight](https://read.readwise.io/read/01jjx10kce3k6b3e1bhyebf6j4))

[Perplexity](https://www.perplexity.ai/) and [ChatGPT Search](https://openai.com/index/introducing-chatgpt-search/) have both been operating in this space for a while, but by far the most impressive implementation I’ve seen is Google Gemini’s [Deep Research](https://blog.google/products/gemini/google-gemini-deep-research/) tool, which I’ve had access to for a few weeks.
With Deep Research I can pose a question like this one:
> Pillar Point Harbor is one of the largest communal brown pelican roosts on the west coast of North America.
> 
> find others
And Gemini will draft a plan, consult dozens of different websites via Google Search and then assemble a report (with all-important citations) describing what it found. ([View Highlight](https://read.readwise.io/read/01jjx15cje0ntwkhczm8j17n1d))

It makes intuitive sense to me that this kind of research assistant can be built on our current generation of LLMs. They’re competent at driving tools, they’re capable of coming up with a relatively obvious research plan (look for newspaper articles and research papers) and they can synthesize sensible answers given the right collection of context gathered through search.
Google are particularly well suited to solving this problem: they have the world’s largest search index and their Gemini model has a 2 million token context. I expect Deep Research to get a whole lot better, and I expect it to attract plenty of competition. ([View Highlight](https://read.readwise.io/read/01jjx17a43v1pxh7dmgkma2a5b))

I don’t think generative AI for art—images, video and music—deserves nearly the same level of respect as a useful tool as text-based LLMs. Generative art tools are a lot of fun to try out but the lack of fine-grained control over the output greatly limits its utility outside of personal amusement or generating [slop](https://simonwillison.net/tags/slop/). ([View Highlight](https://read.readwise.io/read/01jjx1bqav2bzmej1m8yty0xvb))

