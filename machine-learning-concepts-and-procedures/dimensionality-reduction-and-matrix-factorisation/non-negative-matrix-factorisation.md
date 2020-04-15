# Non-negative matrix factorisation

Non-negative Matrix Factorisation, shortened as NMF, is a technique, often employed in recommender systems and in computer vision, to create an \(approximate\) factorisation of a big matrix into two sensibly smaller matrices in a way that elements are non-negative.

The explanation here is inspired by the one on [Wikipedia](non-negative-matrix-factorisation.md#references).

## What?

Let's say you have a big $$m \times n$$ matrix $$V$$ , with NMF you are able to factorise it into the product of matrices $$W$$ \( $$m \times p$$ \) and $$H$$ \($$p \times n$$ \), with the property that $$p \ll m, n$$ and $$p$$ playing the role of the _hidden features_ in the data. The typical use case is that of a big sparse matrix factorised into two smaller dense matrices, which are much easier to deal with for computations.

Often, an approximate factorisation is desired, so that in reality

$$
V \approx W H \ .
$$

In fact, $$p$$ is chosen precisely in such a way that $$WH$$ is a reasonable approximation of $$V$$ . The real full decomposition is

$$
V = WH + U \ ,
$$

where $$U$$ is the residuals matrix, whose elements can be either positive or negative.

The usual way to proceed in finding $$W$$ and $$H$$ is to use gradient descent \(see page\) by looking at minimising the difference between $$V$$and $$WH$$ with the constraint of non-negativity.

{% page-ref page="../learning-algorithms/the-gradient-descent-method.md" %}

### Some examples

Let's say we are working with text and doing some NLP on documents. We have a term-document matrix \(see page\) $$V$$, $$10^2 \times 10^5$$  and we would like to extract 10 features in order to generate a features matrix $$W$$ with $$10^4$$ rows and 10 columns and a coefficient matrix $$H$$ with 10 rows and $$10^2$$ columns. The product of $$WH$$ would then have $$10^4$$ rows and $$10^2$$ columns, working as a reasonable approximation of the original $$V$$ .

Other typical applications are those where you have the matrix of users' ratings on items \(products, movies, ...\) and you'd want to discover some $$p$$latent features.$$W$$ will give you the association of users to these hidden features and$$H$$the association of the items to these hidden features. Once obtained the factorisation, you can use it to predict the rating a given user $$u_i$$ would give to an item $$d_j$$, as

$$
V_{ij} = \sum_p w_{ip}^T h_{pj}
$$

{% page-ref page="../../term-document-matrix.md" %}

## References

1. [Wikipedia](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization) on the topic

