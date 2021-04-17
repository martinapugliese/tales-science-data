# Some geometry

## Voronoi tasselation

The Voronoi [tasselation](some-geometry.md#references) consists in partitioning the plane into regions based on the distance to points in a specific subset of the plane.

For each point, there is a region of all points closer to it than any other one \(Voronoi cells\).

## Simplex

A simplex is the generalisation of a triangle/tetrahedron to an arbitrary number of dimensions. The k simplex is a k-dimensional polytope, the convex hull of its k+1 vertices.

Given points$$u_0, \ldots, u_k \in \mathbb{R}^k$$, with$$u_1 - u_0, \ldots, u_k - u_0$$linearly independent, the simplex determined by them is the set of points

$$
C : {\theta_0 u_0 + \cdots + \theta_k u_k | \theta_i \geq 0, 0 \leq i \leq k, \sum_{i=0}^k \theta_i = 1}
$$

* the _2-simplex_ is a triangle;
* the _3-simplex_ is a tetrahedron;
* the _4-simplex_ is a 5-cell

## References

1.  [Wikipedia about the Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram)

