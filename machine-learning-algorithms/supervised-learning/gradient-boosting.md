# Gradient boosting

## What is and the idea

The gradient boosting method, sometimes called the Gradient Boosting Machine \(GBM\), like other boosting methods, combines many weak learners into one strong learner in a iterative fashion and can be used for regression or classification. The weak learner is typically chosen as a decision tree, where the name _Gradient Tree Boosting_ comes from in that case. The method works by optimising a differentiable loss function by means of gradient descent.

The goal is learn a model$$F$$that predicts

$$
\hat y = F(x)
$$

by minimising a loss function$$L$$\(can be for instance the mean squared error averaged over the training set\):

$$
L = ||\hat y - y||^2
$$

where$$y$$are the true values.

Let's say we have a total of$$M$$stages. At each stage$$1 \leq m \leq M$$, we use a weak learner$$F_m$$: an example of a \(very\) weak learner could be one that predicts the mean of all the sample points as the target.

At the following stage, the GBM improves the learner by adding an estimator$$h$$so that

$$
F_{m+1}(x) = F_m(x) + h(x)
$$

The point is how to choose the estimator$$h$$ .

A perfect$$h$$would give

$$
F_{m+1}(h) = F_m(x) + h(x) = y \Leftrightarrow h(x) = y - F_m(x)
$$

so$$h$$represents the residual. As a matter of fact, the GBM fits $$h$$ to the residual.

This way, like in other boosting methods, each learner learns to correct its predecessor.

## The Mathematics

In general, in a function space, given a training set of $$N$$ points

$$
\{(\mathbf x_1, y_1), (\mathbf x_2, y_2), \ldots, (\mathbf x_N, y_N)\} \ ,
$$

with $$\mathbf x_i = (x_i^1, x_i^2, \ldots, x_i^n)$$ a vector of $$n$$ features.

Goal: finding a$$\hat F(x)$$as the approximation of a $$F^*(x)$$ that minimises the expected value of some chosen loss function $$L(y, F(\mathbf x))$$ over the distribution of the training set values, so that

$$
F^*(x) = arg \min_F \mathbb{E}_{\mathbf x, y} [L(y, F(\mathbf x))]
$$

The problem will have to be solved by numerical optimisation. We have the functional

$$
\Phi(F) = \mathbb{E}_{\mathbf x, y} [L(y, F(\mathbf x))] \ ,
$$

which we can write as

$$
\Phi(F) = \mathbb{E}_{\mathbf x} [\phi(F(\mathbf x))]
$$

where

$$
\phi(F(\mathbf x)) = \mathbb{E}_y[L(y, F(\mathbf x)) | \mathbf x] \ .
$$

This functional of$$F$$has to be minimised over$$F$$, which is considered as a parameter. In numerical optimization, we will assume the form of the solution to be

$$
F(\mathbf x) = \sum_{m=0}^{M} f_m(\mathbf x)
$$

$$h_0$$is an initial guess and the subsequent$$f_m$$are the incremental boosts we perform at each step.

The optimisation method utilised will be the gradient descent, whereby we compute the gradient at each step as

$$
\mathbf g_m (\mathbf x) = \Big [ \frac{\partial \phi(F(\mathbf x))}{\partial F(\mathbf x)} \Big ]_{F(\mathbf x) = F_{m-1}(\mathbf x)}
$$

and$$F{m-1}(\mathbf x) = \sum{i=0}^{m-1} f_i(\mathbf x)$$.

Assuming enough regularity that derivative and integration can be exchanged, we compute

$$
\mathbf g_m(\mathbf x) = \mathbb{E}_y \Big[\frac{\partial L(y, F(\mathbf x))}{\partial F(\mathbf x)} \Big| x \Big]_{F(\mathbf x) = F_{m-1}(x)}
$$

By line-search we will have the parameter update

$$
F_m(\mathbf x) = F_{m-1}(\mathbf x) - \rho_m \mathbf g_m(\mathbf x)
$$

with

