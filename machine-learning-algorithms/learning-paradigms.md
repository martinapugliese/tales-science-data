# Learning paradigms

## Paradigms of Machine Learning \(main ones\)

There are several ways to separate tasks and problems in machine learning into categories based on the logical way of proceeding and the type of outcome desired. The main, traditional ones are _supervised_ and _unsupervised_ learning, which are different in the approach and the type of data you feed in, but there are some other paradigms which are getting interest in more recent times \(for instance reinforcement learning\).

### Supervised learning

In supervised learning, you teach the machine to learn from data points that have a target value against them specifying the ground truth.

In the case of a _regression_ you want to predict the value of the dependent variable given the independent variable\(s\); in the case of a _classification_, you have data separated into categories, identified by their labels and try to predict the target class of the data point. In both cases the machine is trained to learn from existing matches in order to generalise on new data and spit out the target value for those.

In fact, _regression_ and _classification_ are the main problems you tackle in a supervised learning setting.

### Unsupervised learning

Learning is unsupervised when there are no labels in the training set that specify the ground truth. This type of machine learning deals with extracting patterns from the data, understanding and manipulating its structure in order to separate group of points which are somehow similar.

_Clustering_ is one instance of unsupervised learning: you try to group data points together into groups for similarity; another task is _anomaly detection_, where the computer flag some data point as weird with respect to the rest. Other techniques which usually get classed in this paradigm deal with the shrinking of data points into smaller sets which contain most of the relevant original information, these usually go under the name of _dimensionality reduction_.

