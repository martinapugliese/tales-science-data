# Word Embeddings

_Word embeddings! Words and documents become vectors, that you can embed in a mathematical space and compute similarities, add and subtract together!_

Word embeddings are a set of models in NLP such that words \(or phrases, because they can be extended to them\) are mapped to numerical vectors. This way, they are rendered in numerical representations which can be used to apply  algebraic operations to compute similarities and analyse distances in space, which can be used to derive similarities and predictions. The beauty of this is that you treat words as regular vectors in a mathematical space. Note that this is the same you would do if were to you one-hot encode them, but this is typically a quite inefficient procedure, as it would create very sparse vectors which have no relations one another: for instance "dog" might have a 1 in position 123 and "animal" a 1 in position 1167, but there is no relation between the two vectors even though the two words are semantically related. Similar techniques, like using frequencies or variations of them \(like TF-IDFs\) also suffer from similar problems. Word embeddings aim at giving dense representations of words in a vector space that you can actually use to compute things on and are capable of capturing relations among words at the level of their semantics. For instance, these vectors would tell you that "dog" is related to "animal".

Word embeddings models are based on neural networks.

## Contents

{% page-ref page="word2vec.md" %}

{% page-ref page="doc2vec.md" %}



