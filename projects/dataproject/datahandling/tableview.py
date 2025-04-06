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
#root.attributes("-fullscreen", True)
#w,h = root.winfo_screenmmwidth(), root.winfo_screenmmheight()
#root.geometry("%dx%d+0+0" % (w, h))

fileopen()

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
for i in cols:
    listbox.heading(i,text=i)
    listbox.column(i, anchor="center", stretch=False)
    #listbox.place(x=10,y=10)
    listbox.pack(side="top")
for row,cols in enumerate(data.values, start=0):
    listbox.insert("","end",values = cols)
num = 0 #replace with screen

L1 = tk.Label(root, text="selection")
L1.place(x= 250, y= 1000)
def f1():
    if name.get() == 1:
        L1.config(text="Harry Is There")
    else:
        L1.config(text= "Harry Is Not There")
#checkbtn1 = IntVar()
for abc1 in data.columns:
    global name
    name = "checkbtn" + abc1
    name = IntVar()
    num = num + 20
    abc1 =tk.Checkbutton(root, text=abc1, variable = name, onvalue=1, offvalue=0, command=f1)
    abc1.place(x=0,y=num)
    
root.mainloop()