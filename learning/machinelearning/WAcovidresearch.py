import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sklearn.model_selection as ms
import warnings

warnings.filterwarnings("ignore") 


data=pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/washington-history.csv')

print(data.info())

for i in data["death"]:
    i=np.nan_to_num(i)

plt.plot(data["date"],data["death"])
plt.show()
for j in data["deathConfirmed"]:
    j = np.nan_to_num(j)
for q in data["hospitalized"]:
    q = np.nan_to_num(q)

plt.scatter(x=data["hospitalized"],y=data["deathConfirmed"])
plt.show