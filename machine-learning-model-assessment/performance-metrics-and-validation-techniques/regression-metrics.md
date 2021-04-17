# Regression metrics

## RMSE: root mean square error

This is probably the most common metric used to assess the quality of a regression task. The RMSE is calculated as

$$
RMSE = \sqrt{\frac{ \sum_{i=1}^n (y_i - \hat{y_i})^2 }{n}} \ ,
$$

where$$n$$is the number of samples in the set,$$y$$the actual value and$$\hat y$$the predicted score \(the difference between predicted and actual value being called the _residual_\). This metric represents the square root of the average of the squared differences between the actual and the predicted values.

## RSS: residual sum of squares

The RSS is calculated as

$$
RSS = \sum_{i=1}^n (y_i - \hat{y_i})^2
$$

The RSS expresses the _unexplained_ variance, the variance not captured by the model. 

## $$R^2$$: coefficient of determination

The coefficient of determination, usually indicated as$$R^2$$, expresses the proportion of the variance in the dependent variable that is predictable from the independent variable. It is a number smaller or equal than 1, 1 being the best situation.

Calling$$\hat{y}$$the predicted values and$$y$$the actual values, we calculate the average of the actual values

$$
\bar y = \frac{1}{n} \sum_{i=1}^n y_i \ ,
$$

the _total sum of squares_

$$
SS_{TOT} = \sum_{i=1}^n (y_i - \bar y)^2
$$

and the explained sum of squares

$$
SS_{exp} = \sum_{i=1}^n (\hat{y_i} - \hat y)^2
$$

With the definition of the RSS from above, we have

$$
R^2 = 1 - \frac{RSS}{SS_{TOT}}
$$

The second bit expresses the fraction of unexplained variance to the total variance in the data, so the $$R^2$$ is the fraction of variance explained to the total variance.

## MAE: mean absolute error

The MAE is calculated as

$$
MAE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i}) \ ,
$$

that is, as the average of the differences of the actual to the predicted values



## References

1. G Varoquaux, [**Understanding and diagnosing your machine-learning models**](http://gael-varoquaux.info/interpreting_ml_tuto/content/01_how_well/01_metrics.html#classification-settings) \(regression setting\)
2. Wikipedia has a very nice [page](https://en.wikipedia.org/wiki/Coefficient_of_determination) on the coefficient of determination

