import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import IntVar
#import graphmatplotlibpractice as DA
def fileopen():
        try:
            global filename
            global data
            filename = filedialog.askopenfilename()
            print(filename)
            data = pd.read_csv(filename)
            print("donereading")
            
        except:
            pass

root = tk.Tk()
root.title("Graphing")
root.geometry("3008x1692")

fileopen()

cselector = tk.Tk()
cselector.title("Selector")
cselector.geometry("250x500")

num = 0 #replace with screen
list2 = []
def f1():
    list2.append(listbox.get(tk.ANCHOR))
    print(list2)
    
def f2():
    win1 = tk.Tk()
    data1=data[list2]
    #print(data1)
    cols= tuple(data1.columns)
    print(cols)
    listbox = ttk.Treeview(win1, columns=cols,show='headings',height=85)
    vsb = ttk.Scrollbar(win1, orient="vertical", command=listbox.yview)
    vsb.place(x=2990, y= 0, height = 1680)
    listbox.configure(yscrollcommand=vsb.set)
    listbox.place(x=0,y=0)

    for i in cols:
        listbox.heading(i,text=i)
        listbox.column(i,anchor='center')
        listbox.place(x=10,y=10)
    for row,cols in enumerate(data.values, start= 0):
        listbox.insert("","end",values=cols)
    win1.mainloop()


L1 = tk.Label(cselector, text="selection")
L1.place(x= 250, y= 1000)
list1 = []
listbox = tk.Listbox(cselector)
col = data.columns
for i in range(len(col)):
    listbox.insert(i, col[i])
listbox.place(x=0, y=0)
b1 = tk.Button(cselector,text="Add",command=f1)
b1.place(x=185, y=0)
b2 = tk.Button(cselector,text='Submit',command=f2)
b2.place(x=185,y=40)
cselector.mainloop()

cols = tuple(data.columns)
listbox = ttk.Treeview(root, columns=cols, show = "headings", height = 85)
vsb = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
###CREATE RESPONSIVE X-HEIGHT###
vsb.place(x=2990, y= 0, height = 1680)
listbox.configure(yscrollcommand=vsb.set)
# hsb = ttk.Scrollbar(root, orient = "horizontal", command=listbox.xview)
# hsb.pack(fill = "x")
# hsb.place(x=20, y= 500, width=1000)
# listbox.configure(xscrollcommand=hsb.set)


root.mainloop()

    # list1 = data[list2]
    # listbox = tk.Listbox(cselector)
    # cols = tuple(list2.columns)
    # for i in range(len(cols)):
    #     listbox.insert(i, cols[i])
    # listbox.place(x=0, y=0)
    # b1 = tk.Button(cselector,text="Add",command=f1)
    # b1.place(x=185, y=0)
    # cselector.mainloop()

    # cols = tuple(data.columns)
    # listbox = ttk.Treeview(root, columns=cols, show = "headings", height = 85)
    # vsb = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
    # ###CREATE RESPONSIVE X-HEIGHT###
    # vsb.place(x=2990, y= 0, height = 1680)
    # listbox.configure(yscrollcommand=vsb.set)
    # root.mainloop()

# hsb = ttk.Scrollbar(root, orient = "horizontal", command=listbox.xview)
# hsb.pack(fill = "x")
# hsb.place(x=20, y= 500, width=1000)
# listbox.configure(xscrollcommand=hsb.set)

L1 = tk.Label(cselector, text="selection")
L1.place(x= 250, y= 1000)

