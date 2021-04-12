# The Maximum Likelihood, Maximum a Posteriori and Expectation-maximisation estimation methods

## The Likelihood

Imagine you have a statistical model, that is, a mathematical description of your data which depends on some parameters$$\theta$$. The _likelihood function_, usually indicated as$$\mathcal L$$, is a function of these parameters and represents the probability of observing evidence \(observed data\) $$E$$ given said parameters:

$$
\mathcal{L} = P(E \ | \  \theta)
$$

Because it is a function of the parameters given the outcome, you write

$$
\mathcal{L}(\theta \  | \ E) = P(E \ | \  \theta)
$$

The difference between _probability_ and _likelihood_ is quite subtle in that in common language they are be casually swapped, but they represent different things. The probability measures the outcomes observed as a function of the parameters $$\theta$$ of the underlying model. But in reality $$\theta$$ are unknown and in fact, we go through the reverse process: estimating the parameters given the evidence we observe. For this, we use the likelihood, which is defined as above because we maximise it in such a way to respond to the equality above. This is exactly what the ML estimation does, as per below.

Bear in mind that the likelihood is a function of $$\theta$$.

## The MLE method

The _Maximum Likelihood Estimation_ \(MLE\) is a procedure to find the parameters of a statistical model via the maximisation of the likelihood so as to maximise the agreement between the model and the observed data.

The maximisation of the likelihood is usually performed via the maximisation of its logarithm as it is much more convenient; the logarithm is a monotonic function so the procedure is legit.

### Example: a Bernoulli distribution

Refer to the page about distributions 

{% page-ref page="../foundational-concepts-on-distribution-and-measures/some-of-the-most-famous-distributions.md" %}

The likelihood function for a Bernoulli distribution \( $$x_i \in {0, 1}$$ \) is, for parameter $$p$$ :

$$
\begin{align} \mathcal{L}(x_1, x_2, \ldots, x_n  |  p) &= P(X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n  |  p) \\ &= p^{x_1}(1-p)^{1-x_1} \cdot \ldots \cdot p^{x_n}(1-p)^{1-x_n} \\ &= p^{\sum_i x_i}(1-p)^{\sum_i(1-x_i)} \\ &= p^{\sum_i x_i}(1-p)^{n -\sum_i x_i} \end{align}
$$

so that if we take the logarithm, we get

$$
\log \mathcal{L} = \sum_i x_i \log p + \Big(n - \sum_i x_i\Big) \log (1-p) \ .
$$

To maximise it, we compute and nullify the first derivative

$$
\frac{d \log \mathcal{L}}{d p} = \frac{\sum_i x_i}{p} - \frac{n - \sum_i x_i}{1-p} = 0
$$

which leads to

$$
\sum_i x_i - p \sum_i x_i = np - p \sum_i x_i
$$

and finally to

$$
p = \frac{\sum_i x_i}{n}
$$

### Example: estimating the best mean of some data

