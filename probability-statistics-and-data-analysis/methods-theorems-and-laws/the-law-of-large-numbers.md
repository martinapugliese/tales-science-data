# The law of large numbers

In short, the law of large numbers states that the sample mean of a series of random variables will be closer and closer to the expected value of the distribution where the variables are extracted from, the higher the number of these variables.

It exists \(mathematically speaking\) in two forms, of which the strong implies the weak; the strong form being subject to more hypotheses. We will not report on the hypotheses nor the proof, we will just give the general idea.

## Weak form

In its weak form, the law of large numbers refers to a convergence in probability, stating that

$$
\lim_{n \to \infty} P(|\bar x_n - \mu| > \epsilon) = 0
$$

where $\bar x\_n$ is the sample mean of $n$ random variables and $\mu$ the expected value of their distribution. What this means is that there is a chance the two means are not near as the vicinity is in probability.

## Strong form

The strong form refers to an almost sure convergence and states that

$$
P(\lim_{n \to \infty} \bar x_n = \mu) = 1
$$

What this means is that the sample mean of $$n$$ values $$\hat x$$ is almost surely near the expected value of the distribution $$\mu$$ , or, better stated, for a large enough $$n$$ we have

$$
\forall \epsilon > 0 \ \ |\bar x_n - \mu| < \epsilon \ .
$$

## References

1. The [Wikipedia](https://en.wikipedia.org/wiki/Law_of_large_numbers) page is pretty good

