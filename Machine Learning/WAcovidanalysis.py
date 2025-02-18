import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sklearn.model_selection as ms
import warnings
warnings.filterwarnings("ignore") 
#1. READING DATA

#defining data
data=pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/washington-history.csv') 

#getting info from data
print(data.info())

#understanding date column
print(data["date"].describe())

#printing columns
for i in data["death"]:
    print(i)





#2. CORRELATION MATRIX

#finding the correlation
#cm=data.corr()


#plt.subplots(figsize=(10,8))
#sns.heatmap(cm,annot=True)
#plt.show()

#3. VISUALATION

#data.plot(kind="hist",subplots=True, layout=(7,6),sharex=False,sharey=False)
#scatter_matrix(data,diagonal="hist")
#plt.show()


#4.SEQUENCING THE COLUMNS
for j in range(420):
    data.loc[j,"date"] = j+1

#sequencing the columns for the slicing part
data=data[["date","deathConfirmed","deathIncrease","deathProbable","hospitalized","hospitalizedCumulative","hospitalizedCurrently","hospitalizedIncrease","inIcuCumulative","inIcuCurrently","negative","negativeIncrease","negativeTestsAntibody","negativeTestsPeopleAntibody","negativeTestsViral","onVentilatorCumulative","onVentilatorCurrently","positive","positiveCasesViral","positiveIncrease","positiveScore","positiveTestsAntibody","positiveTestsAntigen","positiveTestsPeopleAntibody","positiveTestsPeopleAntigen","positiveTestsViral","recovered","totalTestEncountersViral","totalTestEncountersViralIncrease","totalTestResults","totalTestResultsIncrease","totalTestsAntibody","totalTestsAntigen","totalTestsPeopleAntibody","totalTestsPeopleAntigen","totalTestsPeopleViral","totalTestsPeopleViralIncrease","totalTestsViral","totalTestsViralIncrease","death"]]
#printing sequenced data
print(data)
#5. SLICING
#converting the datas values into an array
array=data.values
#printing the array
print(array)
#printing the x seperator
print("X----------------------------")
#creating the seperation between the x data which is columns 0 to 39
X=array[:,0:39]
#printing the seperated x values
print(X)
#printing the y seperator
print("y----------------------------")
#creating the seperation between the y data which is column 39 and 40
y=array[:,39]
#printing y
print(y)
#6. CONVERTING NAN TO NUM
#changing the y values nans to numbers
y=y.astype(float)
y=np.nan_to_num(y)
print(y)
#changing the x values nans to numbers
X=X.astype(float)
X=np.nan_to_num(X)
print(X,"jsalkdfjlaksjdlkasjdlkajslkjdalksjl")
print(array[:,0])

#7. SPLITING DATA
X_train,X_test,y_train,y_test=ms.train_test_split(X,y,train_size=0.80,test_size=0.20,random_state=1)


print("x_train:---",X_train)
print("y_train:---",y_train)
print("x_test:---",X_test)
print("y_test:---",y_test)

#7. EVALUATION
###SINGLE MODEL
#model=DecisionTreeRegressor(random_state=42)
#result=ms.cross_val_score(model,X_train,y_train,cv=10,scoring="accuracy")
#result=ms.cross_val_score(model,X_train,y_train,cv=10,scoring="neg_mean_squared_error")
#print(result)
###MANY MODELS
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
    
    print("############################AVERAGE",i,avg)
    list_result.append(avg)
print(list_result)
print(model)
import matplotlib.pyplot as plt
plt.bar(["SVC","LR","LD","KN","DT","GB","DTR"],list_result,data=list_result)
plt.show()
best_model=max(list_result)
print(best_model)
d1={model[k]:list_result[k]for k in range(len(model))}
print(d1)
for val in d1.items():
    (model,acc)=val
    if acc==max(d1.values()):
        print((f"-------------------------------------------Premier Model:  {model}").format())
        break


from sklearn.tree import DecisionTreeClassifier
model5=DecisionTreeClassifier()
result5=ms.cross_val_score(model5,X_train,y_train,cv=10,scoring="accuracy")
print(result5)
print(sum(result5)/len(result5))


#8. PREDICTION
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Predictions: ", predictions)
print("Croscheck Y Test: ", y_test)
l1=[]
for i in range(0,len(predictions)):
    if predictions[i]==y_test[i]:
        l1.append(1)
    else:
        l1.append(0)
print(sum(l1),"out of",len(predictions))
print("Accuracy: ",sum(l1)/len(predictions))
plt.scatter(predictions,y_test)
plt.xlabel("Machine")
plt.ylabel("Data")
x_lim=plt.xlim()
y_lim=plt.ylim()
plt.plot(x_lim,y_lim,"k--")
plt.show()

#9.REFINING SCORE 

l2=[]
for i in range(0,len(predictions)):
    #if predictions[i]>y_test[i]:
        #sub=predictions[i]-y_test[i]

    sub=y_test[i]-predictions[i]
    l2.append(sub)
print("Difference Between Real And Machine: ",l2)
#print(sum(l2),"out of",len(predictions))

#print("Accuracy: ",sum(l1)/len(predictions))

l3=[]
for i in range(0,len(predictions)):
    if predictions[i]>y_test[i]:
        sub=predictions[i]-y_test[i]
    else:
        sub=y_test[i]-predictions[i]
    l3.append(sub)
print("Difference Between Real And Machine: ",l3)
avg_diff=sum(l3)/len(l3)
print("AVG DIFF---------------------",avg_diff)

l4=[]
for i in range(0,len(predictions)):
    if predictions[i]>y_test[i]:
        sub=predictions[i]-y_test[i]
    else:
        sub=y_test[i]-predictions[i]
        acc=sub/y_test
        
    l4.append(acc)
print("Difference Between Real And Machine: ",l4)


