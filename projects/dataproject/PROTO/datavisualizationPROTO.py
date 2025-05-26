import tkinter as tk
from tkinter import filedialog
import webbrowser as wb
import os 
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

#SETUP
try:
    root = tk.Tk()
    root.title("Data Handling")
    root.geometry("500x500")
    menubar=tk.Menu(root)

    #FUNCTIONS

    def fileopen():
        try:
            global filename
            global data1
            filename = filedialog.askopenfilename()
            print(filename)
            data1 = pd.read_csv(filename)
            print("donereading")
        except:
            pass
        #print(data1)
        #subprocess.Popen([filename  ,"sudo /usr/bin/open Preview"],shell=True)

    def import_window():
        try:
            win1 = tk.Tk()
            win1.title("Import Dialog")
            win1.geometry("300x200")
            L1 = tk.Label(win1, text="Import CSV File:   ")
            L1.place(x=0, y=0)
            B1 = tk.Button(win1, text="Select File", command=fileopen)
            B1.place(x=100,y=0)

            L2 = tk.Label(win1, text="Visualize Data: ")
            L2.place(x=0, y=50)
            B2 = tk.Button(win1, text="Line Graph", command=linegraph)
            B2.place(x=100,y=50)
            B3 = tk.Button(win1, text="Bar Graph", command=bargraph)
            B3.place(x=200,y=50)
            win1.mainloop()
        except:
            pass

    def linegraph():
        try:
            data1.plot(kind="line")
            plt.show()
        except:
            pass

    def bargraph():
        try:
            data1.plot(kind="bar")
            plt.show()
        except:
            pass

    def visual():
        try:
            win2 = tk.Tk()
            win2.title("Visualization")
            win2.geometry("200x50")
            
            win2.mainloop()
        except:
            pass
        #data1.plot


    
    #FILE BAR
    filemenu=tk.Menu(menubar,background="#A5D0FD", activebackground="#F59C9C")
    filemenu.add_command(label="Import", command=import_window)
    filemenu.add_command(label="Visualization", command=visual)
    menubar.add_cascade(label="Data",menu=filemenu)






    root.config(menu=menubar, background="#FFF")
    root.mainloop()

except:
    pass