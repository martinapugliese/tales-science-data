# Polynomial Regression

A polynomial regression wants to model a non-linear, polynomial relationship within the data. It can be just reduced to a linear regression via variable substitution, reducing the features to linear ones. A generic polynomial model is

$$
y(x) = \sum_{i=0}^{i=m}a_i x^i = a_0 + a_1x + a_2x^2 + \ldots + a_mx^m
$$

The problem can be reduced to that of a multiple linear regression where the features are the polynomials of$$x$$:

$$
\begin{cases}
    x_1 = x \\
    x_2 = x^2 \\
    \ldots \\
    x_m = x^m
\end{cases}
$$

so that the model is linear in all of these new features.

The same applies to non-polynomial features, say exponentials or other functions.