$$
\rho_m = arg \min_\rho \mathbb{E}_{y, \mathbf x} [L(y, F_{m-1}(\mathbf x)) - \rho \mathbf g_m(\mathbf x)]
$$

In practice though, we have finite data, our training set. This means that$$\phi(F(\mathbf x))$$cannot be estimated accurately by its value at each$$\mathbf x_i$$, because we'd only be using the training set to estimate it. We'd need to use other points.

This problem gets typically addressed by using a parametric form for$$F$$:

$$
F(\mathbf x, \{\beta_m, \mathbf a_m\}_1^M) = \sum_{m=1}^M \beta_m h_m(\mathbf x; \mathbf a_m)
$$

and performing parameter optimisation to minimise the training data-based approximation of the loss function, so that

$$
\{\beta_m, \mathbf a_m\}_1^M = arg \min_{ (\beta'_m, \mathbf a'_m \}_1^M } \sum_{i=1}^N L\Big(y_i, \sum_{m=1}^M \beta'_m h(\mathbf x_i; \mathbf a'_m) \Big)
$$

When this is unfeasible, a greedy approach is utilised, so that, for a given $$m$$,

$$
(\beta_m, \mathbf a_m) = arg \min_{\beta, \mathbf a} \sum_{i=1}^N L\Big(y_i, F_{m-1}(\mathbf x_i) + \beta h(\mathbf x_i, \mathbf a) \Big)
$$

and then

$$
F_m(\mathbf x) = F_{m-1}(\mathbf x) + \beta_m h(\mathbf x; \mathbf a_m)
$$

$$h(\mathbf x, \mathbf a_m)$$is the weak learned employed.

Also, we use the data-based computation of the gradient

$$
g_m(\mathbf x_i) = \Big[\frac{\partial L(y_i, F(\mathbf x_i))}{\partial F(\mathbf x_i)} \Big]_{F(\mathbf x) = F_{m-1}(\mathbf x)}
$$

and the data-based line-search update

$$
\rho_m = arg \min_\rho \sum_{i=1}^N L(y_i, F_{m-1}(\mathbf x_i) + \rho h(\mathbf x_i; \mathbf a_m))
$$

$$
F_m(\mathbf x) = F_{m-1} (x) + \rho_m h(\mathbf x; \mathbf a_m)
$$

## The Algorithmic Implementation

1. Start by initialising a constant function $$F_0(x)$$ :

   $$
   F_0(\mathbf x) = arg \min_\rho \sum_{i=1}^{N} L(y_i, \rho)
   $$

2. For$$m=1$$ to $$M$$ :
   * Compute the negative gradient for each data point $$i=1, \ldots, N$$as

     $$
     g_{mi} = - \Big[\frac{\partial L(y_i, F(\mathbf x_i))}{\partial F(\mathbf x_i)} \Big]_{F=F_{m-1}}
     $$

   * Compute the parameters from the training set as per above
   * Update the learner $$F_m$$ as above

## Choosing the loss function

### Ordinary Least Squares Regression

In the simple case of an OLS regression, the loss function is

$$
L(y, F) = \frac{1}{2}(y-F)^2 \ ,
$$

so its negative gradient with respect to $$F$$ is $$y-F$$ , that is, the residual.

The update rule computes

$$
\begin{aligned}
F_m &= F_{m-1} + h \\
    &= F_{m-1} + y - F_m \\
    &= F_{m-1} - \frac{\partial L}{\partial F_m}
\end{aligned}
$$

so it clearly appears that the update rule is that of the Gradient Descent.

## Gradient Tree Boosting

When used with a decision tree as the weak learner \(usual case\), the algorithm is called Gradient Tree Boosting.

Note that with respect with normal GB, GTB does not use the same$$\rho_m$$for the whole tree but rather a$$\rho_{mj}$$for each leaf j.

## References

1. J H Friedman, [**Greedy function approximation: a gradient boosting machine**](http://statweb.stanford.edu/~jhf/ftp/trebst.pdf), ****_Annals of Statistics_, 2001

