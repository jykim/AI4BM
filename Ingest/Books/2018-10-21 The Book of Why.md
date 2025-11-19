---
author: Judea Pearl
category: books
source: ibooks
date: 2025-11-18
URL:
---
Judea Pearl #ibooks

## Highlights
More ambitiously, once we really understand the logic behind causal thinking, we could emulate it on modern computers and create an “artificial scientist.” This smart robot would discover yet unknown phenomena, find explanations to pending scientific dilemmas, design new experiments, and continually extract more causal knowledge from the environment

Unfortunately, statistics has fetishized this commonsense observation. It tells us that correlation is not causation, but it does not tell us what causation is. In vain will you search the index of a statistics textbook for an entry on “cause.” Students are not allowed to say that X is the cause of Y—only that X and Y are “related” or “associated.”

But I hope with this book to convince you that data are profoundly dumb. Data can tell you that the people who took a medicine recovered faster than those who did not take it, but they can’t tell you why. Maybe those who took the medicine did so because they could afford it and would have recovered just as fast without it.

Evolution has endowed us with the ability to engineer our lives, a gift she has not bestowed on eagles and owls, and the question, again, is “Why?” What computational facility did humans suddenly acquire that eagles did not?

In his book Sapiens, historian Yuval Harari posits that our ancestors’ capacity to imagine nonexistent things was the key to everything, for it allowed them to communicate better. Before this change, they could only trust people from their immediate family or tribe. Afterward their trust extended to larger communities, bound by common fantasies

Whether or not you agree with Harari’s theory, the connection between imagining and causal relations is almost self-evident. It is useless to ask for the causes of things unless you can imagine their consequences.

In fact, my research on machine learning has taught me that a causal learner must master at least three distinct levels of cognitive ability: seeing, doing, and imagining.

FIGURE 1.2. The Ladder of Causation, with representative organisms at each level. Most animals, as well as present-day learning machines, are on the first rung, learning from association. Tool users, such as early humans, are on the second rung if they act by planning and not merely by imitation. We can also use experiments to learn the effects of interventions, and presumably this is how babies acquire much of their causal knowledge. Counterfactual learners, on the top rung, can imagine worlds that do not exist and infer reasons for observed phenomena. (Source: Drawing by Maayan Harel.)

Good predictions need not have good explanations. The owl can be a good hunter without understanding why the rat always goes from point A to point B.

I fully agree with Gary Marcus, a neuroscientist at New York University, who recently wrote in the New York Times that the field of artificial intelligence is “bursting with microdiscoveries”—the sort of things that make good press releases—but machines are still disappointingly far from humanlike cognition.

The goal of strong AI is to produce machines with humanlike intelligence, able to converse with and guide humans. Deep learning has instead given us machines with truly impressive abilities but no intelligence. The difference is profound and lies in the absence of a model of reality.

The machine will not figure out for itself that a pedestrian with a bottle of whiskey in hand is likely to respond differently to a honking horn. This lack of flexibility and adaptability is inevitable in any system that works at the first level of the Ladder of Causation.

Intervention ranks higher than association because it involves not just seeing but changing what is. Seeing smoke tells us a totally different story about the likelihood of fire than making smoke. We cannot answer questions about interventions with passively collected data, no matter how big the data set or how deep the neural network.

While reasoning about interventions is an important step on the causal ladder, it still does not answer all questions of interest. We might wonder, My headache is gone now, but why? Was it the aspirin I took? The food I ate? The good news I heard? These queries take us to the top rung of the Ladder of Causation, the level of counterfactuals, because to answer them we must go back in time, change history, and ask, “What would have happened if I had not taken the aspirin?”

Counterfactuals have a particularly problematic relationship with data because data are, by definition, facts. They cannot tell us what will happen in a counterfactual or imaginary world where some observed facts are bluntly negated. Yet the human mind makes such explanation-seeking inferences reliably and repeatably.

The rewards of having a causal model that can answer counterfactual questions are immense. Finding out why a blunder occurred allows us to take the right corrective measures in the future. Finding out why a treatment worked on some people and not on others can lead to a new cure for a disease.

The advantage we gained from imagining counterfactuals was the same then as it is today: flexibility, the ability to reflect and improve on past actions, and, perhaps even more significant, our willingness to take responsibility for past and current actions.

However, we can answer a slightly less ambitious question: How can machines (and people) represent causal knowledge in a way that would enable them to access the necessary information swiftly, answer questions correctly, and do it with ease, as a three-year-old child can? In fact, this is the main question we address in this book.

Also, our judgment would be that B (in all likelihood) did not shoot; nothing about A’s decision should affect variables in the model that are not effects of A’s shot. This bears repeating. If we see A shoot, then we conclude that B shot too. But if A decides to shoot, or if we make A shoot, then the opposite is true.

To pass the mini-Turing test, our computer must conclude that the prisoner would be dead in the fictitious world as well, because B’s shot would have killed him. So A’s courageous change of heart would not have saved his life.

Finally, to illustrate the third rung of the Ladder of Causation, let’s pose a counterfactual question. Suppose the prisoner is lying dead on the ground. From this we can conclude (using level one) that A shot, B shot, the captain gave the signal, and the court gave the order. But what if A had decided not to shoot? Would the prisoner be alive? This question requires us to compare the real world with a fictitious and contradictory world where A didn’t shoot.

Instead of predicting whether a prisoner is alive or dead, we might want to predict how much the unemployment rate will go up if we raise the minimum wage. This kind of quantitative causal reasoning is generally beyond the power of our intuition.

One of the most intriguing features of the Causal Revolution, though, is that in many cases we can leave those mathematical details completely unspecified. Very often the structure of the diagram itself enables us to estimate all sorts of causal

and counterfactual relationships: simple or complicated, deterministic or probabilistic, linear or nonlinear.

Probabilities, as given by expressions like P(Y | X), lie on the first rung of the Ladder of Causation and cannot ever (by themselves) answer queries on the second or third rung. Any attempt to “define” causation in terms of seemingly simpler, first-rung concepts must fail.

The main point is this: while probabilities encode our beliefs about a static world, causality tells us whether and how probabilities change when the world changes, be it by intervention or by act of imagination.

