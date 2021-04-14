# Intro

Topic models are statistical techniques used in NLP to discover the "topics" in a collection of documents. The basic idea is that words related to a topic will appear frequently in documents about that topic. There are several of these techniques, all originating from this same basic idea and all based on algebraic manipulations of matrices where text features are encoded.

The first paper which introduced the ideas behind these methods dates back from 1990 \(see [Deerwester](intro.md#references)\) and introduces a technique called _Latent Semantic Analysis_ which works on features extracted from text \(for instance tf-idf values by identifying subspaces of features with most variance, then resumed in [Papadimitriou et al](intro.md#references). In 1999, another [paper](intro.md#references) was published which was an extension/improvement of the first one \(_Probabilistic Latent Semantic Indexing_\) and in 2003 the [paper](intro.md#references) about _Latent Dirichlet Allocation_ came out, which is the simplest proper topic model. All three techniques are described in the notebooks of these folder.

## References

1.  S Deerwester,  **Indexing by Latent Semantic Analysis** _Journal of the American society for information science_, 41, 1990
2.  C H Papadimitriou, P Raghavan, H Tamaki, S Vempala, [**Latent Semantic Indexing: a Probabilistic Analysis**](https://pdfs.semanticscholar.org/6406/70d83e83427ff85ce2fbe4381d517f9512c1.pdf), _Proceedings of the seventeenth ACM SIGACT-SIGMOD-SIGART symposium on Principles of database systems ACM_, 1998
3.  T Hofmann [**Probabilistic latent semantic indexing**](http://www.csie.ntu.edu.tw/~b97020/DSP/p50-hofmann.pdf) _Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval, ACM_ 1999
4.  D M Blei, A Y Ng, M I Jordan, [**Latent dirichlet allocation**](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf), _Journal of machine Learning research_, 2003

