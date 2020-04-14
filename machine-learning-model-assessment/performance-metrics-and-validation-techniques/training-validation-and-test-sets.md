# Training, Validation and Test sets

When you are evaluating which of several models performs best in your case, the way to go is to divide the original dataset into three parts:

* a _training_ set to fit the models
* a _test_ set to evaluate the final model
* a _validation_ set to select the model

The test set is to be ideally be kept aside and only used at the very end of the analysis. While when you are evaluating one model only you are fine with a split into training/test, when you have multiple rivalling models to choose from you need a split into three. A typical way is to split into 50%/25%/25% but it really varies depending on the size you start with in the first place.

The validation set is used to assess the performance of the model you are evaluating, among many, the test set to estimate the generalisation error at the end. Note that this 3-way split is also used when the model needs to be tuned, so you use the validation set to tune its parameters before running it, once tuned, on the test set to measure its performance on unseen data. The model you will run on the test set at the end will be the one with the best performance in the validation phase.

If for these types of cases you'd use only a 2-way split you'd risk underestimating the error and overfitting, because you'd have chosen the model by tuning it on a set and it may not generalise well to unseen data.

The training set is used to train each model \(or each combination of parameters\) on the data; the validation phase then assess, for each of these models/tunes, the performance. After it, you'd have selected the one giving the best result. This phase can for instance encompass a cross-validation. The testing phase is then needed to have an unbiased estimation of the generalisation error, as the model will run on fresh, independent data.

What to typically do when you have finished the whole procedure in order to have a usable model, is to re-train it on training+validation sets and then test it on the test set.

