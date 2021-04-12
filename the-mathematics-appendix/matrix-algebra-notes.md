# Matrix Algebra notes

Capital letters, like$$A$$, indicate matrices.

## Transpose of a matrix

Transposing a matrix$$A$$, of elements $$[A]_{ij} = a_{ij}$$ , is the operation which switches the row and column positions of each element:

$$
[A^t]_{ij} = a_{ji}
$$

### Properties

* **Transpose of the transpose**:$$(A^t)^t = A$$ 
* **Transpose of the sum**:$$(A + B)^t = A^t + B^t$$ 
* **Transpose of the product**:$$(AB)^t = B^t A^t$$ 

_**Proofs**_ 

The first one follows straightly from definition.

The second one is straightforward just because the elements of$$(A+B)^t$$are the sums of elements in$$A^t$$and$$B^t$$.

The third one is easily proven using the fact that $$[AB]_{ij} = \sum_k a_{ik} b_{kj}$$_,_ so that we can say $$[(AB)^t]_{ij} = [AB]_{ji} = \sum_k a_{jk} b_{ki}, $$and $$[B^t A^t]_{ij} = \sum_k b^t_{ik} a^t_{kj} = \sum_k b_{ki} a_{jk}$$ , so the two things are the same.

## Special types of matrices

* _**IDEMPOTENT**_: $$M^2 = M$$ 

## Matrix Convolution

Given two matrices A and B \(typically kernel and image, as this is used in computer vision\),

$$
A =
\begin{bmatrix}
    a_{11}  & a_{12} & a_{13} & \dots & a_{1n} \\
    a_{21}  & a_{22} & a_{23} & \dots & a_{2n} \\
    \dots   &  \dots & \dots & \dots & \dots \\
    a_{n1}       & a_{n2} & a_{n3} & \dots & a_{nn}
\end{bmatrix},  \ \
B =
\begin{bmatrix}
    b_{11}  & b_{12} & b_{13} & \dots & b_{1n} \\
    b_{21}  & b_{22} & b_{23} & \dots & b_{2n} \\
    \dots   &  \dots & \dots & \dots & \dots \\
    b_{n1}  & b_{n2} & b_{n3} & \dots & b_{nn}
\end{bmatrix} \ ,
$$

their convolution is obtained via the multiplication of locationally similar entries and summing:

$$
\mathcal{C} = \sum_{i=0}^{i=} \sum_{j=1}^{j=} B_{ij} A_{n-in-j}
$$

This procedure is loosely related to mathematical convolution.

## Frobenius norm of a matrix

Given matrix M, its Frobenious norm is the square root of the sum of the squares of its elements.

$$
||M|| = \sqrt{\sum_{i,j} M_{ij}^2}
$$

