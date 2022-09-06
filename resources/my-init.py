# basic
import numpy as np
import pandas as pd
# plots
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import hvplot.pandas 
import holoviews as hv 
# magic

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline');
get_ipython().run_line_magic('config', "InlineBackend.figure_format='retina'");
# hv.extension('bokeh')

# https://matplotlib.org/stable/gallery/style_sheets/bmh.html
plt.style.use('bmh')
mpl.rcParams['font.family'] = 'Source Sans Pro'


# from http://seaborn.pydata.org/tutorial/aesthetics.html?highlight=sine%20plot
def my_sineplot():
  x = np.linspace(0, 14, 100)
  for i in range(1, 7):
    plt.plot(x, np.sin(x + i * .5) * (7 - i))
  plt.xlabel('angle [rad]')
  plt.ylabel('Y [a.u]')
  plt.title('Test Plot')
  
