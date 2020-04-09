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

## References <a id="references"></a>

1. [ **Behind the enemy lines** has a brilliant example on the difference between the two interpretations](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html)

