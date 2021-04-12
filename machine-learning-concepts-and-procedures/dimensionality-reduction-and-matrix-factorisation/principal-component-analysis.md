# Principal Component Analysis

Principal Component Analysis \(PCA\), whose original and pioneering paper is in [the references](principal-component-analysis.md#references), is a method for dimensionality reduction whose aim is to change the coordinate system via a linear transformation and switch to a new set of coordinates which explain most \(not all\) of the variance in the original dataset.

Given a data matrix$$X$$where samples \($$n$$\) are placed in rows, so that features are in the columns \($$p$$\), we want to find a coordinate set able to isolate most of the variance in the data. PCA transforms the data by rotating them in such a way that points are spread out as much as possible

$$
X =
  \begin{bmatrix}
    X_{11} & X_{12} & \ldots & X_{1p} \\
    \ldots & \ldots & \ldots & \ldots \\
    X_{n1} & X_{12} & \ldots & X_{np} \\
  \end{bmatrix}
$$

The first step consists in rescaling the original matrix in such a way that each feature has 0 mean and standard deviation 1. For feature$$j$$, we compute the mean and the standard deviation across the samples:

$$
\mu_j  = \frac{1}{n} \sum_i X_{ij} \ ,
$$

$$
\sigma_j = \sqrt{\frac{1}{n} \sum_i (X_{ij} - \mu_j)} \ ,
$$

so as to build the scaled matrix whose elements are

$$
Z_{ij} = \frac{X_{ij} - \mu_j}{\sigma_j}
$$

The second step is computing the correlation matrix of$$Z$$\(the correlations between each pair of properties\):

$$
C_{jk} = \frac{1}{n} \sum_i Z_{ij} Z_{ik} = \frac{1}{n} \sum_i \frac{(X_{ij} - \mu_j)}{\sigma_j} \frac{(X_{ik} - \mu_k)}{\sigma_k}
$$

The third step is about computing the eigenvalues and eigenvectors of $$C$$ .

The PCA method consists in isolating the largest eigenvalues and projecting the sample points onto the corresponding eigenvectors, so that a change of coordinate system takes place. In fact, the system to be solved is

$$
C \underline{v} = \lambda \underline{v}
$$

The _principal components_ are the projections of the sample data points onto the eigenvectors. The$$k$$-th principal component is

$$
p_k = v_k^t X
$$

It can be proven that the eigenvalues of$$C$$are the variances of the principal components. In fact, from the eigenvalue equation above:

$$
\underline{v}^t C \underline{v} = \underline{v}^t \lambda \underline{v} = \lambda \underline{v}^t \underline{v} = \lambda
$$

Keeping only the largest ones means keeping most of the variance in the original dataset. The total variance in the dataset is$$p$$because the columns in matrix$$Z$$have variance 1.

Rotating the coordinates does not change this variance, but considering just some eigenvalues will cut some part of it. The fraction of variance represented, for instance, by the first and second components is $$\frac{(\lambda_1 + \lambda_2)}{p}$$ . A PCA approach is only useful if a few components explain most of the variance in the dataset.

## References

1. K Pearson, [**On lines and planes of closest fit to systems of points in space**](http://stat.smmu.edu.cn/history/pearson1901.pdf), _The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science_, 2.11, 1901
2. [PCA explained visually](https://setosa.io/ev/principal-component-analysis/), a project by V Powell

