# Naive Bayes

For the Bayes' theorem, refer to page

{% page-ref page="../../probability-statistics-and-data-analysis/methods-theorems-and-laws/the-bayes-theorem.md" %}

The Naive Bayes is a probabilistic classifier based on \(surprise surprise!\) the Bayes' theorem and it uses a Maximum A Priori estimate to classify the labels.

In a nutshell, its properties are:

* It assumes independence among features used for the classification;
* It is usually used for text classification;
* Is fast;
* Requires small training data;
* The probability of the outcome classification is unreliable.

## How does it work

Given a target variable$$y$$\(the class\) and features$$x_1, x_2, \ldots, x_n$$, by Bayes' theorem we can write

$$
P(y \ | \  x_1, x_2, \ldots, x_n) = \frac{P(x_1, x_2, \ldots, x_n \ | \ y) P(y)}{P(x_1, x_2, \ldots, x_n)} \ ,
$$

$$P(y)$$being the frequency of the class$$y$$.

The _naive_ assumption of the algorithm is that features are independent of each other, that is, the likelihood at the second member can be factorised into the product of the likelihoods of single features:

$$
P(x_i | y, x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n) = P(x_i | y) \ \ \ \forall i \ .
$$

This way, we can simplify and write

$$
P(y \ | \ x_1, \ldots, x_n) = \frac{\prod_{i=1}^{i=n} P(x_i \ | \ y) P(y)}{P(x_1, \ldots, x_n)} \ ,
$$

We apply the MAP estimation \(see page\) to find the$$y$$that maximises the posterior. The denominator only gives a constant of normalisation, so the maximising value is found via

$$
\hat{y} = arg \max_y P(y) \prod_{i=1}^{i=n} P(x_i | y)
$$

What this means is that the classifier assigns the class label$$\hat y$$as the one which maximises the posterior probability.

{% page-ref page="../../probability-statistics-and-data-analysis/methods-theorems-and-laws/the-maximum-likelihood-maximum-a-posteriori-and-expectation-maximisation-estimation-methods.md" %}

## The different classifiers in the family \(some cases\)

The different Naive Bayes classifiers differ in the assumptions for the likelihood distribution $$P(x_i | y)$$ .

### Gaussian Naive Bayes

In a Gaussian Naive Bayes, it is assumed to be a gaussian:

$$
P(x_i | y) = \frac{1}{\sqrt{2 \pi \sigma_y^2}} e^{- \frac{(x_i - \mu_y)^2}{2 \sigma_y^2}} \ ,
$$

with parameters$$\mu_y$$and $$\sigma_y$$ being the mean and the standard deviation of feature$$x_i$$in class$$y$$ , estimated using the Maximum Likelihood estimation.

### Bernoulli Naive Bayes

In a Bernoulli Naive Bayes, used when features are binary, it is assumed that

$$
P(x_i | y) = P(i | y) x_i + (1 - P(i | y))(1-x_i) \ .
$$

### Multinomial Naive Bayes

In a Multinomial Naive Bayes, with feature vector $$\mathbf{x}$$ and$$k_i$$being the number of successes for variable $$x_i$$, the likelihood is given as

$$
P(\mathbf{x} | y_k) = \frac{\Big(\sum_i x_i\Big)!}{\prod_i x_i!} \prod p_{k_i}^{x_i}
$$

Note that the multinomial Naive Bayes classifier becomes a linear classifier when expressed in logarithmic scale:

$$
\begin{align} \log P(yk | \mathbf{x}) &\propto \log \Big[p(y_k) \prod{i=1}^n p{k_i}^{x_i}\Big] \\ &= \log p(y_k) + \sum{i=1}^n xi \log p{k_i} \\ &= b + \mathbf{w}_k^t \mathbf{x} \end{align}
$$

with $$b = \log p(y_k)$$ __\(a constant\) __and __$$\mathbf{w}_k = \log p{k_i}$$.

## Regularised Naive Bayes: the smoothing

If in the training data there is no value for which feature$$x_i$$is determined by the class $$y$$ , meaning there is no occurrences where feature and class are together, the likelihood would equal zero: this is a problem as there would be a zero in the multiplication.

A correction to remedy this problem \(_regularised Naive Bayes_\) is obtained via adding an addend in the calculation of the likelihood as a frequency so as to have a small but non-zero probability. While in general we would calculate it as

$$
p_i = \frac{n_i}{n_y}  \ ,
$$

where$$n_i$$is the number of times feature$$x_i$$appears in the sample for class $$y$$ in the training set and $$n_y$$ is the total count of occurrences of class $$y$$, we smoothen as

$$
p_i = \frac{n_i + \alpha}{n_y + \alpha n}
$$

where $$\alpha$$ is a chosen factor and $$n$$ the number of possible values for feature $$x_i$$ . This procedure is called _Lidstone smoothing_, with $$\alpha = 1$$ it's the _Laplace smoothing_.

## An example: sex classification

This small example, as well as the ones below are taken and reworked from [the Wikipedia page on the topic](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Sex_classification). 

The problem is classifying if a person is a male \(M\) or a female \(F\) based on height \(h, in feet\), weight \(w, in pounds\) and foot size \(f, in inches\). This is the training data we assume to have collected:

| Gender | h \(feet\) | w \(lbs\) | f \(inches\) |
| :--- | :---: | :---: | :---: |
| M | 6 | 180 | 12 |
| M | 5.92 | 190 | 11 |
| M | 5.58 | 170 | 12 |
| M | 5.92 | 165 | 10 |
| F | 5 | 100 | 6 |
| M | 5.5 | 150 | 8 |
| M | 5.42 | 130 | 7 |
| M | 5.75 | 150 | 9 |

