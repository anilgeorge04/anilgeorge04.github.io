---
title: "Data Skeptic: Correlation does not imply Causation"
excerpt: "A mantra to deeply ingrain the data skeptic mindset"
header:
    teaser: /assets/images/pinterest-correlation.jpg
tags:
    - metrics
    - insights
    - decision making
---
{% include figure image_path="/assets/images/pinterest-correlation.jpg" alt="Correlation all who eat chicken go to the moon" caption="Source: [Pinterest](https://www.pinterest.co.uk/pin/312296555380025188)" %}

>"CORRELATION DOES NOT IMPLY CAUSATION"

Anyone who's taken any Statistics class ever has heard this more than once.

When I joined the field of Data Science ~10 years ago, we fresh hires went through an intensive training program (Mu Sigma University). Here, this phrase was the first choice of greeting for all instructors. The freshers would respond "In p-value we place our confidence". 

Okay, I am exaggerating a little because it sounded funny in my head. But this was the undertone in most conversations to drill in a *Data Skeptic* mindset into the budding Data Scientists (or [Decision Scientists](https://www.mu-sigma.com/our-people/data-analytical-companies-decision-scientists) as Mu Sigma called it).

As humans, we look for patterns to make sense of things around us. We also tend to look for a cause and effect relationship in these patterns. So, it is quite natural to conflate correlation with causation to simplify our understanding.

#### What is Correlation?
**Correlation** is any statistical relationship, whether causal or not, between two random variables. It refers to the degree to which a pair of variables are linearly related. Think of this quantified relation as ranging from -1 (strong negative correlation) to +1 (strong positive correlation). Values closer to 0 suggest next to no correlation. A correlation of +1 is suspect because both the variables are behaving as a proxy for one another.

Correlation is useful in suggesting a *likely* predictive relationship between two variables. But, this is not sufficient to guarantee a causal nature. For example, the price of good A might have a strong positive correlation with price of good B. But, it is premature to suggest that one causes the other without validating this hypothesis. Are they complementary goods that influence the price of each other? Are they standalone events that are being caused by different factors altogether?

<div class="notice--info">
    Did the <a href="https://en.wikipedia.org/wiki/File%3aPiratesVsTemp%28en%29.svg">Pirates cause global warming?</a>
    {% include figure image_path="https://upload.wikimedia.org/wikipedia/commons/d/de/PiratesVsTemp%28en%29.svg" %}
</div>

#### So how do I get to the cause?
**Causation** in statistics refers to the *explain-ability* of one event (the 'effect') by a prior event ('the cause').

Correlation is a powerful place to start exploratory data analysis. It helps us filter out the relationships that we want to study further. There are many statistical methods used to identify causation. 

For product managers and owners looking to introduce new features, a go-to technique in your arsenal can be a simple controlled experiment or [A/B Testing](https://en.wikipedia.org/wiki/A/B_testing). This is a powerful extension of [Hypothesis Testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing). As more information and evidence becomes available, updating prior beliefs and probability for a hypothesis becomes important. Here, it helps to have a grip on [Bayesian Inference](https://en.wikipedia.org/wiki/Bayesian_inference).

While each of these statistical concepts warrant detailed lessons of their own, the core idea is to start from a hypothesis about what *caused* the outcome (*effect*). Correlation is a good leading indicator for this. Then, we go about studying the probability distribution of the data, to understand how well one variable explains the outcome.

Smoking was advertised as "healthy" for many years. That is until [this study](https://en.wikipedia.org/wiki/British_Doctors_Study) that proved a causal relationship between the two correlated events of smoking and lung cancer.

Remember that just because two events correlate, it does not necessarily mean that one causes the other. 

For the times when your pattern-matching biases blunt your skepticism,

{% include figure image_path="https://imgs.xkcd.com/comics/correlation.png" alt="Correlation does not imply causality XKCD" caption="Source: [XKCD](https://xkcd.com/552/)" %}