# Helper methods for classification jobs

from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools



def do_plot_conf_mat(targets_true,
                     targets_pred,
                     labels=None,
                     normalize=False,
                     cmap=plt.cm.Blues):
    """
    Compute the confusion matrix of a classifier and plot it with overlayed numbers on each cell.
    Conf Mat will have the real targets on the rows and the predicted targets on the columns.
    INPUT:
        - the list of real targets for samples
        - the list of predictes samples for samples
        - the list of labels to be plotted in that order on the cells rows/colums
            * defaults to None, which will put cells in the sorted order of all targets found
              (all available classes will be used)
            * if list is given, this will automatically adjust cell values to those order
              because this is what confusion_matrix does automatically.
              In this case, you can pass a list containing only the classes of your interest for the matrix.
        - boolean about whether to normalize matrix (by row) or not (default:False)
        - the map of gradient colours to apply
    OUTPUT:
        - the conf matrix
    NOTEs:
        * overlayed numbers in the normalised case are printed with 2 decimal digits
        * gradient colourbar on the side will always report non-normalised values
        * If normalised, the diagonal of the conf mat will give the rate of correctly classified samples in each class
    """

    # Compute the confusion matrix
    cm = confusion_matrix(targets_true, targets_pred, labels=labels)

    # Set the title
    title = 'Confusion Matrix'

    if not labels:
        labels = sorted(list(set(targets_true) & set(targets_pred)))

    # Set plotting parameters
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    plt.xticks(tick_marks, labels, rotation=45)
    plt.yticks(tick_marks, labels)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        title += ', normalized (by row)'

    # this is for overlaying the numbers on cells
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, round(cm[i, j], 2),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.title(title)

    plt.show()

    return cm
