# Helper methods for NLTK


def measure_lexical_diversity(tokenized_string):
    """
    Given a tokenized string (list of tokens),
    return the fraction of unique tokens to total tokens.
    """
    return len(set(tokenized_string)) / len(tokenized_string)


def compute_perc_word_usage(word, tokenized_string):
    """
    Given a tokenized string (list of tokens),
    return the fraction of use of a given word as fraction of all tokens.
    """
    return tokenized_string.count(word) / len(tokenized_string)


def plot_freqdist_freq(fd,
                       max_num=None,
                       cumulative=False,
                       title='Frequency plot',
                       linewidth=2):
    """
    As of NLTK version 3.2.1, FreqDist.plot() plots the counts and has
    no kwarg for normalising to frequency. Work this around here.
    INPUT:
        - the FreqDist object
        - max_num: if specified, only plot up to this number of items
          (they are already sorted descending by the FreqDist)
        - cumulative: bool (defaults to False)
        - title: the title to give the plot
        - linewidth: the width of line to use (defaults to 2)
    OUTPUT: plot the freq and return None.
    """

    tmp = fd.copy()
    norm = fd.N()
    for key in tmp.keys():
        tmp[key] = float(fd[key]) / norm

    if max_num:
        tmp.plot(max_num, cumulative=cumulative,
                 title=title, linewidth=linewidth)
    else:
        tmp.plot(cumulative=cumulative, title=title, linewidth=linewidth)

    return
