# Feature Selection Techniques

## Subset selection methods

These methods are about selecting the best features for a task, those that give the strongest effects. In all methods a model is chosen that gives the best result, and for this task model selection techniques are used \(using the validation set\).

### Look at all combinations

What you could think of doing is, having $$p$$ initial features, looking at all possible combinations of them in terms of how the model performs. You'd have to create $${p}\choose{k}$$ with $$k = 1, 2, \ldots p$$ sets of predictors and fitting the model for each of these sets, then picking the set giving the best result for the model.

This procedure is very expensive.

### Forward stepwise selection

This procedure consists in adding one feature at a time until you added all $p$. In practice what you do is

1. At step $$k$$ , \( $$k \in (1, 2, \ldots p)$$ \) you have a model fitted with $$k$$ predictors
2. At step $$k+1$$ you have the sets of models fitted with one predictor more, for all possible choices of the new added feature and you choose the one giving the best result
3. At the very end, when you have all the models fitted with every $$k$$ number of features, you'll chose the very best one

This method is an approximation of the "look at all combinations one", but does not consider all possible combinations and for this so it's not guaranteed to find the best of all possible combinations adoptable.

### Backward stepwise selection

This method is the mirror one of the forward one from above: it removes one feature at a time, starting from the model which uses all the $$p$$ features. In the following steps, it works the same way.

It suffers from the same problem of the forwards stepwise, namely it is not guaranteed to find the best combination of features, but is computationally viable.

