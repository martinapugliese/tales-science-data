# Latent semantic analysis

## What is in a nutshell

Also called _Latent Semantic Indexing_, it is a technique first described in [Deerwester](latent-semantic-analysis.md#references) and then in [Papadimitriou et al](latent-semantic-analysis.md#references). It is a method which uses SVD to identify patterns in collections of texts encoded numerically in a matrix. The bulk of the idea is that words used in the same context have similar meanings, so that semantically related terms show latent correlations. In the context of Information Retrieval, this allows a query against documents which have undergone LSA to output results which are conceptually similar in meaning to the query even if the words are not the same, so this works as an improvement of a simple keyword search.

## How does it work

The first thing is to build the term-document matrix M, an$$n \times m$$ matrix \(n number of documents in collection, m number of unique terms\)

Then we weigh the data in the matrix so that each cell value$$m_{ij} $$ becomes a multiplication of a local weight$$l_{ij}$$\(a function of the relative frequency$$f_{ij}$$of the term i in document j\) and a global weight$$g_i$$\(the relative frequency of term i in the entire collection of documents\).

Now, for the _local weight_, typical choices of the function of the occurrences are:

* _binary_: 

  $$
  l_{ij} = 
  \begin{cases}
    1 \text{ if term } i \ \text{exists in doc} \ j\\
    0 \text{ else}
  \end{cases}
  $$

* _term frequency_: the actual number of occurrences$$f_{ij}$$of term i in doc j
* _log_: $$l{ij} = \log(f{ij} + 1)$$ 
* _augnorm_: $$\frac{\frac{f{ij}}{\max{ij} f_{ij}}}{2}$$ 

For the _global weight_ instead, functions can be:

* _binary_:$$g_i = 1$$ 
* _normal_:$$gi = \frac{1}{\sqrt{\sum_j f{ij}^2}}$$ 
* _IDF_ \(see page\):$$g_i = \log_2{\frac{n}{1 + d_i}}$$ , with $$d_i$$ the number of documents in which term i appears and N being the number of documents in the collection
* _GF-IDF_ :$$g_i = \frac{f^g_i}{d_i}$$ , where $$f^g_i$$ is the total number of times term i appears in the whole collection \(g stands for "global"\); $$d_i$$ is the number of documents in which term appears
* _entropy_: $$gi = 1 + \frac{\sum_j p{ij} \log{p{ij}}}{\log n}$$_,_ with __$$p_{ij} = \frac{f_{ij}}{f^g_i}$$ 
* An SVD \(see page\) is run on the matrix so it is decomposed into three matrices as$$M = T S D^t$$, T being an$$m \times r$$term-concept matrix, S that of singular values \($$r \times r$$\), D the concept-document matrix \($$n \times r$$\), which respect$$T T^1 = \mathbb{1}$$;$$D^t D = \mathbb{1}$$and $$s_{ij} = 0$$when $$i \neq j$$.
* The SVD is truncated to reduce the rank and keep only the largest $$k \ll r$$ singular values, so that the dimensionality is effectively reduced to k and only the most important semantic information is kept. Actually, the efficient LSI algorithms compute directly these k singular values instead of the SVD of the full matrix and then truncate it

## Then ...

The reduced T, D, S will define the new vector spaces and embody the conceptual information in the collection. The similarity of terms or documents is computed in these spaces: for instance, the similarity between documents j and i will be computed as the similarity \(typically cosine\) between the corresponding vectors in the document space; same for the similarity between terms.

A query q can be transformed into this space as well, as $$\hat q = S^{-1} T q$$ , and then similarity to documents can be used to retrieve the best matching ones.

Note that

$$
M = T S D^t \iff M^t T S^{-1} = D \ ,
$$

so a new vector for a new document can be calculated by multiplying a new column in$$M^t$$, but this is only a good idea if the new document contains terms and concepts which are already represented, otherwise they'd be ignored: to account for them the SVD has to be recalculated. The process of augmenting the LSI with new documents is called _folding-in_.

### Applications

The low-dimensional space can be used to

* compare documents \(clustering, document classification, ...\)
* find relations between terms \(synonymy, ...\)
* find similar documents across languages

### Note that

* A PCA approach on these problems would not work as it would require a normalisation of the matrix, which would imply a loss of variability in the lexicon

{% page-ref page="../general-concepts-and-tasks-in-nlp/text-as-numerical-features.md" %}

{% page-ref page="../../machine-learning-concepts-and-procedures/dimensionality-reduction-and-matrix-factorisation/singular-value-decomposition.md" %}

## References

1.  S Deerwester,  **Indexing by Latent Semantic Analysis** _Journal of the American society for information science_, 41, 1990
2.  C H Papadimitriou, P Raghavan, H Tamaki, S Vempala, [**Latent Semantic Indexing: a Probabilistic Analysis**](https://pdfs.semanticscholar.org/6406/70d83e83427ff85ce2fbe4381d517f9512c1.pdf), _Proceedings of the seventeenth ACM SIGACT-SIGMOD-SIGART symposium on Principles of database systems ACM_, 1998

