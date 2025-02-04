import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
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
root.geometry("1200x500")
fileopen()

cols = tuple(data.columns)
listbox = ttk.Treeview(root, columns=cols, show = "headings")
for i in cols:
    listbox.heading(i,text=i)
    listbox.column(i, anchor="center")
    listbox.place(x=10,y=10)
for row,cols in enumerate(data.values, start=0):
    listbox.insert("","end",values = cols)

root.mainloop()