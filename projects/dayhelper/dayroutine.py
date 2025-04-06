import tkinter as tk
from tkinter import filedialog
import webbrowser as wb
import os 
import subprocess

import customtkinter as ctk
def fileopen():
    filename = filedialog.askopenfilename()
    print(filename)
    subprocess.Popen([filename  ,"sudo /usr/bin/open Preview"],shell=True)
    
def mainmail():  
    wb.open('https://mail.google.com/mail/u/1/#inbox')

def piano():
    wb.open('https://us02web.zoom.us/j/2320221486?pwd=SWJYMjl0aVZRNW1rMUoxcElwaW1hUT09#success')


    
root = tk.Tk()
root.title("Manager")
root.geometry("500x500")
menubar=tk.Menu(root)
#FILE BAR
filemenu=tk.Menu(menubar,background="#A5D0FD", activebackground="#F59C9C")
filemenu.add_command(label="Open File", command=fileopen)
menubar.add_cascade(label="File",menu=filemenu)

#CLASSES BAR
classmenu=tk.Menu(menubar)
classmenu.add_command(label="Piano Class",command=piano)
menubar.add_cascade(label="Classes",menu=classmenu)

#SHORTCUTS BAR
shortcutmenu=tk.Menu(menubar)
shortcutmenu.add_command(label="Main Mail",command=mainmail)
menubar.add_cascade(label="Shortcuts",menu=shortcutmenu)

#ON-SCREEN

timelabel=ctk.CTkLabel(root,text="Made by: Parth Amradkar",text_color="#323b3b")
timelabel.place(x=200,y=475)


#CONFIG
root.config(menu=menubar, background="#D4F3FC")
root.mainloop()
 