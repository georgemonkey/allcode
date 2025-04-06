import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import sklearn.model_selection as ms
from sklearn.linear_model import LogisticRegression
#storing data
data=pd.read_csv("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/DataSets/seaborn-data-master/geyser.csv")
#printing data
print(data)
#printing data info
print(data.info())
#printing avg max min...
print(data.describe())
#correlation matrix
corr_matrix=data.corr()
"""
#configuring heatmap
plt.subplots(figsize=(10,8))
#creating heatmap
sns.heatmap(corr_matrix,annot=True)
#displaying heatmap
plt.show()
#creating kde
data.plot(kind="kde",subplots=True,layout=(2,2),sharex=False,sharey=False)
#displaying kde
plt.show()
#creating scatter matrix
scatter_matrix(data,diagonal="hist")
#displaying scatter matrix
plt.show()
"""
#slice
array=data.values
print(array)

#printing x
print("X Data")
X=array[:,0:2]
print(X)

#printing y
print("Y Data")
Y=array[:,2]
print(Y)

#printing y shape
print("Y Shape")
print(Y.shape)

#printing x shape
print("X Shape")
print(X.shape)


X_train,X_test,y_train,y_test=ms.train_test_split(X,Y,train_size=0.80,test_size=0.20,random_state=1)
print("x_train:***********",X_train)
print(X_train.shape)
print("y_train:***********",y_train)
print(y_train.shape)
print("x_test:***********",X_test)
print(X_test.shape)
print("y_test:***********",y_test) 
print(y_test.shape)
"""
#creates the logistic regression model
model2=LogisticRegression(solver="liblinear",multi_class="ovr")
#generates the result from using the logistic regression model
result2=ms.cross_val_score(model2,X_train,y_train,cv=10,scoring="accuracy")
#converting in a decimal
print("%"+sum(result2)/len(result2)*100)
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
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Predictions Made By Computer: ", predictions)
print("Real Data: ",y_test)
l1=[]
for i in range(0,len(predictions)):

    if predictions[i]==y_test[i]:
        l1.append(1)
    else:
        l1.append(0)

print(sum(l1),"out of", len(predictions))
print("Accuracy Comaparing Machine Results To Real Data", sum(l1)/len(predictions))
plt.scatter(predictions,y_test)
plt.xlabel("Prediction Outputted By Machine")
plt.ylabel("Real Output")
x_lim=plt.xlim()
y_lim=plt.ylim()
plt.plot(x_lim,y_lim,"k--")
plt.show()