We use a gaussian assumption, so we assume the likelihood for each feature to be

$$
P(x_i | y) = \frac{1}{\sqrt{2 \pi \sigma_y^2}}  e^{- \frac{(x_i - \mu_y)^2}{2 \sigma_y^2}}
$$

and we estimate the parameters of said gaussians via MLE \(see page\), obtaining:

| Gender |  $$\mu_h$$  |  $$a = b$$  |  $$\mu_w$$  |  $$\sigma^2_w$$  |  $$\mu_f$$  |  $$\sigma^2_f$$  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| M | 5.86 |  $$3.5 \cdot 10^{-2}$$  | 176.25 |  $$1.23 \cdot 10^2$$  | 11.25 |  $$9.19 \cdot 10^{-1}$$  |
| F | 5.42 |  $$9.72 \cdot 10^{-2}$$  | 132.5 |  $$5.58 \cdot 10^2$$  | 7.5 | 1.67 |

The two classes are equiprobable because we got the same number of training points for each, so$$a = b$$, and these are the priors for each class. Note that we could also give the priors from the population, assuming that each gender is equiprobable.

Now, given a new sample point whose height is 6 feet, weight 130 lbs and foot size 8 inches, we want to classify its gender, so we determine which class maximises the posterior:

$$
P(M | h, w, f) = \frac{P(h, w, f | M) P(M)}{P(E)} \ ,
$$

where, under the Naive Bayes assumption,

$$
P(h, w, f | M) = P(h | M) P(w | M) P(f | M) \ ,
$$

and

$$
P(E) = P(h, w, f | M)P(M) + P(h, w, f | F)P(F) \ ,
$$

which is just a normalising constant so can be ignored. Now,

$$
P(h | M) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{- \frac{(6 - \mu)^2}{2 \sigma^2}} \approx 1.5789
$$

In the same way we compute $$P(w | M) = 5.9881 \cdot 10^{-6}$$and$$P(f | M) = 1.3112 \cdot 10^{-3}$$, so that in the end we obtain$$P(M | h, w, f) = 6.1984 \cdot 10^{-9}$$. Similarly we get$$P(F | h, w, f) = 5.3779 \cdot 10^{-4}$$, which is larger so we predict that the sample is a female.

## Other examples, on classifying text

### Spam filter

This is a common application of a Naive Bayes classifier and it is a case of text classification.

Some words are more frequent than others in spam e-mails \(for example "Viagra" is definitely a recurring word in spam e-mails\). The user manually and continuously trains the filter of their e-mail provider by indicating whether a mail is spam or not. For all words in each training mail, the filter then adjusts the probability that it will appear in a spam or legitimate e-mail.

Let S be the event that an e-mail is spam and$$w$$a word, then we compute the probability that an e-mail is spam given that it contains$$w$$as \( $$\neg S$$ is the event that mail is not spam, or "ham"\):

$$
P(S | w) = \frac{P(w | S) P(S)}{P(w | S) P(S) + P(w | \neg S) P(\neg S)} \ ,
$$

where$$P(S)$$, the prior, is the probability that a message is spam in general, and$$P(w | S)$$is the probability that$$w$$appears in spam messages.

A non biased filter will assume$$P(S) = P(\neg S) = 0.5$$, biased filters will assume higher probability for mail being spam.$$P(S | w)$$is approximated by the frequency of mails containing word$$w$$and being identified as spam in the learning phase, and similarly for $$P(w | \neg S)$$.

Now, this is valid for a single word, but a functional spam classifier uses several words and a Naive Bayes hypothesis, assuming that the presence of each word is an independent event. Note that this is a crude assumption as in reality in natural language words co-occurrence is key. Nevertheless, it is a useful idealisation, useful for the calculation in the Naive Bayes fashion.

So, with more words considered and asusming the priors are the same \(see [references](naive-bayes.md#references)\),

$$
P(S | w_1, \ldots, w_n) = \frac{P(w_1 | S) \cdots P(w_N | S)}{P(w_1 | S) \cdots P(w_N | S) + P(w_1 | \neg S) \cdots P(w_N | \neg S)}
$$

## Text classification

Given texts which can fall into categories \(for example literary genres\), we use

$$
P(C | w_1, \ldots, w_n) = \frac{\Pi_{i=1}^n P(w_i | C) P(C)}{\mathcal{N}}
$$

with$$C$$being the genre,$$w_i$$the words and the denominator is an irrelevant factor.

With a bag of words approach, if we have a training set$$D$$and a vocabulary$$V$$containing all the words in the documents, considering$$D_i$$the subset of texts in category$$C_i$$, then

$$
P(C_i) = \frac{|D_i|}{|D|}
$$

\(fraction of samples in category$$C_i$$\). Now, we concatenate all documents in$$D_i$$, obtaining$$n_i$$words and $$\forall w_j \in V$$ we call$$n_{ij}$$the number of occurrences of$$w_j$$in$$D_i$$, so

$$
P(w_j | C_i) = \frac{n_{ij} + 1}{n_i + |V|}
$$

\(we use smoothing\). The predicted category is then

$$
arg \max_{C_k \in \mathcal{C}} P(C_k) \Pi_{i=1}^n P(w_i | C_k)
$$

## References

1. P Graham, [A Plan for Spam](http://www.paulgraham.com/spam.html), 2002

{% page-ref page="../../probability-statistics-and-data-analysis/methods-theorems-and-laws/the-maximum-likelihood-maximum-a-posteriori-and-expectation-maximisation-estimation-methods.md" %}



