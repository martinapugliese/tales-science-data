# The backpropagation mechanism

The backpropagation algorithm is the core of how artificial neural networks manage to _learn_, doing so by iteratively correcting the error between the actual value and the predicted value in a back-propagation fashion. The original paper proposing this now universally adopted mechanism is a [Nature](the-backpropagation-mechanism.md#references) from 1986 by Rumelhart, Hinton, Williams.

## What is it

The backpropagation algorithm is a brilliant way to train a network by perturbing each weight iteratively with an amount proportional to the partial derivative of the cost function with respect to it, propagating these derivatives backwards in the network. This is done to aid gradient descent and eventually train the network by reducing the error between what gets predicted and what the value is actually.

The idea per se is simple, the implementation is hard though and it took some research to figure out an efficient mechanism for it. Mechanism that arrived with the [Rumelhart & co. paper](the-backpropagation-mechanism.md#references) in 1986.

The reason why backpropagation is the core of the learning procedure of neural networks is that by adjusting the weights though little kicks and repeatedly, the hidden layers of the network come to _learn_ features. While what happens to the input and output layers is controllable, it is the hidden layer\(s\) that do all the painstaking work of representing the featured of the input data. If in a network there were no hidden layer, it would be easy to change the weights in such a way that the output matches the expected real output. But the network wouldn't be learning and wouldn't do anything worth of excitement. It is via backpropagation that the network can learn, in its hidden neurons, how to represent the data.

## The procedure in detail

### Prologue: gradient descent

The notes here will follow both the original paper cited above and [this very helpful paragraph on Wikipedia](https://en.wikipedia.org/wiki/Backpropagation#Finding_the_derivative_of_the_error) about the topic, and will refer to a feedforward network \(see page\) of sigmoid neurons \(see page\), however the backpropagation procedure applies to a generic activation function, so long as it's differentiable, but the sigmoid makes for very nice calculations.

{% page-ref page="artificial-neural-networks-in-a-nutshell.md" %}

{% page-ref page="../types-of-neurons-and-networks/the-sigmoid-neuron.md" %}

Let's consider the transmission of information to a neuron$$k$$in the $$l$$-th layer, we will use$$i$$to indicate an input and$$o$$to indicate an output, and will make use of this note to factor the bias inside the transfer function as a further weight. 

The neuron receives input from all the neurons in the previous,$$l-1$$-th layer as a weighted combination of their outputs as per activation function:

$$
i_k^l = \sum_i o_i^{l-1} w_{ik}^{l-1,l}
$$

where the apex indicates the layer we are referring to. Note that the weight $$w_{ik}^{l-1,l}$$ is meant to represent the weight of the connection between neuron$$i$$in layer$$l-1$$and our reference neuron$$k$$in layer$$l$$ .

As per output function, the output of$$k$$is \(using a sigmoid output function as per tradition, this will prove to be a very convenient choice later on\):

$$
o_k^l = \frac{1}{1 + e^{- \sum_i o_i^{l-1} w_{ik}^{l-1,l}}}
$$

The goal of training the network is finding the weights such that the network output is near the expected one. For this goal, we have to define a cost function which measures the difference between expected and obtained result, and minimise it. Now, the cost function can be given as the mean squared error

$$
E = \frac{1}{2n} \sum_i^n [o_i - e_i]^2 \ ,
$$

where the sum goes over all training samples,$$o$$is the network output for the sample and$$e$$the expected output. It gets minimised via gradient descent \(see page\), which requires calculating the partial derivatives of it with respect to all weights \(its parameters\).

{% page-ref page="../../machine-learning-concepts-and-procedures/learning-algorithms/the-gradient-descent-method.md" %}

Note that the cost function could in principle be given differently, as long as it satisfies two requirements:

1. it is differentiable
2. it can be written as a sum of contributions \(or, we can say as a mean\) of the single training data points

The first requirement is needed because as per gradient descent we will have to compute derivatives of the cost function; the second because we generalise the calculation to the whole training set by applying the sum over the calculations on a training data point.

Also note that in practice the version of gradient descent applied is the stochastic one.

### Calculating the derivatives of the cost function: backpropagation

Backpropagation propagates the partial derivatives of the cost function with respect to the parameter weights from the output layer back to the first one, iteratively. The derivative of the cost function with respect to a weight is computable via chain rule \(for simplicity, we are not indicating the layer\)

$$
\begin{equation}
    \frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial o_j} \frac{\partial o_j}{\partial i_j} \frac{\partial i_j}{\partial w_{ij}} \ ,
\end{equation}
$$

Now let's break down the components. For the last one, we have

$$
\frac{\partial i_j}{\partial w_{ij}} = o_i \ .
$$

For the second one, using the form of the activation function from above, we have \(you can easily prove that the equality is right\)

$$
\frac{\partial o_j}{\partial i_j} = o_j (1 - o_j) \ .
$$

We are left with calculating the first bit,$$\frac{\partial E}{\partial o_j}$$. The derivative of the cost function with respect to$$o_j$$can be calculated if we think of the cost as a function of all outputs of all the neurons in layer$$\bar{l}$$which receive input from neuron$$j$$,

$$
\frac{\partial E}{\partial o_j} = \frac{\partial E(\{o_k \forall k \in \bar l\})}{\partial o_j} \ ,
$$

which can be written as

$$
\frac{\partial E}{\partial o_j} = \sum_{k \in \bar l} \frac{\partial E}{\partial o_k} \frac{\partial o_k}{\partial o_j} = \sum_{k \in \bar l} \frac{\partial E}{\partial o_k} \frac{\partial o_k}{\partial i_k} \frac{\partial i_k}{\partial o_j} = \sum_{k \in \bar l} \frac{\partial E}{\partial o_k} \frac{\partial o_k}{\partial i_k} w_{jk}
$$

This recursive equation states that the derivative of the cost function with respect to$$o_j$$can be calculated from the same derivatives with respect to the output of neurons in the further layer.

This all can be written as

$$
\begin{equation}
    \frac{\partial E}{\partial w_{ij}} = o_i \delta_j \ ,
\end{equation}
$$

with

$$
\delta_j = \sum_{k \in \bar l} \delta_k w_{jk} o_j (1-o_j) \ ,
$$

and in the case of a neuron in the output layer things are much easier to compute, leading to $$\delta_j = (o_j-e_j)o_j(1-o_j)$$ .

These expression encapsulate the essence of backpropagation: you calculate the difference between the expected output and the obtained one and starting from the output layer you propagate the derivatives back in the network.$$\delta$$is the error we are propagating. We have to start from where we can compute it \(the output layer\) and then iteratively go back scaling the previous layers in order to obtain the calculation in the preceding layers.

Following the gradient descent procedure, we need to update the parameters of the cost function \(the weights\) by perturbing them by an amount proportional to the derivative via a learning rate:

$$
\Delta w_{ji} = - \alpha o_i \delta_j \ .
$$

## References

1. D E Rumelhart, G E Hinton, R J Williams, [**Learning representations by back-propagating errors**](http://www.cs.toronto.edu/~hinton/absps/naturebp.pdf), _Nature_, 323.6088, 1986
2. [**Nielsen's book on backpropagation**](http://neuralnetworksanddeeplearning.com/chap2.html)

