# Setting up Neural Networks

The way neural networks get set up changes the way they perform. Note that in general these algorithms have lots of parameters \(all the weights and biases\) and it's well known that with lots of parameters you can fit everything. Overfitting is a very common problem with neural networks. The discussion here loosely follows the brilliant chapter 2 of the wonderful [Nielsen's book](setting-up-neural-networks.md#references).

## The cost function

Following gradient descent, weights and biases of a network change proportionally to the derivatives of the cost function; if these are small, learning will be slow. Now, a quadratic cost function, whose form would be

$$
C \propto (y-f(wx+b))^2 \ ,
$$

$$f$$being the network prediction and$$y$$the actual value, has derivatives $$\frac{\partial C}{\partial w} \propto (y-f) f' x$$and$$\frac{\partial C}{\partial b} \propto  (y-f)f'$$. Now, with sigmoid neurons we have the derivative of the sigmoid which is very small when the output if close to 1, as the curve flattens, and this makes the learning quite slow.

A typical way to do better on this is to use a different cost function. A choice can be the cross-entropy,

$$
C = - \frac{1}{n} \sum_x [y \log f + (1-y) \log(1-f)] \ ,
$$

$$n$$being the number of samples. This choice solves the problem as its derivatives will be proportional to$$f - y$$, which is the error in the prediction, making the learning proportional to the error itself. Very convenient: it's like a human who learns faster the wronger he/she is about something!

## Regularising

To tackle overfitting, regularisation is a common choice as per machine learning tasks in general. One can apply$$L_2$$or$$L_1$$regularisation terms as per usual, or another common choice in neural networks is the so-called _dropout_, which works by actually modifying the network itself.

What you do is starting with the whole network as is and then removing half of the neurons in the hidden layers \(call them "dropout neurons"\), choosing them at random. You make it proceed as normal and then repeat the procedure by choosing another set of dropout neurons. The fact that you'll have half the neurons in the hidden layers has to be compensated by halving their outputs as well. The whole mechanism is a sort of averaged result of the training of different networks and the reason why it works in reducing overfitting is because with less neurons in the hidden parts there is less complexity the networks learns, and then an averaged result is computed.

## Initialising the weights

The easiest way to initialise the network weights is to extract them at random from a Gaussian distribution. If you choose a Gaussian with standard deviation 1 for all neurons, you end up with the variable $$\sum_j w_j x_j + b$$being distributed with a Gaussian which is very broad. This will make for easy saturation in several neurons as due to this broadness the probability to have large values is not so small and so the result of the sigmoid function will be easily close to 0 or 1.

To prevent this, the usual choice is to extract the weights from a Gaussian with standard deviation equal to $$\frac{a}{\sqrt{n_{in}}}$$,$$n_{in}$$being the number of input weights in the neuron.

## Augmenting the training set

The main reason why neural networks typically require lots of training data is because they have to learn so many parameters. Augmenting the training set by perturbing it to create new, artificial data points is a usual trick. For instance, in the case of images, you can slightly rotate them to create new ones.

## References

1. M Nielsen, [**Neural networks and deep learning**](http://neuralnetworksanddeeplearning.com/), 2017

