# Using aggregated metrics well

_Sometimes the wrong metric is used, sometimes the language is too sloppy. For the description of the things described in this page, head over to this page:_

{% page-ref page="../foundational-concepts-on-distribution-and-measures/" %}

## When people talk average

Technically speaking, an average is a mean.

But.

The word _average_ in common \(street\) English is usually used to mean \(oh, the irony!\) an aggregated number which is supposed to represent a collection of data points as its "central" value. We're talking about common talk, not the one among professionals of data, and this often happens in politics and \(sloppy\) journalism, with consequences that can go from funny to disastrous. This aggregated number, the _average_ is not necessarily calculated as the \(arithmetic\) mean, and this can lead to awkward situations where people don't know what they're exactly talking about and whether that number is really representative of their data. Sometimes they mean the mean, sometimes they mean the median, for one. But they can mean other different things as well: an example is when to derive the "average" value of a set of fractions, you compute the [mediant](https://en.wikipedia.org/wiki/Mediant_%28mathematics) instead of averaging said fractions. Some other times, the mode is intended when people talk about an average.

I find this one of the interesting peculiarities of the English language, and it wouldn't really matter if it weren't for the fact that in many occasions it is quite necessary to go look at a properly defined metric in order to understand what the data says. See the lovely lil' book [**How to lie with Statistics**](using-aggregated-metrics-well.md#references), which is very old but a nice read. Also, this discussion on [Quora](using-aggregated-metrics-well.md#references) is interesting.

## Is the mean always the best descriptor of a distribution?

If you have data distributed in a gaussian way, a good descriptor of the typical situation of your data is the mean. If the distribution is skewed though, and in particular in the case of power laws, the median is a much better indicator to represent the distribution. Have a look at this [video](using-aggregated-metrics-well.md#references) on the matter.

The mean is very sensible to outliers in this cases as when you add a data point , the median is not so it's a much more robust statistic to represent the distribution.

About the power-law, head here:

{% page-ref page="../foundational-concepts-on-distribution-and-measures/some-of-the-most-famous-distributions.md" %}

## References

1. D Huff, **How to lie with Statistics**, _W W Norton & Company_, 1954
2. [Quora](https://www.quora.com/What-is-difference-between-the-mean-and-the-average) on mean and average
3. [Calling Bullshit](https://www.youtube.com/watch?v=mc-6-v2c4WM) on mean & median
4. A nice [example](http://www.conceptstew.co.uk/pages/mean_or_median.html) of when using a mean is a misuse of statistics: income distributions

