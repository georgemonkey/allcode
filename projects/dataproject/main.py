#button for generating complete info of data
#generate min, max, mean, mode, deviation or all columns
#should work with only selected columns or entire dataset

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import IntVar
import matplotlib.pyplot as plt
from tkinter import messagebox
from pandas.plotting import scatter_matrix
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



fileopen()

root = tk.Tk()
root.title("Selector")
root.geometry("650x1000")

num = 0 #replace with screen
selecteddata = []
def append_column():

    global textdata
    textdata = '0'
    selecteddata.append(listbox.get(tk.ANCHOR))
    display_selected_list()
def remove_column():
    selecteddata.remove(listbox.get(tk.ANCHOR))
    display_selected_list()
def display_selected_list():
    textdata = ' '
    for i in (selecteddata):
        textdata = textdata + '\n' + i 
        selected_display.configure(text = textdata )
def data_selected_display():
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
def data_complete_display():
    win2 = tk.Tk()
    win2.title = 'temp'
    cols= tuple(data.columns)
    listbox = ttk.Treeview(win2, columns=cols,show='headings',height=85)
    vsb = ttk.Scrollbar(win2, orient="vertical", command=listbox.yview)
    vsb.place(x=2990, y= 0, height = 1680)
    listbox.configure(yscrollcommand=vsb.set)
    listbox.place(x=0,y=0)

    for i in cols:
        listbox.heading(i,text=i)
        listbox.column(i,anchor='center')
        listbox.place(x=10,y=10)
    for row,cols in enumerate(data.values, start= 0):
        listbox.insert("","end",values=cols)
    win2.mainloop()
def data_complete_info_display():
    clear_info_panel()
    completedatainfo = 'INDEX: '+str(data.index)+'\n'+'COUNT: '+str(data.count())+ '\n'+'DATA TYPES: '+str(data.dtypes)
    leftinfo.config(text=completedatainfo)
def data_selected_info_display():
    global selected_data
    clear_info_panel()
    selected_data=data[selecteddata]
    selected_datainfo = 'INDEX: '+str(selected_data.index)+'\n'+'COUNT: '+str(selected_data.count())+ '\n'+'DATA TYPES: '+str(selected_data.dtypes)
    leftinfo.config(text=selected_datainfo)
def clear_info_panel():
    rightinfo.configure(text=' ')
    leftinfo.configure(text=' ')
def clear_selected():
    selecteddata.clear()
    selected_display.configure(text='')
def getcords(event):
    x = event.x
    y = event.y
    print(x,y)
def opengraphpanel():
    if (len(selecteddata) == 0):
        messagebox.showerror("Error!", "Select columns before entering graphing panel")
    else:
        graphpanel = tk.Tk()
        graphpanel.title('Graphing Panel')
        graphpanel.geometry('450x400')
        warning1 = tk.Label(graphpanel,text='GRAPHS FROM SELECTED COLUMNS',font = ('Helvetica',18 ))
        warning1.place(x=30, y = 15)
        selected_dataLISTFORM=data[selecteddata]
        print('selected list converted')
        selected_x = tk.StringVar()
        x_selector = ttk.Combobox(graphpanel,textvariable=selected_x,values=data,state='readonly')
        x_selector.place(x=4,y=300)
        x_selector.set('Select X-Value')

        selected_y = tk.StringVar()
        y_selector = ttk.Combobox(graphpanel,textvariable=selected_y,values=data,state='readonly')
        y_selector.place(x=220,y=300)
        y_selector.set('Select Y-Value')

        def linegraph():
            selected_dataLISTFORM.plot(kind='line')
            plt.show()
        def bargraph():
            selected_dataLISTFORM.plot(kind="bar")
            plt.show()
        def scatkde():
            scatter_matrix(selected_dataLISTFORM, diagonal="kde")
            plt.show()
        def histkde():
            scatter_matrix(selected_dataLISTFORM, diagonal="hist")
            plt.show()
    
        linegraph_button = tk.Button(graphpanel,text='Line Graph', command=linegraph,font = ('Helvetica',20 ),width=14)
        linegraph_button.place(x=4,y=50)
        bargraph_button = tk.Button(graphpanel,text='Bar Graph', command=bargraph,font = ('Helvetica',20 ),width=14)
        bargraph_button.place(x=4,y=100)
        scatkde_button = tk.Button(graphpanel,text='Scatter KDE', command=scatkde,font = ('Helvetica',20 ),width=14)
        scatkde_button.place(x=4,y=150)
        histkde_button = tk.Button(graphpanel,text='Histogram KDE', command=histkde,font = ('Helvetica',20 ),width=14)
        histkde_button.place(x=4,y=200)
        pie_button = tk.Button(graphpanel,text='Pie Graph', command=histkde,font = ('Helvetica',20 ),width=14)
        pie_button.place(x=4,y=250)
        graphpanel.mainloop()
gc = tk.Button(text='get cords')
root.bind("<Button-1>", getcords)
gc.place(x=215,y=700)
list1 = []
listbox = tk.Listbox(root,width=60,height=15)
col = data.columns
for i in range(len(col)):
    listbox.insert(i, col[i])
listbox.place(x=40, y=0)

rightinfo = tk.Label(root,text='')
rightinfo.place(x=10, y= 250)
leftinfo = tk.Label(root,text='')
leftinfo.place(x=300,y=570)
selected_display = tk.Label(root,text='',font = ('Helvetica',20 ))
selected_display.place(x=20,y=570)
selected_display_label = tk.Label(root,text='Selected Items: ',font = ('Helvetica',20 ),background='#1E1E1E')
selected_display_label.place(x=20,y=570)

###LEFT ROW
add_button = tk.Button(root,text="Add Column",command=append_column,font = ('Helvetica',20 ),width=20)
add_button.place(x=20, y=300)

remove_button = tk.Button(root,text="Remove Column",command=remove_column,font = ('Helvetica',20 ),width=20)
remove_button.place(x=20, y=350)

display_selected_button = tk.Button(root,text='Display Selected Columns',command=data_selected_display,font = ('Helvetica',20 ),width=20)
display_selected_button.place(x=20,y=400)

display_selected_button = tk.Button(root,text='Display Complete Columns',command=data_complete_display,font = ('Helvetica',20 ),width=20)
display_selected_button.place(x=20,y=450)

open_graph_panel_button = tk.Button(root, text='Open Graphing Panel', command = opengraphpanel, font = ('Helvetica',20 ),width=20)
open_graph_panel_button.place(x=20, y=500)

###RIGHT ROW
display_complete_info_button = tk.Button(root, text = 'Display Complete Data Info', command = data_complete_info_display,font = ('Helvetica',20 ),width=20)
display_complete_info_button.place(x=320,y=300)

display_selected_info_button = tk.Button(root, text = 'Display Selected Data Info', command = data_selected_info_display,font = ('Helvetica',20 ),width=20)
display_selected_info_button.place(x=320,y=350)

clear_info_panel_button = tk.Button(root, text='Clear Info',command=clear_info_panel,font = ('Helvetica',20 ),width=20)
clear_info_panel_button.place(x=320,y=400)

clear_selected_button = tk.Button(root,text = 'Clear Selected Items', command = clear_selected,font = ('Helvetica',20 ),width=20)
clear_selected_button.place(x=320, y=450)


root.mainloop()
