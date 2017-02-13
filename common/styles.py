# Methods to style the notebooks

from IPython.core.display import HTML
import json
import matplotlib


def set_css_style(css_file_path):
    """
    Read the custom CSS file and load it into Jupyter.
    Pass the file path to the CSS file.
    """

    styles = open(css_file_path, "r").read()
    return HTML(styles)


def setup_matplotlib(matplotlib_file_path):
    """
    Setup all the stylistic params of matplotlib.
    Pass the file path to the Matplotlib rcParams file.
    """

    # Overwrite rcParams with the custom style file
    params = json.load(open(matplotlib_file_path))
    matplotlib.rcParams.update(params)

    # Set the ggplot style
    matplotlib.pyplot.style.use('ggplot')

