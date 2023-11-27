#%% Library import------------------------------------------------------------:

    
import numpy as np 
import tkinter as tk 
from tkinter import ttk
import matplotlib as mpl
import matplotlib.pyplot as plt 

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


# Options to not show figures:
plt.ioff()
mpl.use('Agg')

#%%

# Plots: 
mpl.rcParams['image.cmap']      = 'seismic'
mpl.rcParams['lines.linewidth'] = 1.5
mpl.rcParams['pcolor.shading']  ='auto'

# Matlab default figure color cycler: 
    
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler('color', 
                                         ['#0072BD', '#D95319',
                                          '#EDB120', '#7E2F8E', 	
                                          '#77AC30', '#4DBEEE', 
                                          '#A2142F'])
