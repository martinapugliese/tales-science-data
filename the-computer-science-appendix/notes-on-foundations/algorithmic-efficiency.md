# Algorithmic efficiency

The efficiency of an algorithm is measured based on how long it takes to run and how much memory it consumes. Roughly speaking, these are the concepts of time and space complexity, respectively.

## Time complexity

For assessing the time complexity of an algorithm \(which in many cases is the most important one to measure\) the theory uses the "big-O notation" \(see the relative [page](../../the-mathematics-appendix/mathematical-functions.md#big-o-and-little-o-notation) in the mathematical appendix\), borrowed from mathematics. This formalisation attaches a value of time complexity to an algorithm which expresses its asymptotic behaviour, mathematically speaking, as a function of the size of the data in input. For instance:

*  $$O(N)$$ complexity: the time scales linearly with the size in input \(e.g. a simple for loop over an array of elements, that does nothing else\) 
* $$O(N^a), a > 1$$ complexity: the scaling is polynomial, a much \(depending on the value of$$a$$\) less efficient algorithm

## Space complexity

Space complexity measures the \(asymptotic\) behaviour in terms of memory consumption by the algorithm. It is also represented using the big-O notation.









