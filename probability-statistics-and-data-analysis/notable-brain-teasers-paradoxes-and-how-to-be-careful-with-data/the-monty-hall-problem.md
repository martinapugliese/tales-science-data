# The Monty Hall problem

Monty Hall was the presenter of an American TV show which popularised this tricky brain teaser. The original problem, a probability brain teaser, was posed in a letter to the American Statistician in 1975; M vos Savant solved the problem in a letter to readers in her column in 1990, initially receiving harsh criticism.

\_\_![](../../.gitbook/assets/montyhall.png) _You are given a choice of three doors: behind one there is a car and behind the others there are goats._

_The host knows what's behind each door. Let's say you pick door A. The host then opens door C which shows a goat. He then gives you the option to change your decision. The question is: is it advantageous to switch your choice from A to B?_

Intuitively one would say that it makes no difference as the probability of the car being behind each door is 1/3 for each door, but actually this is wrong. A bayesian approach, which makes us change our knowledge after accounting for the evidence, is the way to go. See the page about the Bayes' Theorem.

{% page-ref page="../methods-theorems-and-laws/the-bayes-theorem.md" %}

Let's call $$H_n$$ the event of the host opening door $$n$$ , $$C_n$$ that of can being behind door $$n$$ .

The priors are

$$
P(C_n) = 1/3 \ \forall n
$$

We have to compute

$$
P(C_A | H_B) = \frac{P(H_B | C_A) P(C_A)}{P(H_B}
$$

where

$$
P(H_B) = \sum_n P(H_B| C_n) P(C_n)
$$

Now, we have

$$
P(H_B| C_A) = P(H_C|C_A) = 1/2 \ ,
$$

because if the car is in A the host would open either of B and C with equal probability. For similar reasons, we have

$$
P(H_B|C_B) = 0
$$

and

$$
P(H_B|C_C) = 1
$$

\(because you chose A\).

Plus, in our case,

$$
\begin{aligned}
    P(H_B) &= P(H_B|C_A) P(C_A) + P(H_B|C_B)P(C_B) + P(H_B|C_C)P(C_C) \\
           &= \frac{1}{3}\Big(\frac{1}{2} + 0 + 1\Big) = \frac{1}{2} \ ,
\end{aligned}
$$

so

$$
P(C_A|H_B) = \frac{1}{3}
$$

On the flip side, following a similar reasoning,

$$
P(C_C|H_B) = \frac{2}{3} \ ,
$$

which means it is convenient to switch the choice to door C.

## References

1. M vos Savant on the [problem](http://marilynvossavant.com/game-show-problem/)



