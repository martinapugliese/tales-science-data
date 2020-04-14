# AdaBoost

### The gist

AdaBoost, shortening for _adaptive boosting_ is a boosting ensemble method used both in classification and in regression problems. The authors won the Goedel prize for the work in 2003, whose original paper is in the [first reference](adaboost.md#references) but a nice reading over the general idea, by the same authors is the paper in the [second reference](adaboost.md#references).

The idea is to fit a sequence of weak learners \(a weak learner is one that is just slightly better than a random guesser\) on repeatedly modified versions of the training set, then combine their predictions through a weighted majority voting system.

In the first iteration, you give the same weight to all $$n$$ training samples, $$w_i = \frac{1}{n}$$ ; in successive iterations the weights are modified in such a way that the training samples which were incorrectly predicted in the previous iteration will see their weights increased while those which were correctly predicted will see their weights decreased. This way, the weak learner is forced to focus on the points more difficult to predict: this is the adaptive part of the idea. The resulting combination of these weak learners will be a strong learner.

As per current literature, AdaBoost with decision trees is considered a pretty strong classifier.

## The algorithm

This part follows [the Wikipedia page](https://en.wikipedia.org/wiki/AdaBoost). Let's see we have a binary classification problem, class variables being $$y_i \in {1, -1}$$ and sample points$$(x_1, y_1), \ldots, (x_n, y_n)$$, where$$x_i \in X$$\(feature matrix\).

* Call a weak learner $$h$$ 
* At iteration $$t$$ , you'll have built a combination of weak learners into a strong learner

$$
H_t(x_i) = \sum_{i=1}^t \alpha_i h_i(x_i) \ ,
$$

so that

$$
H_t(x_i) = H_{t-1}(x_i) + \alpha_t h_t(x_i)
$$

This way we have built a linear combination of weak learners over several iterations. The weights $$\alpha_i$$ of each learner remain to be attributed in the most effective way. If we consider the error$$E$$on$$H_t$$ as the sum of the exponential losses on each data point,

$$
E = \sum_{i=1}^n e^{-y_i H_t(x_i)}
$$

\(note that the argument of the exponential will be a 1 if the point is well classified and a -1 if not\) which by posing $$w_i^1 = 1$$ __and __$$w_i^t = e^{-y_i H{t-1}(x_i)}$$ \( $$w_i$$ represents a weight to the error\) we can rewrite as

$$
E = \sum_{i=1}^n w_i^t e^{-y_i \alpha_t h_t(x_i)} \ .
$$

We can now split the sum between the points which are well classified and those misclassified:

$$
\begin{align}
    E &= \sum_{i: y_i = h_t(x_i)} w_i^t e^{-\alpha_t} + \sum_{i: y_i \neq h_t(x_i)} w_i^t e^{\alpha^t} \\
      &= \sum_{i=1}^n w_i^t e^{-\alpha_t} + \sum_{i: y_i \neq h_t(x_i)} w_i^t [e^\alpha_t - e^{-\alpha_t}]
\end{align}
$$

In the last expression above, the only part depending on the weak classifiers is the second sum, so the weak classifier that minimises$$E$$ is the one minimising this sum, which means the one that minimises $$\sum_{i: y_i \neq h_t(x_i)} w_i^t$$ , so the one with the lowest weighted error.

If we derive$$E$$with respect to$$\alpha_t$$, we obtain

$$
\alpha_t = \frac{1}{2} \log{\frac{\sum_{i: y_i = h_t(x_i)} w_i^t}{\sum_{i: y_i \neq h_t(x_i)} w_i^t}}
$$

Now, the weighted error rate of the weak classifiers is

$$
\epsilon_t = \frac{\sum_{i: y_i \neq h_t(x_i)} w_i^t}{\sum_{i=1}^n w_i^t} \ ,
$$

so it follows that we can write the $$\alpha_t$$ which minimises $$E$$ as

$$
\alpha_t = \frac{1}{2} \log{\frac{1-\epsilon_t}{\epsilon_t}}
$$

which is $$\frac{1}{2}$$ times the logit negative function.

To summarise then, the AdaBoost algorithm consists of

1. Choose the weak classifier which minimised the error $$E$$ 
2. Use it to compute the classifiers weighted error $$\epsilon_t$$ 
3. Use this to compute the weights $$\alpha_t$$ 
4. Use this to compute the boosted \(strong\) classifier $$H_t$$ 

Note that there exist several variants of the original AdaBoost.

## References

1. Y Freund, R E Schapire, [**A decision-theoretic generalization of on-line learning and an application to boosting**](https://www.face-rec.org/algorithms/Boosting-Ensemble/decision-theoretic_generalization.pdf)**,** _J of computer and system sciences_ 55.1, 1997
2. Y Freund, R E Schapire, [**A short introduction to boosting**](https://cseweb.ucsd.edu/~yfreund/papers/IntroToBoosting.pdf)**,** _J of Japanese Society for Artificial Intelligence_, 14\(5\), 1999

