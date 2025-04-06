import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/DataSets/seaborn-data-master/diamonds.csv")
"""
print("DATA")
print(data)
print(data.info())
data["price"] = data["price"].astype(float)
print(data["price"])
print(data)
print(data.info())
print(data.describe())
print("CUT-------------------------")
print(data["cut"].value_counts())
for j in data.index:
    if data.loc[j,"cut"] =="Ideal":
        data.loc[j, "cut"] = 1
    elif data.loc[j,"cut"] =="Premium":
        data.loc[j, "cut"] = 2
    elif data.loc[j,"cut"] =="Very Good":
        data.loc[j, "cut"] = 3
    elif data.loc[j,"cut"] =="Good":
        data.loc[j, "cut"] = 4
    elif data.loc[j,"cut"] =="Fair":
        data.loc[j, "cut"] = 5
print(data)

print("COLOR----------------------------")
print(data["color"].value_counts())

for j in data.index:
    if data.loc[j,"color"]=="D":
        data.loc[j,"color"]= 1
    elif data.loc[j,"color"]=="E":
        data.loc[j,"color"]= 2
    elif data.loc[j,"color"]=="F":
        data.loc[j,"color"]= 3
    elif data.loc[j,"color"]=="G":
        data.loc[j,"color"]= 4
    elif data.loc[j,"color"]=="H":
        data.loc[j,"color"]= 5
    elif data.loc[j,"color"]=="I":
        data.loc[j,"color"]= 6
    elif data.loc[j,"color"]=="J":
        data.loc[j,"color"]= 7
        
print(data)
print("CLARITY---------------------------------")
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

#data.hist(bins=50,figsize=(20,15))
#plt.show()

cm=data.corr()
import seaborn as sns

plt.subplots(figsize=(10,8))
sns.heatmap(cm,annot=True)
plt.show()
"""
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
    
for j in data.index:
    if data.loc[j,"color"]=="D":
        data.loc[j,"color"]= 1
    elif data.loc[j,"color"]=="E":
        data.loc[j,"color"]= 2
    elif data.loc[j,"color"]=="F":
        data.loc[j,"color"]= 3
    elif data.loc[j,"color"]=="G":
        data.loc[j,"color"]= 4
    elif data.loc[j,"color"]=="H":
        data.loc[j,"color"]= 5
    elif data.loc[j,"color"]=="I":
        data.loc[j,"color"]= 6
    elif data.loc[j,"color"]=="J":
        data.loc[j,"color"]= 7

for j in data.index:
    if data.loc[j,"cut"] =="Ideal":
        data.loc[j, "cut"] = 1
    elif data.loc[j,"cut"] =="Premium":
        data.loc[j, "cut"] = 2
    elif data.loc[j,"cut"] =="Very Good":
        data.loc[j, "cut"] = 3
    elif data.loc[j,"cut"] =="Good":
        data.loc[j, "cut"] = 4
    elif data.loc[j,"cut"] =="Fair":
        data.loc[j, "cut"] = 5

data=data[["carat","cut","color","clarity","depth","table","x","y","z","price"]]
print(data)






#SLICING
array=data.values
print(array)

#print("XDATA=================================================")
X=array[:,0:9]
#print(X)
#print("YDATA========================================================")
Y=array[:,9]
#print(Y)

#VISUALATION

from pandas.plotting import scatter_matrix
#scatter_matrix(data,diagonal="hist")
#plt.show()

#SPLITING DATA
import sklearn.model_selection as ms
X_train,X_test,y_train,y_test=ms.train_test_split(X,Y,train_size=0.80,test_size=0.20,random_state=1)
#print("x_train---",X_train)
#print("y_train---",y_train)
#print("x_test:---",X_test)
#print("y_test:---",y_test)

#EVALUTION 



from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor(random_state=42)
result=ms.cross_val_score(model,X_train,y_train,cv=2,scoring="neg_mean_squared_error")
print(result)


#PREDICTION

model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Predictions: ",predictions)
print("Real Data: ",y_test)
l1=[]
for i in range(0,len(predictions)):

    if predictions[i]==y_test[i]:
        l1.append(1)
    else:
        l1.append(0)

print(sum(l1),"out of",len(predictions))
print("Accuracy: ", sum(l1)/len(predictions))

plt.scatter(predictions,y_test)
plt.xlabel("Predicted Output")
plt.ylabel("Real Output")
x_lim=plt.xlim()
y_lim=plt.ylim()
plt.plot(x_lim,y_lim,"k--")
plt.show()




