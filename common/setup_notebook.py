# Methods to set the notebook up
# Note that these have to be called in order


from IPython.core.display import HTML
from IPython.core.interactiveshell import InteractiveShell

import json
import matplotlib
from matplotlib import pyplot as plt


def config_ipython():

    # Print vars on multiple lines in same cell without "print"
    InteractiveShell.ast_node_interactivity = "all"



def setup_matplotlib(matplotlib_file_path='../styles_files/matplotlibrc.json'):
    """
    Setup all the stylistic params of matplotlib.
    Pass the file path to the Matplotlib rcParams file.
    """

    # Overwrite rcParams with the custom style file
    params = json.load(open(matplotlib_file_path))
    matplotlib.rcParams.update(params)

    # Set ggplot style
    plt.style.use('ggplot')



def set_css_style(css_file_path='../styles_files/custom.css'):
    """
    Read the custom CSS file and load it into Jupyter.
    Pass the file path to the CSS file.
    """

    styles = open(css_file_path, "r").read()
    return HTML(styles)




