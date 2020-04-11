# Propagation of uncertainty

For the covariance, refer to page:

{% page-ref page="../foundational-concepts-on-distribution-and-measures/independence-joint-marginal-conditional-probability-covariance-and-correlation.md" %}

Given a function of $$n$$ non-correlated variables $$f(x_1, x_2, \ldots, x_n)$$ , such that each variable $$x_i$$ has its own uncertainty $$\Delta x_i$$ , we can compute the uncertainty on $$f$$ as

$$
\Delta f(x_1, x_2, \ldots, x_n, \Delta x_1, \ldots, \Delta x_n)  = \left[\sum_{i=1}^{i=n} \frac{\partial f}{\partial x_i} \Delta x_i\right]^{\frac{1}{2}} \ .
$$

If the variables are correlated, then there is the covariance term:

$$
\Delta f(x_1, x_2, \ldots, x_n, \Delta x_1, \ldots, \Delta x_n) = \left[\sum_{i=1}^{n} \sum_{k=1}^n \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_k} C_{ik}\right]^{1/2} \ ,
$$

where $$C_{ik}$$ is the covariance matrix.

In the most common cases:

* $$f = x \pm y \Rightarrow (\Delta f)^2 = (\Delta x)^2 + (\Delta y)^2 \pm 2 C_{xy}$$ 
* $$f = cx \Rightarrow \Delta f = c \Delta x$$ 
* $$f = xy \Rightarrow (\Delta f)^2 = y^2 (\Delta x)^2 + x^2 (\Delta y)^2 + 2 xy C_{xy}$$ 
* $$f = \frac{x}{y} \Rightarrow (\Delta f)^2 = \frac{(\Delta x)^2}{y^2} + \frac{x^2}{y^4} (\Delta y)^2 - 2 \frac{x}{y^3} C_{xy}$$ 



