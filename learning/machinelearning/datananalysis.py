import pandas as pd

data=pd.read_csv("/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv")
"""
print(data)
print(data.info())
print(data.shape)
print(data.head(20))
print(data.tail(20))
print(data.describe())
"""
print(data.columns.dtype)
for i in data.columns:
    list1 = list(data.columns)
    if data[i].dtype == "object":
        print(i)
        list1.remove(i)
print(list1)
data = data[list1]
print(data)

corr_matrix=data.corr()
import seaborn as sns
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True)
plt.show()
