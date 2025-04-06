import pandas as pd

data=pd.read_csv("/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/DataSets/seaborn-data-master/iris.csv")
print(data)

from matplotlib import pyplot 
#data.plot(kind="hist",subplots=True,layout=(2,2),sharex=False,sharey=False)
#data.plot(kind="kde",subplots=True,layout=(2,2),sharex=False,sharey=False)
#data.plot(kind="bar",subplots=True,layout=(2,2),sharex=False,sharey=False)
from pandas.plotting import scatter_matrix
scatter_matrix(data,diagonal="hist")
data.plot(x="sepal_length",y="sepal_width",kind="hist")
pyplot.show()