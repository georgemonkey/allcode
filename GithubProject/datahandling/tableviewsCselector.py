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

L1 = tk.Label(cselector, text="selection")
L1.place(x= 250, y= 1000)
list1 = []
def f1():
    if name.get() == 1:
        list1.append(abc1)
    else:
        pass
#checkbtn1 = IntVar()
for abc2 in data.columns:
    global name
    
    name = IntVar()
    num = num + 20
    abc1 =tk.Checkbutton(cselector, text=abc2, variable = name, onvalue=1, offvalue=0, command=f1)
    abc1.place(x=0,y=num)
    print(list1)
print(name.get())
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