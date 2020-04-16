# doc2vec

## What's this and how does it relate to word2vec

doc2vec is a sentence embedding extension of word2vec, also sometimes referred to as paragraph2vec. It came out of the same group at Google in the year following word2vec, 2014. doc2vec is a general embedding methos capable of learning vector representations for pieces of texts: sentences, paragraphs, and also full documents.

The simplest way to represent documents as vectors from the word composing them is to averaging the word vectors, but the weakness of this approach is in losing the word order which is essential for the syntactical structure. doc2vec solves the problem.

Note that a Bag of Words model with N-grams tries to solve the problem of word order, but ends up creating high-dimensional and very sparse vectors, the vectors produced by word2vec are dense instead.

doc2vec has been proposed with two possible architectures: the distributed memory model \(related to the CBOW in owrd2vec\) and the distributed bag of words model \(related to the skip-gram in word2vec\).

## Distributed memory model

In this architecture, both words and sentences are trained, a sentence is treated as another word, acting as a memory thath remembers what is missing from the current context.

* Contexts have a fixed length and sampled from a sliding window over the paragraph
* the paragraph vector is shared cross all contexts generated from the same paragraph but not across paragraphs
* word vectors are shared across paragraphs instead 

All vectors are trained via gradient descent with backpropagation as per usual. Paragraph and word vectors can be averaged or concatenated. With V words in the vocabulary, N paragraphs and suppose the vectors we want to learn have dimension p, there will be $$Vq + Nq$$ parameters to learn.

## Distributed bag of words model

In this model, context words are ignored. At each iteration of gradient descent, a text window is sampled and then a word is sampled from it. This requires to store less data and is faster but has a lower performance than the DM model.

## References

1.  Q Le, T Mikolov, [**Distributed representations of sentences and documents**](https://cs.stanford.edu/~quocle/paragraph_vector.pdf), _Proceedings of the 31st International Conference on Machine Learning \(ICML-14\)_, 2014

