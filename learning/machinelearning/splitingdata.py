import pandas as pd
import sklearn.model_selection as ms
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
