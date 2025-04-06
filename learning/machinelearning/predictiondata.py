import tkinter
import pandas as pd
import sklearn.model_selection as ms
from tkinter import messagebox
import matplotlib as plt
data=pd.read_csv("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code 2/ML/seaborn-data-master/iris.csv")
print(data)
print(data.info())
array=data.values
print(array)
print("---------------------------------------------------------------------------------")
X=array[:,0:4]
print(X)
print("------------------------------------------------------------------------------------------------------------")
y=array[:,4]
print(y)


X_train,X_test,y_train,y_test=ms.train_test_split(X,y,train_size=0.80,test_size=0.20,random_state=1)
print("x_train:----",X_train)
print("y_train:----",y_train)
print("x_test:----",X_test)
print("y_test:----",y_test)
print(y_train.shape)
print(X_train.shape)
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

print(model)
list_result=[]
for i in model:
    result=ms.cross_val_score(i,X_train,y_train,cv=10,scoring="accuracy")
    print(result)
    average=(sum(result)/len(result))
    print(average)
    list_result.append(average)
print(list_result)
print(model)
import matplotlib.pyplot as plt
plt.bar(["SVC","LR","LD","KN","DT","GB"],list_result,data=list_result)
plt.show()
best_model=max(list_result)
print(best_model)
d1={model[k]:list_result[k]for k in range(len(model))}
print(d1)
for val in d1.items():
    (model,acc)=val
    if acc==max(d1.values()):
        print((f"The Highest Accurate Model Is: {model}").format())
        break





    
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Predictions: ", predictions)
print("Crosscheck Y Test: ", y_test)
l1=[]
for i in range(0,len(predictions)):
   

    if predictions[i]==y_test[i]:
        l1.append(1)
    else:
        l1.append(0)
print(sum(l1),"out of",len(predictions))
print("Accuracy: ",sum(l1)/len(predictions))
print(0.9833333333333332-0.9666666666666667)
plt.scatter(predictions,y_test)
plt.xlabel("Prediction Made By Machine")
plt.ylabel("Real Output")
x_lim=plt.xlim()
y_lim=plt.ylim()
plt.plot(x_lim,y_lim,"k--")

plt.show()
