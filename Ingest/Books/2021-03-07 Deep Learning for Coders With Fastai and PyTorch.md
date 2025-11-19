---
author: Jeremy Howard
category: books
source: ibooks
date: 2025-11-18
URL:
---
Jeremy Howard #ibooks

## Highlights
Harvard professor David Perkins, who wrote Making Learning Whole (Jossey-Bass), has much to say about teaching. The basic idea is to teach the whole game. That means that if you’re teaching baseball, you first take people to a baseball game or get them to play it. You don’t teach them how to wind twine to make a baseball from scratch, the physics of a parabola, or the coefficient of friction of a ball on a bat.

In deep learning, it really helps if you have the motivation to fix your model to get it to do better. That’s when you start learning the relevant theory. But you need to have the model in the first place.

The hardest part of deep learning is artisanal: how do you know if you’ve got enough data, whether it is in the right format, if your model is training properly, and, if it’s not, what you should do about it? That is why we believe in learning by doing.

As with basic data science skills, with deep learning you get better only through practical experience. Trying to spend too much time on the theory can be counterproductive. The key is to just code and try to solve problems: the theory can come later, when you have context and motivation.
    - Tags: [[blue]] 

We strongly believe that the focus in learning needs to be on understanding the underlying techniques and how to apply them in practice, and how to quickly build expertise in new tools and techniques as they are released.

Many accurate models are of no use to anyone, and many inaccurate models are highly useful. To ensure that your modeling work is useful in practice, you need to consider how your work will be used.

After cleaning the dataset using these steps, we generally are seeing 100% accuracy on this task. We even see that result when we download a lot fewer images than the 150 per class we’re using here. As you can see, the common complaint that you need massive amounts of data to do deep learning can be a very long way from the truth!

The Verge investigated software used in over half of the US states to determine how much healthcare people receive, and documented its findings in the article “What Happens When an Algorithm Cuts Your Healthcare”. After implementation of the algorithm in Arkansas, hundreds of people (many with severe disabilities) had their healthcare drastically cut.

As data scientists, we’re naturally inclined to focus on making our models better by optimizing some metric or other. But optimizing that metric may not lead to better outcomes. And even if it does help create better outcomes, it almost certainly won’t be the only thing that matters.

Now, as you are collecting your data and developing your model, you are making lots of decisions. What level of aggregation will you store your data at? What loss function should you use? What validation and training sets should you use? Should you focus on simplicity of implementation, speed of inference, or accuracy of the model? How will your model handle out-of-domain data items? Can it be fine-tuned, or must it be retrained from scratch over time?
These are not just algorithm questions. They are data product design questions. But the product managers, executives, judges, journalists, doctors—whoever ends up developing and using the system of which your model is a part—will not be well-placed to understand the decisions that you made, let alone change them.

They described how they used an algorithm that made recommendations such that watch time would be optimized.
However, human beings tend to be drawn to controversial content. This meant that videos about things like conspiracy theories started to get recommended more and more by the recommendation system. Furthermore, it turns out that the kinds of people who are interested in conspiracy theories are also people who watch a lot of online videos! So, they started to get drawn more and more toward YouTube.

No one at Google planned to create a system that turned family videos into porn for pedophiles. So what happened?
Part of the problem here is the centrality of metrics in driving a financially important system. When an algorithm has a metric to optimize, as you have seen, it will do everything it can to optimize that number. This tends to lead to all kinds of edge cases, and humans interacting with a system will search for, find, and exploit these edge cases and feedback loops for their advantage.

One important signal to classify the main topic of a video is the channel it comes from. For example, a video uploaded to a cooking channel is very likely to be a cooking video. But how do we know what topic a channel is about? Well…in part by looking at the topics of the videos it contains! Do you see the loop?

One way to break this feedback loop is to classify videos with and without the channel signal. Then when classifying the channels, you can only use the classes obtained without the channel signal. This way, the feedback loop is broken.

Taking gender into account could therefore cause Meetup’s algorithm to recommend fewer tech meetups to women, and as a result, fewer women would find out about and attend tech meetups, which could cause the algorithm to suggest even fewer tech meetups to women, and so on in a self-reinforcing feedback loop.

So, Evan and his team made the ethical decision for their recommendation algorithm to not create such a feedback loop, by explicitly not using gender for that part of their model. It is encouraging to see a company not just unthinkingly optimize a metric, but consider its impact.
    - Tags: [[blue]] 

Historical bias comes from the fact that people are biased, processes are biased, and society is biased. Suresh and Guttag say: “Historical bias is a fundamental, structural issue with the first step of the data generation process and can exist even given perfect sampling and feature selection.”

IBM’s system, for instance, had a 34.7% error rate for darker females, versus 0.3% for lighter males—over 100 times more errors! Some people incorrectly reacted to these experiments by claiming that the difference was simply because darker skin is harder for computers to recognize.

We also see this kind of bias in online advertisements. For instance, a study in 2019 by Muhammad Ali et al. found that even when the person placing the ad does not intentionally discriminate, Facebook will show ads to very different audiences based on race and gender. Housing ads with the same text but picturing either a white or a Black family were shown to racially different audiences.

What we’ve measured is who had symptoms, went to a doctor, got the appropriate tests, and received a diagnosis of stroke. Actually having a stroke is not the only thing correlated with this complete list—it’s also correlated with being the kind of person who goes to the doctor

This is an example of measurement bias. It occurs when our models make mistakes because we are measuring the wrong thing, or measuring it in the wrong way, or incorporating that measurement into the model inappropriately.

it turns out that diabetes patients have different complications across ethnicities, and HbA1c levels (widely used to diagnose and monitor diabetes) differ in complex ways across ethnicities and genders. This can result in people being misdiagnosed or incorrectly treated because medical decisions are based on a model that does not include these important variables and interactions.

In other words, the researchers noticed that models predicting occupation did not only reflect the actual gender imbalance in the underlying population, but amplified it! This type of representation bias is quite common, particularly for simple models. When there is a clear, easy-to-see underlying relationship, a simple model will often assume that this relationship holds all the time.

For example, in the training dataset 14.6% of surgeons were women, yet in the model predictions only 11.6% of the true positives were women. The model is thus amplifying the bias existing in the training set.

As the Arkansas healthcare example showed, machine learning is often implemented in practice not because it leads to better outcomes, but because it is cheaper and more efficient. Cathy O’Neill, in her book Weapons of Math Destruction (Crown), described a pattern in which the privileged are processed by people, whereas the poor are processed by algorithms.

