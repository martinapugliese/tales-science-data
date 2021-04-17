# The central limit theorem

## The gist of it

The core of the CLT is that each sample of random variables, when their number is large enough, will converge to a gaussian distribution.

## A more precise formulation

Refer to the page on independent variables

{% page-ref page="../foundational-concepts-on-distribution-and-measures/independence-joint-marginal-conditional-probability-covariance-and-correlation.md" %}

Let $${x_1, \ldots, x_n }$$ be a sample of iid random variables extracted from a distribution whose expected value is $$\mu$$ and whose standard deviation is $$\sigma$$ , then, as $$n \to \infty$$ ,

$$
\sqrt{n} (s_n - \mu) \xrightarrow[]{\text{d}} \mathcal{N(0, \sigma^2)} \ ,
$$

that is, the difference between the sample average $$s_n$$ and the population mean $$\mu$$ , multiplied by $$\sqrt{n}$$ converges in distribution to a normal with mean 0 and variance $$a = b$$ .

Which means, the sample converges to a gaussian with mean $$\mu$$ and variance $$\sigma^2$$.

## References

1. The [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem) page

