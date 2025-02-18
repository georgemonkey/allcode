import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np
import sklearn.model_selection as ms
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/national-history.csv')

print(data.info())


data=data[["date","deathIncrease","inIcuCumulative","inIcuCurrently","hospitalizedIncrease","hospitalizedCurrently","hospitalizedCumulative","negative","negativeIncrease","onVentilatorCumulative","onVentilatorCurrently","positive","positiveIncrease","states","totalTestResults","totalTestResultsIncrease","death"]]
for j in range(420):
    data.loc[j,"date"]=j+1
array=data.values

print("X------------------")
X=array[:,0:16]
print(X)
y=array[:,16]
print(y)

y=y.astype(float)
y=np.nan_to_num(y)
print(y)
print("Y-------------------")
X=X.astype(float)
X=np.nan_to_num(X)
print(X,"Data With NaN data removed")
print(array[:,0])

X_train,X_test,y_train,y_test=ms.train_test_split(X,y,train_size=0.80,test_size=0.20,random_state=1)

print("x_train:---",X_train)
print("y_train----",y_train)
print("x_test---",X_test)
print("y_test---",y_test)

model=[]
from sklearn.svm import SVC
model.append(SVC(gamma="auto"))

from sklearn.linear_model import LogisticRegression
model.append(LogisticRegression(solver="liblinear",multi_class="ovr"))

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model.append(LinearDiscriminantAnalysis())

from sklearn.neighbors import KNeighborsClassifier
model.append(KNeighborsClassifier())

from sklearn.tree import DecisionTreeClassifier
model.append(DecisionTreeClassifier())

from sklearn.naive_bayes import GaussianNB
model.append(GaussianNB())
from sklearn.tree import DecisionTreeRegressor
model.append(DecisionTreeRegressor(random_state=42))

print(model)
list_result=[]
for i in model:
    result=ms.cross_val_score(i,X_train,y_train,cv=10,scoring="accuracy")
    print(result)
    avg=(sum(result)/len(result))

    print("AVG-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0")
    list_result.append(avg)
print(list_result)
print(model)

plt.bar(["SVC","LR","LD","KN","DT","GB","DTR"],list_result,data=list_result)
plt.show()

#best_model=max(list_result)
#print(best_model)
d1={model[k]:list_result[k]for k in range(len(model))}
print(d1)
for val in d1.items():
    (model1,acc)=val
    if acc==max(d1.values()):
        print((f"IDEAL MODEL0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0 {model1}"))
#        break

model1.fit(X_train,y_train)
predictions=model1.predict(X_test)
print("Predictions: ",predictions)
print("CrossCheck Y Test: ", y_test)
l1=[]
for i in range(0,len(predictions)):
    if predictions[i] == y_test[i]:
        l1.append(1)
    else:
        l1.append(0)

print(sum(l1),"out of",len(predictions))
print("Accuracy: ",sum(l1)/len(predictions))

plt.scatter(y_test,predictions)
plt.ylabel("Machine")
plt.xlabel("Data")
x_lim=plt.xlim()
y_lim=plt.ylim()
plt.plot(x_lim,y_lim,"k--")
plt.show()

