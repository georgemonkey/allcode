import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.model_selection as ms
import tkinter as tk
import matplotlib.pyplot as plt 
from tkinter import messagebox
from tkinter import filedialog
root= tk.Tk()
root.title("ML")
root.geometry("500x600")

def importdata():
    print("Hi There")
    global data
    filename=filedialog.askopenfilename(initialdir="/",filetypes=((("All Files", "*.*"),("Text Files", "*.txt*"))))
    print("FileName: ",filename)
    
    data=pd.read_csv(filename)
    messagebox.showinfo(title="Success!",message="Data Successfully Imported!")
    print(data)

importbtn=tk.Button(root,text="Import Data", command=importdata)
importbtn.place(x=0,y=0)    

def datacon():
    global array
    array=data.values
    messagebox.showinfo(title="Success!",message="Data Successfully Converted!")
    print(array)

dataconbtn=tk.Button(root,text="Data Conversion",command=datacon)
dataconbtn.place(x=0,y=50)


def dataprep():
    col=0
    col=dataprepinput.get()
    a=int(col)
    global X
    global y
    X=array[:,0:a]
    y=array[:,a]
    messagebox.showinfo(title="Success!",message="Data Successfully Prepared!")
    print(X)
    print(y)

datapreplabel=tk.Label(root,text="Enter Number Of Independent Columns")
datapreplabel.place(x=0,y=100)
dataprepinput=tk.Entry(root)
dataprepinput.place(x=250,y=100)
dataprepbtn=tk.Button(root,text="Prepare Data", command=dataprep)
dataprepbtn.place(x=0,y=125)

def datatrain():
    global X_train
    global X_test
    global y_train
    global y_test
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,train_size=0.80,random_state=1)
    messagebox.showinfo(title="Success!",message="Data Successfully Trained!")
    print(X_train,X_test,y_train,y_test)

datatrainbtn=tk.Button(root, text="Train", command=datatrain)
datatrainbtn.place(x=0,y=175)

def datatest():
    global result5
    global model
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
            real=(f"The Highest Accurate Model Is: {model}").format()
            

    from sklearn.tree import DecisionTreeClassifier
    model5=DecisionTreeClassifier()
    result5=ms.cross_val_score(model5,X_train,y_train,cv=10,scoring="accuracy")
    print(result5)
    print(sum(result5)/len(result5))
    
    messagebox.showinfo(title="Model Accuracy",message=result5[1])
    messagebox.showinfo(title="Model Select",message=real)  

datatestbtn=tk.Button(root,text="Evaluate Data", command= datatest)
datatestbtn.place(x=0,y=200)

def prediction():
    model.fit(X_train,y_train)
    predictions=model.predict(X_test)
    print("Predictions: ",predictions)
    print("Y Test Values: ", y_test)
    l1=[]
    for i in range(0,len(predictions)):

        if predictions[i] == y_test[i]:
            l1.append(1)
        else:
            l1.append(0)
    print(l1)
    outof=(sum(l1),"out of", len(predictions), "match with the real data")
    messagebox.showinfo(title="Predictions Below",message=outof)
    accuracy=("Accuracy: ",sum(l1)/len(predictions))
    messagebox.showinfo(title="Accuracy Below",message=accuracy)
    plt.scatter(predictions, y_test)
    plt.xlabel("Machine")
    plt.ylabel("Data")
    xlim=plt.xlim()
    ylim=plt.ylim()
    plt.plot(xlim,ylim,"k--")
    plt.show()
predictbtn=tk.Button(root,text="Predict", command=prediction)
predictbtn.place(x=0,y=225)


root.mainloop()
