---
author: CRAIG S. SMITH
category: articles
source: pocket
date: 2025-11-18
URL: https://www.nytimes.com/2019/11/19/technology/artificial-intelligence-bias.html
---
CRAIG S. SMITH #pocket

## Highlights
Another notion of bias, one that is highly relevant to my work, are cases in which an algorithm is latching onto something that is meaningless and could potentially give you very poor results. For example, imagine that you’re trying to predict fractures from X-ray images in data from multiple hospitals. If you’re not careful, the algorithm will learn to recognize which hospital generated the image. Some X-ray machines have different characteristics in the image they produce than other machines, and some hospitals have a much larger percentage of fractures than others. And so, you could actually learn to predict fractures pretty well on the data set that you were given simply by recognizing which hospital did the scan, without actually ever looking at the bone.

To recognize and address these situations, you have to make sure that you test the algorithm in a regime that is similar to how it will be used in the real world. So, if your machine-learning algorithm is one that is trained on the data from a given set of hospitals, and you will only use it in those same set of hospitals, then latching onto which hospital did the scan could well be a reasonable approach. It’s effectively letting the algorithm incorporate prior knowledge about the patient population in different hospitals.

People are starting to research methods to spot and mitigate bias in data. For categories like race and gender, the solution is to sample better such that you get a better representation in the data sets. But, you can have a balanced representation and still send very different messages. For example, women programmers are frequently depicted sitting next to a man in front of the computer, or with a man watching over her shoulder.

