from tkinter import * 
from tkinter import ttk
import time
root= Tk()
root.geometry("600x400")
my_progress=ttk.Progressbar(root, orient=HORIZONTAL,length=300,mode='determinate')
my_progress.pack(pady=20)
root.mainloop()