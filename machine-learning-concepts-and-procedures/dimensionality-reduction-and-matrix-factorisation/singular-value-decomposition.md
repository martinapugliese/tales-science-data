# Singular Value Decomposition

## What is

A singular-value decomposition \(SVD\) of a high-dimensional matrix gives a low-dimensional representation of it. Given a matrix$$M$$, an $$m \times n$$ matrix of rank $$r$$, we can find matrices $$U$$, $$\Sigma$$ and $$V$$ such that we have the decomposition $$M = U \Sigma V^t$$ . These matrices respect conditions:

1. $$U$$ is an $$m \times r$$ matrix and is column orthonormal \(each column is a unit vector and the dot product of any two columns is 0\);
2. $$V$$ is a $$n \times r$$ matrix, also column orthonormal; 
3. $$\Sigma$$ is a diagonal matrix and the elements on its diagonal are called the _singular values_ of $$M$$.

$$U$$, $$\Sigma$$ and $$V$$ are called the SVD components of $$M$$. The singular values represent "hidden concepts" which connect the two other matrices together. SVD is often employed in recommender systems.

### A small example, in words

If $$M$$contains the ratings given by people to movies, so that people are on the rows and movies on the columns, then $$U$$connects people to concepts; $$V$$connects movies to concepts and $$\Sigma$$ gives the strength of each concept.

A person not represented in$$M$$wants to know what movies he/she would like based on the ones he/she has seen. If $$q$$ is the vector representing the movies the person rated, $$q V$$maps the person to the concept space and this can be mapped back to the movie space by multiplying by $$V^t$$ .

To find similar users to a given user, we can map all users to the concept space using $$V$$and then apply some similarity.

## Where is the dimensionality Reduction part

If $$M$$is a very large matrix, its SVD components will be large as well. But in real-world uses of the technique, approximate decompositions are employed instead, so to reduce the original dimensionality.

Setting the $$s$$ smallest singular values to 0 and eliminating the corresponding $$s$$rows of $$U$$ and $$V$$ we obtain an approximate representation. This procedure works well because it can be shown that it minimises the root mean square error between $$M$$ and its approximation, or the Frobenius norm of this difference.

Let $$M = PQR$$be a generic decomposition, then $$m{ij} = \sum_k \sum_l p{ik} q{kl} r{lj}$$ and then

$$
\begin{cases}
||M||^2 &= \sum_i \sum_j m_{ij}^2 \\
&= \sum_i \sum_j (\sum_k \sum_l p_{ik} q_{kl} r_{lj})^2 \\
&= \sum_i \sum_j \sum_k \sum_l \sum_n \sum_m p_{ik} q{kl} r_{lj} p_{in} q_{nm} r_{mj}
\end{cases}
$$

Now, if $$P$$, $$Q$$ and $$R$$ are the SVD components of $$M$$ , then it means $$Q$$ is diagonal, $$P$$ is column orthonormal, $$R$$ is row orthonormal \(note the transpose in the SVD equation\), so $$||M||^2 = \sum_k q{kk}^2$$.

Calling $$P = U$$, $$Q=\Sigma$$ and $$R=V^t$$, with $$\sigma_i$$ being the $$i$$-th diagonal element of $$\Sigma$$ , if we keep the first $$n$$ elements of $$\Sigma$$and set the remaining ones to 0, obtaining a $$\Sigma'$$ , we get

$$
M' = U \Sigma' V^t \ ,
$$

which is an approximation of $$M$$ . The matrix giving the resulting errors is $$M - M' = U (\Sigma - \Sigma') V^t$$ , whose norm is \(following from the above\)

$$
||M - M'||^2 = \sum_k (\Sigma - \Sigma')_{kk}^2
$$

The matrix $$\Sigma - \Sigma'$$ has 0 in the first $$\Sigma - \Sigma'$$ diagonal elements and $$\sigma_i$$ in the remaining ones, with $$n < i \leq r$$. So, $$||M - M'||^2$$ is the sum of the squares of the elements of $$\Sigma$$ which were set to 0. In order to minimise it, we pick the smallest elements of $$\Sigma$$.

## Computing the SVD of a matrix

The computation is strictly connected to the eigenvalues of the symmetric matrix $$M^tM$$ and $$M M^t$$.

If $$M = U \Sigma V^t$$, then $$M^t = V \Sigma^t U^t$$ and because $$\Sigma$$ is diagonal, then $$\Sigma = \Sigma^t$$, so $$M^t = V \Sigma U^t$$ , which then means \(using the orthonormality of $$U$$ and $$V$$\)

$$
M^t M = V \Sigma U^t U \Sigma V^t = V \Sigma^2 V^t
$$

so

$$
M^t M V = V \Sigma^2
$$

Now, $$\Sigma^2$$is diagonal, with entries being the squares of the $$\Sigma$$'s entries. This last equation says that $$V$$is the matrix of eigenvectors of $$M^tM$$ and $$\Sigma^2$$is the matrix of eigenvalues. So, by computing $$M^tM$$we have the eigenvectors and the singular values, only $$U$$remains.

Now,

$$
M M^t = U \Sigma V^t V \Sigma U^t = U \Sigma^2 U^t
$$

so $$M M^t U = U \Sigma^2$$.

which means that $$U$$ is the matrix of eigenvectors of $$M M^t$$.

$$M M^t$$ is a$$n \times m$$matrix, $$M M^t$$is$$m \times n$$ and $$n, m \geq r$$ . Hence, $$M^t M$$and $$M M^t$$have additional$$n-r$$ and $$m-r$$eigenvectors which do not show up in $$U$$, $$V$$and $$\Sigma$$. Since $$r$$ is the rank, all other eigenvalues are 0.

