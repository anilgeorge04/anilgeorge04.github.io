---
title: Wash your hands and save lives
excerpt: 'Why is Dr. Semmelweis known as "the saviour of mothers"?'
header:
  teaser: "https://images.unsplash.com/photo-1584265549884-cb8ea486a613?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80"
  caption: "Photo on [Unsplash](https://unsplash.com/photos/muq_ej7p9s0)"
nbviewer: https://bit.ly/3lLCaFY
mathjax: true
tags:
  - medical
  - datacamp
  - insights
---
{% include /notebooks/datacamp.html %}

The medical origins of washing hands dates back to Dr. Semmelweis in mid 19th century. He managed to bring down the mortality rate of mothers giving birth, by emphasizing the importance of *washing hands*. Let's analyze the data that made Semmelweis realize that something was wrong with the procedures at Vienna General Hospital.

## Meet Dr. Ignaz Semmelweis
<p><img style="float: left;margin:5px 15px 5px 1px" src="/assets/images/wash-your-hands_files/ignaz_semmelweis_1860.jpg"></p>
<p>This is Dr. Ignaz Semmelweis, a Hungarian physician born in 1818 and active at the Vienna General Hospital. If Dr. Semmelweis looks troubled it's probably because he was thinking about <em>childbed fever</em>: A deadly disease affecting women that just have given birth. He was thinking about it because in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth die from it. He was thinking about it because he knows the cause of childbed fever: It's the contaminated hands of the doctors delivering the babies. And they won't listen to him and <em>wash their hands</em>!</p>

Yearly births and deaths across 2 clinics:

        year  births  deaths    clinic
    0   1841    3036     237  clinic 1
    1   1842    3287     518  clinic 1
    2   1843    3060     274  clinic 1
    3   1844    3157     260  clinic 1
    4   1845    3492     241  clinic 1
    5   1846    4010     459  clinic 1
    6   1841    2442      86  clinic 2
    7   1842    2659     202  clinic 2
    8   1843    2739     164  clinic 2
    9   1844    2956      68  clinic 2
    10  1845    3241      66  clinic 2
    11  1846    3754     105  clinic 2


## The alarming number of deaths
<p>The table above shows the number of women giving birth at the two clinics at the Vienna General Hospital for the years 1841 to 1846. Giving birth was very dangerous; an <em>alarming</em> number of women died as the result of childbirth, most of them from childbed fever.</p>
<p>We see this more clearly if we look at the <em>proportion of deaths</em> out of the number of women giving birth. Let's zoom in on the proportion of deaths at Clinic 1.</p>

       year  births  deaths    clinic  proportion_deaths
    0  1841    3036     237  clinic 1           0.078063
    1  1842    3287     518  clinic 1           0.157591
    2  1843    3060     274  clinic 1           0.089542
    3  1844    3157     260  clinic 1           0.082357
    4  1845    3492     241  clinic 1           0.069015
    5  1846    4010     459  clinic 1           0.114464


## Death at the clinics
<p>If we now plot the proportion of deaths at both clinic 1 and clinic 2  we'll see a curious pattern…</p>


    Text(0, 0.5, 'Proportion deaths')

<img src="/assets/images/wash-your-hands_files/wash-your-hands_6_1.png">


## The handwashing begins
<p>Why is the proportion of deaths constantly so much higher in Clinic 1? Semmelweis saw the same pattern and was puzzled and distressed. The only difference between the clinics was that many medical students served at Clinic 1, while mostly midwife students served at Clinic 2. While the midwives only tended to the women giving birth, the medical students also spent time in the autopsy rooms examining corpses. </p>
<p>Semmelweis started to suspect that something on the corpses, spread from the hands of the medical students, caused childbed fever. So in a desperate attempt to stop the high mortality rates, he decreed: <em>Wash your hands!</em> This was an unorthodox and controversial request, nobody in Vienna knew about bacteria at this point in time. </p>
<p>Let's load in monthly data from Clinic 1 to see if the handwashing had any effect.</p>

            date  births  deaths  proportion_deaths
    0 1841-01-01     254      37           0.145669
    1 1841-02-01     239      18           0.075314
    2 1841-03-01     277      12           0.043321
    3 1841-04-01     255       4           0.015686
    4 1841-05-01     255       2           0.007843


## The effect of handwashing
<p>With the data loaded we can now look at the proportion of deaths over time.</p>


    Text(0, 0.5, 'Proportion Deaths')

<img src="/assets/images/wash-your-hands_files/wash-your-hands_10_1.png">


<p>Starting from the summer of 1847 the proportion of deaths is drastically reduced and, yes, this was when Semmelweis made handwashing obligatory. </p>


    Text(0, 0.5, 'Proportion Deaths')

<img src="/assets/images/wash-your-hands_files/wash-your-hands_12_1.png">


## More handwashing, fewer deaths?
<p>Again, the graph shows that handwashing had a huge effect. How much did it reduce the monthly proportion of deaths on average?</p>

    Change in Proportion of Deaths After Washing minus Before Washing: -8.40%


## A Bootstrap analysis of Semmelweis handwashing data
<p>It reduced the proportion of deaths by around 8 percentage points! From 10% on average to just 2% (which is still a high number by modern standards). </p>
<p>To get a feeling for the uncertainty around how much handwashing reduces mortalities we could look at a confidence interval (here calculated using the bootstrap method).</p>

    95% Confidence Interval:

    0.025   -0.100916
    0.975   -0.066943



## The fate of Dr. Semmelweis and his theory
<p>So handwashing reduced the proportion of deaths by between 6.7 and 10 percentage points, according to a 95% confidence interval. All in all, it would seem that Semmelweis had solid evidence that handwashing was a simple but highly effective procedure that could save many lives.</p>
<p>The tragedy is that, despite the evidence, Semmelweis' theory — that childbed fever was caused by some "substance" (what we today know as <em>bacteria</em>) from autopsy room corpses — was ridiculed by contemporary scientists. The medical community largely rejected his discovery and in 1849 he was forced to leave the Vienna General Hospital for good.</p>
<p>Statistics and statistical arguments were uncommon in medical science in the 1800s. His practice earned widespread acceptance only years after his death.</p> 
<p>Dr. Semmelweis is described even today as "the saviour of mothers".</p>

{% include /notebooks/nbviewer.html %}