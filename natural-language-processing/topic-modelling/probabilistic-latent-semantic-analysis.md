# Probabilistic latent semantic analysis

## What is it and how it works

PLSA, also called PLSI \(I for "indexing"\), is a probabilistic version of LSA which models the co-occurrence of words and documents as a mixture decomposition; it came out in the [Hofmann's paper](probabilistic-latent-semantic-analysis.md#references). Note that in the following, we will use the words _concept_ and _topic_ interchangeably.

Given word w and document d, the probability of co-occurrence \(as, the probability that w occurs in d\) is given by a mixture of conditionally independent multinomial distributions. Given latent categories \(topics\) c, we write indeed:

$$
\begin{align}
    P(w, d) &= \sum_c P(c) P(d | c) P(w | c) \\
            &= P(d) \sum_c P(c | d) P(w | c)
\end{align}
$$

In the fist formulation, w and d are thought as generated from the latent class c in similar ways by using the conditional probabilities$$P(d|c)$$and$$P(w|c)$$. In the second formulation instead, $$\forall d$$ , a latent class is chosen conditionally to it according to the probability $$P(c|d)$$and a word is generated from that class following$$P(w|c)$$. The number of parameters is$$c(w+d)$$, so it grows linearly with the number of documents. Said parameters are estimated using the EM algorithm \(see page\).

{% page-ref page="../../probability-statistics-and-data-analysis/methods-theorems-and-laws/the-maximum-likelihood-maximum-a-posteriori-and-expectation-maximisation-estimation-methods.md" %}

## Concepts, documents, words and queries

PLSA is an improved variation of LSA in the sense that

* documents might not contain similar terms but still refer to the same concept
* queries can contain words not present in a document and still be very relevant to the document

This is why is uses the probability of a word, or full query q given the context \($$r \in {0, 1}$$is the relevance of the document\):

$$
\begin{align}
    P(r=1 | q) &= \frac{P(q | r=1) P(r=1)}{P(q)} \\
               &\propto P(q|r=1) P(r=1)
\end{align}
$$

where in the last writing we have$$P(q|r=1)$$, telling us given a document, how probable is the query, and$$P(r=1)$$, which can be uniform or dependent on the popularity of the document.

$$P(q | r=1)$$is calculated as:

* $$\forall d$$, compute the probability of each word w to be relevant for it $$P(w | r=1)$$ 
* compute the conditional probability of words in q

The model relies on the idea that each concept has a distribution over words, each document is a mixture of concepts and each word is drawn from the topics. We will have, according to the equation above,

$$
\begin{align}
    P(w, d) &= P(d) \sum_c P(w | c) P(c | d) \\
            &= \sum_c P(d|c) P(c) P(w|c)
\end{align}
$$

and this is a factorisation of the original matrix into three matrices \(hence the relation to LSA\):

* a matrix U which maps documents to concepts
* a matrix $$\Sigma$$ which contains the concepts
* a matrix V which maps concepts to words

But, differently from an SVD factorisation used in LSA, here there is no orthonormality condition for U and V and their elements are non-negative because they are probabilities.

Now, we need to find all parameters such that the probability of observing the corpus is maximised. Using a MLE approach \(see page, linked above\), we need to maximise the likelihood

$$
\mathcal{L} = \Pi_{i=1}^n \Pi_{j=1}^m P(w_j, d_i)^{n(w_j, d_i)} \ ,
$$

where the exponent gives the multiplicity of$$w_j$$in$$d_i$$, as in, their count. So, computing the log:

$$
\begin{align}
    \log \mathcal{L} &= \sum_{i=1}^n \sum_{j=1}^m n(w_j, d_i) \log P(w_j, d_i) \\
                     &= \sum_{i=1}^n \sum_{j=1}^m n(w_j, d_i) \log \left[ \sum_{k=1}^K P(d_i) P(c_k|d_i) P(w_j|c_k) \right] \\
                     &= \sum_{i=1}^n n(d_i) \sum_{j=1}^m \frac{n(w_j, d_i)}{n(d_i)} \log \left[\sum_{k=1}^K P(d_i) P(c_k|d_i) P(w_j|c_k) \right] \\
                     &= \sum_{i=1}^n n(d_i) \sum_{j=1}^m \frac{n(w_j, d_i)}{n(d_i)} \left( \log P(d_i) + \log \left[ \sum_k P(c_k| d_i) P(w_j|c_k) \right]  \right) \\
                     &= \sum_{i=1}^n n(d_i) \left[ \sum_{j=1}^m \frac{n(w_j, d_i)}{n(d_i)} \log P(d_i) + \sum_{j=1}^m \frac{n(w_j, d_i)}{n(d_i)} \log \sum_k P(c_k | d_i) P(w_j | c_k) \right] \\
                     &= \sum_{i=1}^n n(d_i) \left( \log P(d_i) + \sum_{j=1}^m \frac{n(w_j, d_i)}{n(d_i)} \log \left[ \sum_k P(c_k | d_i) P(w_j | c_k) \right] \right)
\end{align} \ ,
$$

this because $$n(w_j, d_i)$$ is the count of$$w_j$$in$$d_i$$and$$n(d_i)$$is the number of words in $$d_i$$, hence the semplification at the first addend, as $$\sum_j \frac{n(w_j, d_i)}{n(d_i)} = \sum_j P(w_j) = 1$$.

Because of the coupling elements given by the $$c_k$$, this is a hard optimisation problem and the solution can be found via the EM algorithm:

* _E step_: calculate the posterior using the current estimates of the parameters:

$$
P(c_k|d_i, w_j) = \frac{P(w_j, c_k | d_i)}{P(w_j | d_i)} = \frac{P(w_j|c_k, d_i) P(z_k|d_i)}{\sum_k P(w_j|c_i, d_i) P(c_i, d_i)}
$$

* _M step_: maximise the logarithm of the likelihood from the posteriors 

## References

1.  T Hofmann [**Probabilistic latent semantic indexing**](http://www.csie.ntu.edu.tw/~b97020/DSP/p50-hofmann.pdf) _Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval, ACM_ 1999
2.  [Wikipedia on PLSA](https://en.wikipedia.org/wiki/Probabilistic_latent_semantic_analysis)

