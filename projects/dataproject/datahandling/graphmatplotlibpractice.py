import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import seaborn as sns 
from pandas.plotting import scatter_matrix

"""


date = ["25/12", "26/12", "27/12", "28/12"]
temperature = [30,31,35,28]
plt.plot(date,temperature)
plt.show()
data = pd.read_csv('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/DataSets/seaborn-data-master/iris.csv')
print(data)
print(data.columns)

try:
    list1 = []
    list2 = []
    for i in data.columns:
        #print(i)
        #print(sum(data[i]))
        list1.append(sum(data[i]))
        list2.append(i)
except:
    pass
print(list1)
print(list2)
plt.bar(list2,list1)
plt.show() 

plt.bar(data.sepal_length, data.sepal_width)
plt.show()
"""
#SETUP
root = tk.Tk()
root.title("Graphing")
root.geometry("400x500")

#FUNCTIONS
def fileopen():
        try:
            global filename
            global data
            filename = filedialog.askopenfilename()
            print(filename)
            data = pd.read_csv(filename)
            print("donereading")
            PDI()
        except:
            pass
def plotgraph():
    XAXISP = XAXIS.get()
    YAXISP = YAXIS.get()
    print("------------------------------------")
    
    print(GT.get())
    if GT.get() == "Line Graph":
        plt.close()
        plt.plot(data[XAXISP],data[YAXISP])
        plt.show()
    elif GT.get() == "Bar Graph": 
        plt.close() 
        plt.bar(data[XAXISP],data[YAXISP])
        plt.show()
    elif GT.get() == "Distribution Graph (X-AXIS ONLY)": 
        plt.close() 
        sns.kdeplot(data[XAXISP])
        plt.show()
    elif GT.get() == "Histogram (X-AXIS ONLY)": 
        plt.close() 
        sns.histplot(data[XAXISP])
        plt.show()    
    elif GT.get() == "Pie Chart (X-AXIS ONLY)": 
        plt.close() 
        data.plot(kind="pie", y=XAXISP)
        plt.show()
    elif GT.get() == "Scatter Plot": 
        plt.close() 
        plt.scatter(x = data[XAXISP], y = data[YAXISP])
        plt.show()
    elif GT.get() == "Scatter KDE (NO X,Y-AXIS)": 
        plt.close() 
        scatter_matrix(data, diagonal="kde")
        plt.show()
    elif GT.get() == "Histogram KDE (NO X,Y-AXIS)": 
        plt.close() 
        scatter_matrix(data, diagonal="hist")
        plt.show()
    elif GT.get() == "Andrews Curve (X-AXIS STRING ONLY)": 
        plt.close() 
        pd.plotting.andrews_curves(data, XAXISP)
        plt.show()
    elif GT.get() == "Bootstrap Plot (X-AXIS)": 
        plt.close() 
        pd.plotting.bootstrap_plot(pd.Series(data[XAXISP]))
        plt.show()
    elif GT.get() == "Correlation Plot": 
        print(data.info())
        list1 = list(data.columns)
        for i in data.columns:
            list2 = list1
            if data[i].dtype == "object":
                list2.remove(i)
        data1 = data[list2]
        corr_matrix=data1.corr()
        
        plt.subplots(figsize=(10,8))
        sns.heatmap(corr_matrix,annot=True)
        plt.show()
    elif GT.get() == "Box Plot": 
        plt.close() 
        sns.boxplot(x=data[XAXISP], y=data[YAXISP])
        plt.show()
    elif GT.get() == "Pairwise Plot (NO X,Y-AXIS)": 
        plt.close() 
        sns.pairplot(data, kind = "kde", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
        plt.show()
    
def PDI():
    global GT
    GT = tk.StringVar()
    global XAXIS
    XAXIS = tk.StringVar()
    global YAXIS
    YAXIS = tk.StringVar()
    CB1 = ttk.Combobox(root, values = list(data.columns), textvariable=XAXIS)
    CB1.place(x=60, y=75)
    CB2 = ttk.Combobox(root, values = list(data.columns), textvariable=YAXIS)
    CB2.place(x=60, y=100)
    B3 = tk.Button(root, text="Plot Graph", command = plotgraph)
    B3.place(x=150,y=160)
    CB3 = ttk.Combobox(root, values = ["Line Graph", "Bar Graph", "Scatter Plot", "Box Plot", "Distribution Graph (X-AXIS ONLY)", "Histogram (X-AXIS ONLY)", "Pie Chart (X-AXIS ONLY)", "Bootstrap Plot (X-AXIS)", "Scatter KDE (NO X,Y-AXIS)", "Histogram KDE (NO X,Y-AXIS)","Pairwise Plot (NO X,Y-AXIS)", "Andrews Curve (X-AXIS STRING ONLY)", "Correlation Plot"], textvariable=GT)
    CB3.place(x=110, y=125)

#WINDOW
L1 = tk.Label(root, text="Import CSV File:   ")
L1.place(x=0, y=0)
B1 = tk.Button(root, text="Select File", command=fileopen)
B1.place(x=100,y=0)
L2 = tk.Label(root, text="Visualize Data: ")
L2.place(x=0, y=50)
L3 = tk.Label(root, text="X-Axis: ")
L3.place(x=10, y=75)
L4 = tk.Label(root, text="Y-Axis: ")
L4.place(x=10, y=100)
L5 = tk.Label(root, text="Type Of Graph: ")
L5.place(x=10, y=125)





#for i in data.columns:
    #B2 = tk.Button(root, text=data.columns[i], command=fileopen)
    #print(data.columns[i])
    #B2.place(x=100,y=0)

root.mainloop()


