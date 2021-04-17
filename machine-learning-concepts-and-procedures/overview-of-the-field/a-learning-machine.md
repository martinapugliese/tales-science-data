# A learning machine

_**DRAFT PAGE**_

_Core concepts in Machine Learning: how does a machine learn patterns from data._ 

## Garbage in, garbage out

This phrase is used to mean that if poor data is fed into an algorithm, however sophisticated it may be, poor results are obtained.

## Lazy and eager learning

In a _lazy learning_ approach, the algorithm outputs the result on test data only after all training data has been ingested and computation made on it. It uses a predictive function that gets approximates locally and is thereby adaptable to changes. An example is kNN.

In an _eager learning_ approach instead, the predictive function is built during training so that the algorithm can be run on test data along the way. The function is then built globally, making computation less space-consuming. Examples are Naive Bayes and neural networks.

## Ensemble methods

Ensemble methods combine predictions from several estimators to improve the ability to generalise to new data. There are two main classes.

### Averaging methods

The estimators used are independent and their predictions get averaged, to reduce the variance. The main way to obtain this is via _bagging_ \(which stands for _bootstrap aggregating_\): several instances of the algorithm are run on random subsets of the training set, where the random subsets are selected with replacement. The method works great to reduce overfitting; an example is the Random Forest.

### Boosting methods

The estimators are run sequentially so that you have several weak learners combined, and this reduces the bias. Boosting works better than bagging on noisy data; an example is AdaBoost.