This example is reported from [here](the-maximum-likelihood-maximum-a-posteriori-and-expectation-maximisation-estimation-methods.md#references). Let us assume we know the weights of women are normally distributed with a mean $$\mu$$ and standard deviation $$\sigma$$. A random sample of 10 women gives measurements \(in pounds\):

$$
115, 122, 130, 124, 149, 160, 152, 138, 149, 180
$$

We want to estimate $$\mu$$ . We know

$$
P(x_i ; \mu, \sigma) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{- \frac{(x_i - \mu)^2}{2 \sigma^2}}
$$

The likelihood is \(note that the $$X_i$$ are independent\)

$$
\begin{align} \mathcal{L}(x_i | \mu, \sigma) &= P(X_1=x_1, \ldots, X_n=x_n) \\ &= \Pi_i p(x_i; \mu \sigma) \\ &= \sigma^n (2 \pi)^{-n/2} e^{- \frac{1}{2 \sigma^2} \sum_i (x_i - \mu)^2} \end{align}
$$

Now, again it is easier to work with the logarithm:

$$
\log \mathcal{L} = -n \log \sigma \frac{n}{2} \log 2 \pi - \frac{1}{2 \sigma^2} \sum_i (x_i - \mu)^2
$$

so that

$$
\frac{d \log \mathcal{L}}{d \mu} = -\frac{1}{2 \sigma^2} 2 \sum_i (x_i - \mu) = 0
$$

$$
\sum_i x_i - n \mu = 0
$$

$$
\mu = \frac{\sum_i x_i}{n}
$$

and so the maximum likelihood estimate for a given sample is 142.2 and we can could do the same to estimate $$\sigma$$ , obtaining \(can be proven through second derivative that it is a maximum\)

$$
\sigma^2 = \frac{\sum_i (x_i - \mu)^2}{n}
$$

## The MAP method

This _Maximum a Posteriori_ \(MAP\) estimation method uses the mode of the posterior to estimate the unknown population.

From Bayes' theorem, the posterior is expressed as

$$
P(\theta \ | \ x) = \frac{P(x \ | \ \theta) P(\theta)}{\int d \theta' P(x \ | \ \theta') P(\theta')} \ ,
$$

with $$\theta$$ being the parameters of the statistical model and $$x$$ the observed data. The MAP method estimates $$\theta$$ as the one which maximises the posterior; note that the denominator is just a normalisation factor:

$$
\hat{\theta}_{MAP}(x) = arg \max_\theta P(\theta \  | \  x) = arg \max_\theta P(x \ | \ \theta) P(\theta) \ .
$$

This means exactly taking the mode of the posterior distribution.

In the case of a uniform prior, the MAP estimation is equal to the ML estimation as we get to maximise the likelihood because the prior becomes just a factor. For the computation, conjugate priors are particularly handy.

As in the case of the MLE, what we really do is maximising the logarithm of the posterior rather than the posterior itself, so we do

$$
\hat \theta_{MAP}(x) = arg \max_{\theta} \log P(\theta \ | \ x) = arg \max_{\theta} [\log P(x \ | \ \theta) + \log P(\theta)] \ .
$$

## MAP and ML

In the last equation, if we only had the first term to maximise, we would be doing a ML estimation. The second term is the one accounting for the presence of a prior: this is why the MAP method is considered as a regularised ML as prior knowledge is factored in the computation.

While the ML method can be seen as responding to a frequentist approach, the MAP method responds to a Bayesian approach.

## The Expectation-Maximisation algorithm

The EM algorithm can be used to find the solution of MLE or MAP when some data is missing, meaning there are some latent variables not observed.

Let's say that for the random variable $$x$$ we have the $$n$$ observations

$$
x_1, \ldots, x_n \ ,
$$

which depend on parameters $$\theta$$ , and that the goal is to find the parameter $$\theta$$ that maximises the likelihood which is of the form

$$
L = \sum_z P_\theta(x, z) \ ,
$$

meaning it is a sum over the latent variables $$z$$ ; this makes the problem difficult to solve analytically.

The EM algorithm updates the parameters in steps, which means it risks obtaining a local rather than a global maximum.

### The E step

In the E phase \(time $$t$$ \), the expected value of $$L$$ is computed with respect to the conditional distribution of $$z$$ given $$x$$ under the current estimate of parameters $$\theta$$ :

$$
\bar L(\theta | \theta^t) = \mathbb E_{z | x, \theta^t} [\log L (\theta, x)]
$$

This means that the log-likelihood is evaluated using the current state of the parameters.

### The M step

In the M phase \(time $$t+1$$ \), we find the parameters which maximises the log-likelihood found in the E step:

$$
\theta^{t+1} = arg \max_{\theta} \bar L(\theta | \theta^t)
$$

## References

1. Some [examples](https://online.stat.psu.edu/stat414/node/191/) about MLE in this course from PennState
2. [Cross Validated](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability) on the difference between Probability and Likelihood
3. An [assignment](http://www.cs.cmu.edu/~aarti/Class/10601/homeworks/hw2Solutions.pdf) on the method from Carnegie Mellon

