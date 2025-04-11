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
cselector.geometry("600x1000")

num = 0 #replace with screen
selecteddata = []
def append_column():
    global textdata
    textdata = '0'
    selecteddata.append(listbox.get(tk.ANCHOR))
    display_selected_list()
def display_selected_list():
    for i in range(len(selecteddata)):
        textdata = textdata + selecteddata[i]
        selected_display.configure(text = textdata )
    
def data_display():
    global selected_data
    win1 = tk.Tk()
    selected_data=data[selecteddata]
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
def complete_data_display():
    clear()
    completedatainfo = 'INDEX: '+str(data.index)+'\n'+'COUNT: '+str(data.count())+ '\n'+'DATA TYPES: '+str(data.dtypes)
    leftinfo.config(text=completedatainfo)
def display_selected_data():
    clear()
    selected_data=data[selecteddata]
    selected_datainfo = 'INDEX: '+str(selected_data.index)+'\n'+'COUNT: '+str(selected_data.count())+ '\n'+'DATA TYPES: '+str(selected_data.dtypes)
    leftinfo.config(text=selected_datainfo)
def clear():
    rightinfo.configure(text=' ')
    leftinfo.configure(text=' ')
list1 = []
listbox = tk.Listbox(cselector)
col = data.columns
for i in range(len(col)):
    listbox.insert(i, col[i])
listbox.place(x=0, y=0)

rightinfo = tk.Label(cselector,text='')
rightinfo.place(x=10, y= 250)
leftinfo = tk.Label(cselector,text='')
leftinfo.place(x=5,y=250)
selected_display = tk.Label(cselector,text='')
selected_display.place(x=400,y=15)

b1 = tk.Button(cselector,text="Add Column",command=append_column)
b1.place(x=185, y=0)
b2 = tk.Button(cselector,text='Display Selected Columns',command=data_display)
b2.place(x=185,y=40)
b3 = tk.Button(cselector, text = 'Display Complete Data Info', command = complete_data_display)
b3.place(x=185,y=80)
b4 = tk.Button(cselector, text = 'Display Selected Data Info', command = display_selected_data)
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


