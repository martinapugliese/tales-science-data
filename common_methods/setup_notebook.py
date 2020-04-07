# Methods to set the notebook up
# Note that these have to be called in order


from IPython.core.display import HTML
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import set_matplotlib_formats

import json
import sys
import matplotlib
from matplotlib import pyplot as plt


# Name of this repo
REPO_NAME = 'tales-science-data/'

# Relative paths to style files
MATPLOTLIB_FILE = 'style-files/matplotlibrc.json'
CSS_FILE = 'style-files/custom.css'


def find_global_path():
    """
    Finds global path to this repo on machine.
    """
    for item in sys.path:
        if REPO_NAME in item:
            return item.split(REPO_NAME)[0] + REPO_NAME


def config_ipython():

    # Print vars on multiple lines in same cell without "print"
    InteractiveShell.ast_node_interactivity = "all"

    # Setting retina dispay quality for plots
    set_matplotlib_formats('retina')


def setup_matplotlib(matplotlib_file_path=MATPLOTLIB_FILE):
    """
    Setup all the stylistic params of matplotlib.
    Pass the file path to the Matplotlib rcParams file.
    """

    global_path = find_global_path()

    # Set ggplot style
    plt.style.use('ggplot')

    # Overwrite rcParams with the custom style file
    params = json.load(open(global_path + matplotlib_file_path, 'r'))
    matplotlib.rcParams.update(params)


def set_css_style(css_file_path=CSS_FILE):
    """
    Read the custom CSS file and load it into Jupyter.
    Pass the file path to the CSS file.
    """

    global_path = find_global_path()

    styles = open(global_path + css_file_path, 'r').read()
    return HTML(styles)
