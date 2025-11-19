---
author: Chip Huyen
category: books
source: ibooks
date: 2025-11-18
URL:
---
Chip Huyen #ibooks

## Highlights
While completion is powerful, completion isn’t the same as engaging in a conversation. For example, if you ask a completion machine a question, it can complete what you said by adding another question instead of answering the question. “Post-Training” discusses how to make a model respond appropriately to a user’s request.

Figure 1-10. AI can be used throughout all four stages of course creation at Duolingo, but it’s the most helpful in the personalization stage. Image from Pajak and Bicknell (Duolingo, 2022).

At a high level, building applications using foundation models today differs from traditional ML engineering in three major ways:
Without foundation models, you have to train your own models for your applications. With AI engineering, you use a model someone else has trained for you. This means that AI engineering focuses less on modeling and training, and more on model adaptation.
AI engineering works with models that are bigger, consume more compute resources, and incur higher latency than traditional ML engineering.

AI engineering works with models that can produce open-ended outputs. Open-ended outputs give models the flexibility to be used for more tasks, but they are also harder to evaluate. This makes evaluation a much bigger problem in AI engineering.

With the availability of foundation models, ML knowledge is no longer a must-have for building AI applications. I’ve met many wonderful and successful AI application builders who aren’t at all interested in learning about gradient descent. However, ML knowledge is still extremely valuable, as it expands the set of tools that you can use and helps troubleshooting when a model doesn’t work as expected.

In traditional ML engineering, most use cases are close-ended—a model’s output can only be among predefined values. For example, spam classification with only two possible outputs, “spam” and “not spam”, is close-ended. Foundation models, however, are open-ended. Annotating open-ended queries is much harder than annotating close-ended queries—it’s easier to determine whether an email is spam than to write an essay. So data annotation is a much bigger challenge for AI engineering.

Many people argue that because models are now commodities, data will be the main differentiator, making dataset engineering more important than ever.

One challenge with foundation models is that they are often autoregressive—tokens are generated sequentially. If it takes 10 ms for a model to generate a token, it’ll take a second to generate an output of 100 tokens, and even more for longer outputs. As users are getting notoriously impatient, getting AI applications’ latency down to the 100 ms latency expected for a typical internet application is a huge challenge.

With traditional ML engineering, where teams build applications using their proprietary models, the model quality is a differentiation. With foundation models, where many teams use the same model, differentiation must be gained through the application development process.

The existence of so many adaptation techniques also makes evaluation harder. A system that performs poorly with one technique might perform much better with another

Gemini evaluation story highlights the impact of prompt engineering on model performance. By using a different prompt engineering technique, Gemini Ultra’s performance on MMLU went from 83.7% to 90.04%.

With traditional ML engineering, you usually start with gathering data and training a model. Building the product comes last. However, with AI models readily available today, it’s possible to start with building the product first, and only invest in data and models once the product shows promise, as visualized in Figure 1-16.

In traditional ML engineering, model development and product development are often disjointed processes, with ML engineers rarely involved in product decisions at many organizations. However, with foundation models, AI engineers tend to be much more involved in building the product.

First, the more intelligent AI models become, the harder it is to evaluate them. Most people can tell if a first grader’s math solution is wrong. Few can do the same for a PhD-level math solution.4 It’s easy to tell if a book summary is bad if it’s gibberish, but a lot harder if the summary is coherent.

erplexity might not be a great proxy to evaluate models that have been post-trained using techniques like SFT and RLHF.9 Post-training is about teaching models how to complete tasks. As a model gets better at completing tasks, it might get worse at predicting the next tokens. A language model’s perplexity typically increases after post-training. Some people say that post-training collapses entropy. Similarly, quantization—a technique that reduces a model’s numerical precision and, with it, its memory footprint—can also change a model’s perplexity in unexpected ways.10

A new frontier is to create joint embeddings for data of different modalities. CLIP (Radford et al., 2021) was one of the first major models that could map data of different modalities, text and images, into a joint embedding space.

Table 3-3. Examples of built-in AI as a judge criteria offered by some AI tools, as of September 2024. Note that as these tools evolve, these built-in criteria will change.
AI Tools
Built-in criteria 
Azure AI Studio
Groundedness, relevance, coherence, fluency, similarity
MLflow.metrics
Faithfulness, relevance
LangChain Criteria Evaluation
Conciseness, relevance, correctness, coherence, harmfulness, maliciousness, helpfulness, controversiality, misogyny, insensitivity, criminality
Ragas
Faithfulness, answer relevance

AI judges tend to have self-bias, where a model favors its own responses over the responses generated by other models. The same mechanism that helps a model compute the most likely response to generate will also give this response a high score. In Zheng et al.’s 2023 experiment, GPT-4 favors itself with a 10% higher win rate, while Claude-v1 favors itself with a 25% higher win rate.

Some AI judges have verbosity bias, favoring lengthier answers, regardless of their quality. Wu and Aji (2023) found that both GPT-4 and Claude-1 prefer longer responses (~100 words) with factual errors over shorter, correct responses (~50 words). Saito et al. (2023) studied this bias for creative tasks and found that when the length difference is large enough (e.g., one response is twice as long as the other), the judge almost always prefers the longer one.19 Both Zheng et al. (2023) and Saito et al. (2023), however, discovered that GPT-4 is less prone to this bias than GPT-3.5, suggesting that this bias might go away as models become stronger.

Using a model to judge itself, self-evaluation or self-critique, sounds like cheating, especially because of self-bias. However, self-evaluation can be great for sanity checks. If a model thinks its own response is incorrect, the model might not be that reliable.

One open question is whether the judge can be weaker than the model being judged. Some argue that judging is an easier task than generating. Anyone can have an opinion about whether a song is good, but not everyone can write a song. Weaker models should be able to judge the outputs of stronger models.
Zheng et al. (2023) found that stronger models are better correlated to human preference, which makes people opt for the strongest models they can afford.

