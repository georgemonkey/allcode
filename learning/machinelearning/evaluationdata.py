import tkinter
import pandas as pd
import sklearn.model_selection as ms
from tkinter import messagebox
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
"""
print("SVC--------------------------------------------------------")
from sklearn import datasets,linear_model
from sklearn.svm import SVC
model1=SVC(gamma="auto")
result1=ms.cross_val_score(model1,X_train,y_train,cv=10,scoring="accuracy")
print(result1)
#10,5,80,50
#i=10+5+80+50
#a=i/4
#print(a)
"""
#i=0
#length=len(result)
#r=0
##while i <length:
    
    #a=result[i]
    #r+=a
    #i+=1
#print(r/length)
###############


"""
print(sum(result1)/len(result1))
print("LogisticRegression--------------------------------------")
from sklearn.linear_model import LogisticRegression
model2=LogisticRegression(solver="liblinear",multi_class="ovr")
result2=ms.cross_val_score(model2,X_train,y_train,cv=10,scoring="accuracy")
print(result2)
print(sum(result2)/len(result2))
print("LinearDiscriminantAnalysis-----------------------------")
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model3=LinearDiscriminantAnalysis()
result3=ms.cross_val_score(model3,X_train,y_train,cv=10,scoring="accuracy")
print(result3)
print(sum(result3)/len(result3))
print("Neighbors---------------------------------")
from sklearn.neighbors import KNeighborsClassifier
model4=KNeighborsClassifier()
result4=ms.cross_val_score(model4,X_train,y_train,cv=10,scoring="accuracy")
print(result4)
print(sum(result4)/len(result4))
print("DecisionTreeClassifier-------------------------------")
from sklearn.tree import DecisionTreeClassifier
model5=DecisionTreeClassifier()
result5=ms.cross_val_score(model5,X_train,y_train,cv=10,scoring="accuracy")
print(result5)
print(sum(result5)/len(result5))
print("GaussianNB------------------------------------------")
from sklearn.naive_bayes import GaussianNB
model6=GaussianNB()
result6=ms.cross_val_score(model6,X_train,y_train,cv=10,scoring="accuracy")
print(result6)
print(sum(result6)/len(result6))
"""
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
        


from sklearn.tree import DecisionTreeClassifier
model5=DecisionTreeClassifier()
result5=ms.cross_val_score(model5,X_train,y_train,cv=10,scoring="accuracy")
print(result5)
print(sum(result5)/len(result5))