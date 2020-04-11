# ANOVA: Analysis of Variance

ANOVA \(Analysis of Variance\) is a method proposed by Fisher in the late '10s of the twentieth century to analyse differences among means and variations in sets of data, the idea being that of separating the variance into components for each source of variation. It is a generalisation of the t-test to more than 2 groups and it follows the same logics: a result is called significant if it is proven to be unlikely to have occurred by chance; the null hypothesis being that all groups are random samples of the same population, so that their means are equal. ANOVA is cheaper to run than multiple t-tests and also more reliable.

## Learning by example

This is a classic illustrative example of the working of the method.

Let's say that we have some trees, of the same species, located in 7 different places and we want to see whether the leaf size changes by location. We collect 10 leaves from each of the locations, so we have 10 samples in each of the 7 groups. Clearly, the leaf size will vary within a group but the idea is to check whether group averages are different.

Our null hypothesis is that the groups are not different \(they appear so by chance\). We use the $$F$$ -ratio to evaluate the variation in the group averages we measure to the one we expect:

$$
F = \frac{\text{meausured variation in group means}}{\text{expected variation in group means}}
$$

An $$F \approx 1$$ tells that the null hypothesis is correct; a large $$F$$ that there is a location effect instead. But how big should $$F$$ be before we reject the null hypothesis? We use the p-value to assess that.

The numerator of $$F$$ is the _mean square for between_, computed as the mean sum of the squared deviations of each group's mean to the overall mean, using the number of groups - 1 as the degrees of freedom; the denominator is the _mean square for error_, computed as the mean sum of the squared deviations of each leaf size from the group's mean, with degrees of freedom being the number of leaves - the number of groups.

## How the method works and what it needs

ANOVA is based on comparing the variance between the samples to the variance within each sample. If the first is much greater than the second, the means of the samples are not equal; if on the contrary the first is on par with the second, the means of the samples are not significantly different.

The assumptions of ANOVA are

* the populations involved are normally distributed
* the populations have the same variance
* the samples are randomly selected and independent

## A worked example

This example has been reworked from [here](anova-analysis-of-variance.md#references). Let's say that we have data about the pressure exercised on the driver's head by the airbag in a crash test, for 3 types of cars: compact, midsize and full-size, see table

| Compact | Midsize | Fullsize |
| :--- | :---: | ---: |
| 643 | 469 | 484 |
| 655 | 427 | 456 |
| 702 | 525 | 402 |

We want to know whether the mean pressure exercised is equal for each of the car's categories, using a significance level of 5%.

First, we need to compute the sample means and variances/standard deviations \(computed with 2 degrees of freedom\), which are

| Car category | Mean | STD |
| :--- | :--- | :---: |
| Compact | 666.67 | 31.18 |
| Midsize | 473.67 | 49.17 |
| Fullsize | 447.33 | 41.68 |

Out null hypothesis is that the population means are all equal: $$H_0 = \mu_1 = \mu_2 = \mu_3$$ ; the alternative hypothesis is that at least one of them is significantly different from the others.

Let's calculate the F-ratio. We start from the total sum of squares, which gives the total variation in the data:

$$
SST = \sum_r \sum_j (X_{ij} - \bar x)^2  \ ,
$$

where the first sum is over the rows of the data table and the second over the columns; $$\bar x$$ is the gran mean of all samples, which is 529.22, so the SST comes at 96303.55.

Then we have the between sum of squares, which expresses the variation between different groups of data:

$$
SSTR = \sum_j r_j (x_j - \bar x)^2 \ ,
$$

where $$r_j$$ is the number of rows in the j-th group and $$x_j$$ the mean of the j-th group. This comes at 86049.55.

Then we have the within sum of squares, which gives the variation in the data from each group,

$$
SSE = \sum_r \sum_j (X_{ij} - x_j)^2,
$$

which comes at 10254. Note that $$SST = STR + SSE$$ . At this point, the total mean of squares is  \( $$N$$ being the number of samples\), the mean of square group is $$MSTR = \frac{SSTR}{C-1}$$ \( $$C$$ being the number of groups\), and the mean square error is $$MSE = \frac{SSE}{N-C}$$ , so the F ratio can be computed as

$$
F = \frac{MSTR}{MSE} = 25.17 \ .
$$

Our intuition tells us that it's quite large to be between variation is larger than the within variation, hence the null hypothesis is not likely. But to quantify this, we use the values of the F ratio distribution, at the given degrees of freedom \(at numerator we have $$C-1$$ , at denominator $$N-C$$ \): looking at tables for $$F_{2,6}$$ at the chosen significance level $$\alpha=0.05$$ , we see 5.14. The null hypothesis is rejected if the observed F ratio is bigger than this value, which is the case.

## References

1. The airbag [original example](http://cba.ualr.edu/smartstat/topics/anova/example.pdf)
2. R A Fisher **The Correlation Between Relatives on the Supposition of Mendelian Inheritance**, _Phil Trans of the Royal Society of Edinburgh_, 52, 1918

