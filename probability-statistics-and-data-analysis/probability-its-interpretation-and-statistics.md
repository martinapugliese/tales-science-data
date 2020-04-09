# Probability, its interpretation, and Statistics

_Just an introduction over the main concepts: what are probability and statistics?_ 

## Some terminology

Given a _random variable_ $$x$$ which can take values in space $$\Omega $$ \(the _events space_\). An _event_ is the occurrence of one of the values allowed for $$x$$ and its probability gives the mathematical measure of how likely the event is to occur. It is given as a number between 0 and 1 \(extremes included\), where 0 means that the event does not occur at all and 1 that is occurs with certainty.

The _probability_ of an event gives the mathematical measure of how likely it is to occur. It is given as a number between 0 and 1, extremes included, where 1 means that the the event occurs with certainty.

For example, in the throws of a \(fair\), the space of events is given by all the faces that the dice can take when thrown \(there's 6 of them\) and we if we measure the probability of each event we find $$\frac{1}{6}$$ .

## The two interpretations of probability

### Frequentist

In the _frequentist_ approach, the probability is given as the simple ratio of events to the total outcomes the variable can take, that is, as the frequency of the occurrence of event to trials. This assumes a sufficiently large \(?\) number of trials in the first place and assumes that this frequency will asymptotically converge to the probability of our event when said number of trials goes to $$\infty$$ .

Also note that this approach inherently entails the concept of repeatability of the process \(experiment\). 

### Bayesian

In the _Bayesian_ interpretation, the probability measures a degree of belief. The [Bayes' theorem](the-bayes-theorem.md) links the degree of belief in a proposition before and after accounting for the evidence, that is, the result of the data observation. In some sense, this interpretation is nearer to the layman's one: the probability encompasses the belief in something, the prior knowledge of the phenomenon at hand.

An example illustrating the difference in the two approaches, carried out using a coin flip, can be found in [this blog](probability-its-interpretation-and-statistics.md#references). A really good read. 

## Statistics

Statistics is that branch of Mathematics dealing with the analysis of data, the testing of the reliability of experimental results and the building of models which can describe patterns and trends in the observations.

### Descriptive and inferential Statistics

_Descriptive_ _Statistics_ describes the main features of a collection of data quantitatively, that is, describes a sample without learning anything about the underlying population. It does not make use of probability theory.

_Inferential_ _Statistics_ learns from a sample of data in order to infer about the population.

## Odds and probability

The _probability_ expresses the fraction of the successes over the total \(we are using a frequentist interpretation\) and is a number between 0 and 1. The _odds_ of something quantify the fraction of successes to the failures instead and is a concept mostly used in the context of gambling.

If you have possible events $$e_1, \ldots, e_n$$, the probability of one of them $$P(e_x)$$ occurring \(the bars indicate the cardinality of the set of occurrences of the event\) can be written as

$$
P(e_x) = \frac{|e_x|}{\sum_{i=1}^n |e_x|}
$$

while the _odds in favour_ are defined as

$$
o(e_x) = \frac{|e_x|}{\sum_{i=1, i \neq x}^n |e_x|} ,
$$

that is, as the fraction of occurrences of event to all occurrences of all other events. _The odds against_ are defined as the reciprocal:

$$
o(\neg e_x) = \frac{\sum_{i=1, i \neq x}^n |e_x|}{|e_x|}
$$

In most cases, odds are reported in notation as $$e_x: \sum_{i=1, i \neq x}^n |e_x|$$ \(successes : failures\) rather than as a ratio, or, very often as $$p: 1-p$$where $$p$$ is the probability of success, or as $$\frac{p}{1-p} : \frac{1-p}{p}$$.

#### An example: coin flip

In a \(fair\) coin flip, the odds in favour of a head are 1:1, where the notation uses the third way outlined above.

## References <a id="references"></a>

1. [ **Behind the enemy lines** has a brilliant example on the difference between the two interpretations](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html)

