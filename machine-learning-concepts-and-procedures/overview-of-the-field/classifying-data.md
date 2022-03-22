# Classifying data

**DRAFT page**

## Multiclass classification

The methods here exposed are used in multiclass classification when the algorithm does not support it naturally (because it is suited to binary classification).

### One-vs.-all

Also called _one-vs.-rest_, in this technique a single classifier per class is trained: the samples in the training set which are labelled for that class are considered positive and all the other samples negative. A confidence score is drawn for each of these classifiers.

For an unseen data point, each classifier gets applied and the predicted label will be the one for which the corresponding classifier has the highest score.

The problem with this approach is that the single classifiers are trained on unbalanced sets.

### One-vs.-one

In this technique,$$\frac{k(k-1)}{2}$$classifiers get trained, where$$k$$is the number of classes: each classifier receives a pair of classes from the set and learns to distinguish between them.

For an unseen data point, a voting scheme is applied where all the classifiers are used on it and then the class with the highest number of positives gets predicted.

The problem with this approach is that some regions of the input space may receive the same number of votes.
