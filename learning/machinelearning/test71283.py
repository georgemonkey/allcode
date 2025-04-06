import pandas as pd

data=pd.read_csv("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/ML/seaborn-data-master/diamonds.csv")
print(data["clarity"].value_counts())


for j in data.index:
    if data.loc[j,"clarity"]=="SI1":
        data.loc[j,"clarity"] = 1
    elif data.loc[j,"clarity"] == "VS2":
        data.loc[j,"clarity"] = 2    
    elif data.loc[j,"clarity"] == "SI2":
        data.loc[j,"clarity"] = 3
    elif data.loc[j,"clarity"] == "VS1":
        data.loc[j,"clarity"] = 4
    elif data.loc[j,"clarity"] == "VVS2":
        data.loc[j,"clarity"] = 5
    elif data.loc[j,"clarity"] == "VVS1":
        data.loc[j,"clarity"] = 6
    elif data.loc[j,"clarity"] == "IF":
        data.loc[j,"clarity"] = 7
    elif data.loc[j,"clarity"] == "I1":
        data.loc[j,"clarity"] = 8

print(data)