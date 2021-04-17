# Feature engineering techniques

## Feature Hashing

Feature hasing is a trick used to save space and to efficiently retrieve features in memory. What you do is applying a has function to the features and use their hash values as indices of a vector used to store all feature values. It is particularly useful in problem with large number of features.

For instance, feature _A_ gets hashed into 56, so it is index 56 of the vector to be updated.

## One-hot encoding

One-hot encoding is a procedure often used to transform categorical variables into numerical representations in order to use them as features in a model. The name is borrowed from the fact that _one-hot_ are groups of bits where there is only a 1 and all the rest is 0. On the flip side, _one-cold_ are bits where there is only a 0 among 1's. What you do to one-hot encode your variable is consider all the states in which it can be, use as many bits as there are states and for each different state you light up one of the bits. The table here reports the binary numbers 0-7 \(decimal and binary representations given\) encoded in a one-hot fashion: you have 8 states, so the one-hot representations is a string of 8 bits, and for each number you light up the corresponding one with a 1 while keeping all rest as 0.

| Decimal | Binary | One-hot |
| :--- | :--- | :--- |
| 0 | 000 | 00000001 |
| 1 | 001 | 00000010 |
| 2 | 010 | 00000100 |
| 3 | 011 | 00001000 |
| 4 | 100 | 00010000 |
| 5 | 101 | 00100000 |
| 6 | 110 | 01000000 |
| 7 | 111 | 10000000 |

Let's do an example with a proper categorical variable. Let's say one of the features you have is the status of the weather, and that it can take any of three states: sunny, cloudy, rainy. Using one-hot, you would encode it as

| Weather status | One-hotted |
| :--- | :---: |
| sunny | 001 |
| cloudy | 010 |
| rainy | 100 |

At the end, from one feature with 3 states, you end up with 3 features. This procedure adds dimensionality because there will be one feature per each of the states of the categorical variable, containing either a 0 pr a 1. In general, we go from$$n$$observations in$$d$$values to$$d$$binary variables with$$n$$observations each.

