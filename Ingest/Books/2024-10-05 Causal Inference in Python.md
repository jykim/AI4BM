---
author: Matheus Facure
category: books
source: ibooks
date: 2025-11-18
URL:
---
Matheus Facure #ibooks

## Highlights
If you take a deeper look at the types of questions you want to answer with causal inference, you will see they are mostly of the “what if” type. I’m sorry to be the one that says it, but machine learning (ML) is just awful at those types of questions.
ML is very good at answering prediction questions. As Ajay Agrawal, Joshua Gans, and Avi Goldfarb put it in the book Prediction Machines (Harvard Business Review Press), “the new wave of artificial intelligence does not actually bring us intelligence but instead a critical component of intelligence—prediction.”

To give another example from Prediction Machines, “in many industries, low prices are associated with low sales. For example, in the hotel industry, prices are low outside the tourist season, and prices are high when demand is highest and hotels are full. Given that data, a naive prediction might suggest that increasing the price would lead to more rooms sold.”

Or, more intuitively, it can be viewed as how much you should expect default to change, given a small increase in credit limit, while holding fixed all other variables in the model. This interpretation already tells you a bit of how regression adjusts for confounders: it holds them fixed while estimating the relationship between the treatment and the outcome.

FWL-style orthogonalization is the first major debiasing technique you have at your disposal. It’s a simple yet powerful way to make nonexperimental data look as if the treatment has been randomized. FWL is mostly about linear regression; FWL-style orthogonalization has been expanded to work in more general contexts, as you’ll see in Part III.

Not surprisingly, this is just a restatement of the formula you just saw in “Multivariate Linear Regression”. The FWL theorem states an equivalence in estimation procedures with regression models. It also says that you can isolate the debiasing component of linear regression, which is the first step outlined in the preceding list.

