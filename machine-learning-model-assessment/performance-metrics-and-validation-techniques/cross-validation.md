# Cross-Validation

## What do you do in cross-validation?

Cross validation is a technique for validating the performance of a model. In its basic form it basically consists in dividing the original data sample into sets, picking one of them as the training set and validating the performance on the other, the test set, repeating the procedure multiple times with different splits of the original set. Eventually, the results are averaged.

The procedure results in a better outcome than the simple training/test split because it allows for a control of the error by the averaging procedure.

There are multiple categories of cross-validation techniques.

## Types of Cross Validation techniques

### k-fold cross validation

In this case, the original data set is split into k equally-sized sub-samples and each subset is in turn used as the test set while the remaining k-1 constitute the training set. This way you repeat the procedure k times \(called _folds_\), one for each test set. At the end, an average of all validation results is computed. This way, all sample points in the original set are used both for training and for testing \(in different folds\).

If folds are selected such that each set contains the same percentage of samples in each target class \(or dependent variable in the case of regression\), it is called a _stratified k-fold cross validation_.

### Leave-one-out

Is the variation of the k-fold when k=n, n being the number of samples, meaning you are doing samples of one data point so it's one against everyone else.

### Leave-p-out

It is the same as the leave-one-out but the test set is constituted by p of the samples, but all possible splits are calculated, meaning that all possible situations where p items are selected as the test set are built. It is a very expensive procedure and the comprehensive way to consider all possible splits. Note that a k-fold is an approximation of this one as not all splits are considered \(because the original set is preliminarily partitioned into k subsets\).

### Hold-out

It is a k-fold where k=2 but points are randomly assigned to each of the two sets, with typically the training set being bigger. It is a very loose way to do a cross validation, the only real advantage beyond speed being the fact that both sets are large.

### Repeated random sub-sampling validation

Also called a Monte Carlo cross validation, this method splits the original data set into training and test randomly at each iteration. The advantage of this method over a k fold is that the number of points into training and test parts does not depend on the number of folds chosen; the disadvantage of this method is that some samples may never be selected in the test set, or selected multiple times over the iterations.

