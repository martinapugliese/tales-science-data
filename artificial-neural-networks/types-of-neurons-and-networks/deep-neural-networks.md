# Deep neural networks

Deep neural networks are those with multiple hidden layers. They are super-powerful beasts in that they allow us to solve very complicated problems with astonishing performance results, but also quite delicate due to their nature, so some care has to be taken to set them up in the best possible way.

## The vanishing gradient problem

Deep networks exhibit the problem that, in normal conditions and without the use of correcting mechanisms, different layers tend to learn at different speeds, with a negative effect on the overall performance of the network as a whole. In a typical case, the earlier the layer, the slower the learning; because the speed of learning is given by the gradient of the cost function, this means that said gradient gets smaller in earlier layers. The reverse \(the "exploding gradient problem"\) can also happen. All in all, the problem is summarised by saying that the gradient of the cost function suffers from _instability_ along the layers.

The reason behind this has to be found in the computation of the cost function derivative itself. When you do it for a deep network, you find that it's a multiplication of factors of the type $f' w$, where $f$ is the activation function and $w$ the weight at that layer. In the usual case of sigmoid neurons, the derivative of the sigmoid has a bell shape, peaked at 0 with a value of 0.25. These factors then tend to get smaller and smaller the more backwards, that is, the more layers, we go. This is the reason why the earlier the layer, the smaller the gradient. The source of this unstable behaviour is that the gradient in early layers is the product of terms in later layers, so the small values tend to multiply the more factors there are.

Several solutions have been proposed to tackle the problem, see the [Wikipedia page](https://en.wikipedia.org/wiki/Vanishing_gradient_problem#Solutions) for a short overview.

## References

1.  M Nielsen, [**Neural networks and deep learning**](http://neuralnetworksanddeeplearning.com/chap5.html), chapter 5

