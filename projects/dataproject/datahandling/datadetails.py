#button for generating complete info of data
#generate min, max, mean, mode, deviation or all columns
#should work with only selected columns or entire dataset

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
cselector.geometry("500x1000")

num = 0 #replace with screen
list2 = []
def f1():
    list2.append(listbox.get(tk.ANCHOR))
    print(list2)
    
def f2():
    global selected_data
    win1 = tk.Tk()
    selected_data=data[list2]
    #print(selected_data)
    cols= tuple(selected_data.columns)
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

def f3():

    clear()
    #l2.configure(text=str(data.describe()))
    #l2.place(x=10, y= 250)

    la.config(text=str(data.info()))
    
    #la.place(x=230,y=250)
    #print(data.std())
    #L4 = tk.Label(cselector, text='MAXIMUMS:  '+ str(data.mean()))
    #L4.place(x=10,y=500)

def f4():
    try:
        clear()
        selected_data=data[list2]
        l2.configure(text=str(selected_data.describe()))
        #l2.place(x=10, y= 250)
        
        la.configure(text= selected_data.info())
        #la.place(x=230,y=250)
        #print(selected_data.std())
    except:
        pass

def clear():
    l2.configure(text=' ')
    la.configure(text=' ')
list1 = []
listbox = tk.Listbox(cselector)
col = data.columns
for i in range(len(col)):
    listbox.insert(i, col[i])
listbox.place(x=0, y=0)

l2 = tk.Label(cselector,text='')
l2.place(x=10, y= 250)
la = tk.Label(cselector,text='')
la.place(x=5,y=250)

b1 = tk.Button(cselector,text="Add Column",command=f1)
b1.place(x=185, y=0)
b2 = tk.Button(cselector,text='Display Selected Columns',command=f2)
b2.place(x=185,y=40)
b3 = tk.Button(cselector, text = 'Display Complete Data Info', command = f3)
b3.place(x=185,y=80)
b4 = tk.Button(cselector, text = 'Display Selected Data Info', command = f4)
b4.place(x=185,y=120)
b5 = tk.Button(cselector, text='Clear Info',command=clear)
b5.place(x=185,y=160)
cselector.mainloop()

cols = tuple(data.columns)
listbox = ttk.Treeview(root, columns=cols, show = "headings", height = 85)
vsb = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
###CREATE RESPONSIVE X-HEIGHT###
vsb.place(x=2990, y= 0, height = 1680)
listbox.configure(yscrollcommand=vsb.set)
root.mainloop()


