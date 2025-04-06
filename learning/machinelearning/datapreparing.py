import pandas as pd

data=pd.read_csv("/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/DataSets/seaborn-data-master/iris.csv")
print(data)
#print(data.info())
array=data.values
print("Array")
print(array)
print("---------------------------------------X-----------------------------------------")
X=array[:,0:4]
print(X)
print("------------------------------------------Y-----------------------------------------")
Y=array[:,4]
print(Y)
