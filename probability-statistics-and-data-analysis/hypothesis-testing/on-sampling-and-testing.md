# On sampling and testing

_You have some data \(a sample, which you have built with sweat and blood\), you have an hypothesis and the data is meant for you to prove or disprove it._

## How to sample

In general, you'd have a sample of a population, otherwise \(if you had the full population\) you would know everything about it. You have to test precisely because you only have partial information. But is your sample always good/representative? Sampling randomly \(that is, uniformly\) isn't always the best idea.

### Stratified sampling

Stratified sampling is a way to sample data from a population, especially in cases when said population isn't homogeneous so sampling "randomly" \(all points extracted with the same probability\) risks not reflecting the lack of homogeneity.

Stratification is the process of dividing the population into homogeneous subgroups before sampling \(_strata_\), so that each element only belongs to one stratum, and then random sampling is applied on each stratum.

### **Proportional allocation**

In this strategy, you use the sampling fraction for each stratum: if $$n$$is the desired sample size, we use$$n_s = \frac{n N_s}{N}$$, where$$N$$is the total number of items and$$N_s$$the number of items in the stratum as the size fraction of the stratum.

### **Optimal allocation**

In this strategy, the standard deviation of the distribution in each stratum gets taken into account, so that the size fraction of the stratum is$$n_s = \frac{n N_s \sigma_s}{\sum{k=1}^S N_k \sigma_k}$$. What this means is that strata are weighted with their variability.

## Testing

### The null hypothesis

The null hypothesis is the one checked against in the statistical test, that is, the one we are checking if we can disregard; it is basically assumed to be true until some evidence proves the contrary. Typically, it is indicated as $$\mathcal{H_0}$$.

### Hypothesis testing and types of error

#### **Type I error and Type II error**

It is a _false positive_, that is, occurs when$$\mathcal{H_0}$$is erroneously rejected.

It is a _false negative_, that is, occurs when$$\mathcal{H_0}$$is not rejected when it should be.

Here's a handy table:

| Null hypothesis and types of errors | $$\mathcal{H_0}$$true | $$\mathcal{H_0}$$ false |
| :--- | :---: | :---: |
| **Reject** $$\mathcal{H_0}$$  | Type I | true positive |
| **Don't reject** $$\mathcal{H_0}$$  | true negative | Type II |

## References

1.  [Wikipedia has some examples](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)

