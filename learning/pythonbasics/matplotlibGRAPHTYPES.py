import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import seaborn as sns 
from pandas.plotting import scatter_matrix

#PIE CHART
"""
data = pd.DataFrame({"mass": [0.5, 5, 6], "radius": [2450, 6050, 6380]}, index=["mercury", "venus", "earth" ])
print(data)
data.plot(kind = "pie", y = "radius", autopct = "%.2f")
plt.show()
"""

#SCATTER PLOT
"""
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')

print(data)
plt.scatter(x = data.sepal_length, y = data.sepal_width)
plt.show()
"""
#SCATTER KDE
"""
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')
print(data)

scatter_matrix(data, diagonal="kde")
plt.show()
"""
#HISTOGRAM KDE
"""
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')
print(data)

scatter_matrix(data, diagonal="hist")
plt.show()
"""

#ANDREWS CURVE
"""
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')
print(data)

pd.plotting.andrews_curves(data, "species")
plt.show()
"""

#BOOTSTRAP PLOT
"""
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')
print(data)

pd.plotting.bootstrap_plot(pd.Series(data["sepal_length"]))
plt.show()
"""

