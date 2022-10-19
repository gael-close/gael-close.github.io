# Basics
import sys
import os
import numpy as np
import pandas as pd
from box import Box

# Unit 1
import forallpeople as si
from si_prefix import si_format

si.environment("default", top_level=False)

# Unit 2: see https://pint.readthedocs.io/en/0.10.1/tutorial.html#using-pint-in-your-projects
from pint import UnitRegistry, set_application_registry
import pint_pandas

ureg = UnitRegistry()
ureg.default_format = "~"
set_application_registry(ureg)
pint_pandas.PintType.ureg = ureg

# Plots
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import hvplot.pandas
import holoviews as hv  # Load w/ hv.extensions('bokeh') in notebook

# Display
from IPython.display import IFrame, HTML, Image, Markdown


# Magic (use plain python syntax)
import builtins
from IPython import get_ipython

if get_ipython() is not None:
    get_ipython().run_line_magic("matplotlib", "inline")
    get_ipython().run_line_magic("config", "InlineBackend.figure_format='retina'")

# Ignore warnings
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
import logging

logging.getLogger("param").setLevel(logging.ERROR)

# Styles
# https://matplotlib.org/stable/gallery/style_sheets/bmh.html
plt.style.use("bmh")
mpl.rcParams["font.family"] = "Source Sans Pro"
mpl.rcParams["axes.facecolor"] = "white"
my_table_class = 'class="table table-striped table-bordered table-sm"'

# Test plot
# from http://seaborn.pydata.org/tutorial/aesthetics.html?highlight=sine%20plot
def my_sineplot():
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i))
    plt.xlabel(r"Angle $\theta$ [rad]")  # raw string to rende latex
    plt.ylabel("Y [a.u]")
    plt.title("Test Plot")


# Helper functions
def apply_func_df(func):
    def wrapper(df, dd, **kwargs):
        Y = df.apply(func, dd=dd, **kwargs, axis=1, result_type="expand")
        return df.drop(columns=Y.columns, errors="ignore").join(Y)

    wrapper.__wrapped__ = func
    return wrapper


def nest_columns(df, split="."):
    """Nest columns hierarchically"""
    df.columns = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.columns.values))
    )
    return df


def nest_index(df, split="."):
    """Nest columns hierarchically"""
    df.index = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.index.values))
    )
    return df


def my_stack(
    df,
    level="parameter",
    value="value",
):
    """Stack a dataframe. The column keys are stacked under a new level.
    The values are retained in the column named value."""
    df_2 = df.copy()
    df_2.columns.name = level
    df_2 = df_2.stack(dropna=False).to_frame(value)
    return df_2


def print_git_version():
    from git import Repo

    repo = Repo(".", search_parent_directories=True)
    version = repo.git.describe("--tags", "--always", "--dirty")
    return Markdown(f"Git version\n: `{version}`.")
