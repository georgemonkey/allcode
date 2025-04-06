

from glob import glob
from turtle import back, width
import matplotlib.pyplot as pl

from tkinter import *

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import END
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from tkinter import ttk
import customtkinter as ctk
import time
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
splashroot=ctk.CTk()
splashroot.geometry("800x500")
splashroot.title("Event Builder")
splash_label= ctk.CTkLabel(splashroot,text="Event Builder!")
splash_label.pack(pady=20)
lab=ctk.CTkLabel(splashroot,text="Loading...")
lab.pack(pady=50)
my_progress=ttk.Progressbar(splashroot, orient=HORIZONTAL,length=300,mode='determinate')
my_progress.pack(pady=20)
my_progress.start(25)
author=ctk.CTkLabel(splashroot,text="Created By Parth Amradkar")
author.pack(pady=100)
def loop():
    
    lab.destroy()
    lab2=ctk.CTkLabel(splashroot,text="Gathering Data")
    lab2.pack()
    







    
    




def main_window():  
    splashroot.destroy()
    

    root=ctk.CTk()
    root.geometry("800x500")
    root.title("Event Builder")
    l1=ctk.CTkLabel(root,text="Enter Data")
    l1.place(x=300, y=5)
    #form
    l2=ctk.CTkLabel(root,text="Full Name:")
    l2.place(x=10,y=50)
    t1=ctk.CTkEntry(root)
    t1.place(x=125,y=50)
    #name^^^
    l3=ctk.CTkLabel(root,text="Runner SID")
    l3.place(x=10,y=85)
    t2=ctk.CTkEntry(root)
    t2.place(x=125,y=85)
    #sid^^^
    l4=ctk.CTkLabel(root,text="Place")
    l4.place(x=10,y=120)
    t3=ctk.CTkEntry(root)
    t3.place(x=125,y=120)
    #place^^^
    l5=ctk.CTkLabel(root,text="Quick Add")
    l5.place(x=10,y=165)
    #r1=ctk.CTkRadioButton(root,text="Enable For Quick Add MODE",variable="r",value=1)
    #r1.place(x=125,y=165)
    #r2=ctk.CTkRadioButton(root,variable="r",value=2)
    #r2.place(x=155,y=165)
    
    def checks():
        if t1.get()=="":
            messagebox.showinfo("Information","Please Enter Name Into Entry Box")
        elif t2.get()=="":    
            messagebox.showinfo("Information","Please Enter Ruid Into Entry Box")
        elif t3.get()=="":   
            messagebox.showinfo("Information","Please Enter Place Into Entry Box")    
    def cleartable():
        for item in list1.get_children():
            list1.delete(item)   

    def add():
        
        ruid1=t2.get()
        rname1=t1.get()
        rplace1=t3.get()
        checks()

        
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        print("Connection Opened")
        cursor=mydb.cursor()
    

        sql=("insert into runners (ruid,rname,rplace) values (%s, %s,%s) ")
        val=(ruid1,rname1,rplace1)
        cursor.execute(sql,val)
        
        print("Values Registrated")
        
        mydb.commit()
        
        mydb.close()
        print("Connection Closed")
        cleartable()
        show()
    def searchname():

        
        try:   
            rname1=t1.get() 
            mydb=mysql.connector.connect(
            host="localhost",
            database="RB3",
            user="root",
            password="tyu@3434"
            
            )
            cursor=mydb.cursor()
            sql=("select rname,ruid,rplace from runners where rname=%s")   
            val=(rname1,)
            cursor.execute(sql,val)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            
            
            records=cursor.fetchall()
            t1.insert(0,records[0][0])
            t2.insert(0,records[0][1])
            t3.insert(0,records[0][2])
            
            
            print(records)
        except:
            messagebox.showinfo("Information","Name Is Not Located In Database")  
    def clearscreen():
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
    def searchplace():
        try:   
            rplace1=t3.get() 
            mydb=mysql.connector.connect(
            host="localhost",
            database="RB3",
            user="root",
            password="tyu@3434"
            
            )
            cursor=mydb.cursor()
            sql=("select rname,ruid,rplace from runners where rplace=%s")   
            val=(rplace1,)
            cursor.execute(sql,val)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            
            
            records=cursor.fetchall()
            t1.insert(0,records[0][0])
            t2.insert(0,records[0][1])
            t3.insert(0,records[0][2])
            
            
            print(records)
        except:
            messagebox.showinfo("Information","Name Is Not Located In Database")  
    def update():
        rname1=t1.get()
        ruid1=t2.get()
        rplace1=t3.get()
        
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        print("Connection Opened")
        cursor=mydb.cursor()
    

        sql=("update runners set rname=%s,rplace=%s where ruid=%s ")
        val=(rname1,rplace1,ruid1)
        cursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Information","Records Updated Succesfully")
        cleartable()
        show()  
    def searchruid():
        try:   
            ruid1=t2.get() 
            mydb=mysql.connector.connect(
            host="localhost",
            database="RB3",
            user="root",
            password="tyu@3434"
            
            )
            cursor=mydb.cursor()
            sql=("select rname,ruid,rplace from runners where ruid=%s")   
            val=(ruid1,)
            cursor.execute(sql,val)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            
            
            records=cursor.fetchall()
            t1.insert(0,records[0][0])
            t2.insert(0,records[0][1])
            t3.insert(0,records[0][2])
            
            
            print(records)
        except:
            messagebox.showinfo("Information","RUID Is Not Located In Database")
    def delete():
        ruid1=t2.get()
        rname1=t1.get()
        rplace1=t3.get()
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        print("Connection Opened")
        cursor=mydb.cursor()
    

        sql=("DELETE FROM runners WHERE ruid=%s")
        val=(ruid1,)
        cursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Information","Records Deleted Succesfully")
        cleartable()
        show()
        clearscreen()
    def show():
        try:   
            rname=t1.get() 
            mydb=mysql.connector.connect(
            host="localhost",
            database="RB3",
            user="root",
            password="tyu@3434"
            
            )
            cursor=mydb.cursor()
            sql=("select ruid,rname,rplace from runners")   
            
            cursor.execute(sql)
            records=cursor.fetchall()
            print(records)
            for i,(ruid,rname,rplace) in enumerate(records,start=1):
                list1.insert("","end",values=(ruid,rname,rplace))
                mydb.close()

        except:
            messagebox.showinfo("Information","Name Is Not Located In Database")
        
        

    
    def Value1(event):
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        
        rowsid=list1.selection()[0]
        select=list1.set(rowsid)
        t2.insert(0,select["ruid"])
        t1.insert(0,select["rname"])
        t3.insert(0,select["rplace"])
        cleartable()
        show()
    
        
        
        
            

    #button to add
    b1=ctk.CTkButton(root,text="Add", command=add)
    b1.place(x=650,y=50)
    b2=ctk.CTkButton(root,text="Search By Name",command=searchname)
    b2.place(x=650,y=150)
    b3=ctk.CTkButton(root,text="Search By Place",command=searchplace)
    b3.place(x=650,y=100)
    b4=ctk.CTkButton(root,text="Clear Data Entry",command=clearscreen)
    b4.place(x=650,y=200)
    b5=ctk.CTkButton(root,text="Update Via RUID", command=update)
    b5.place(x=650,y=250)
    b6=ctk.CTkButton(root,text="Search Via RUID",command=searchruid)
    b6.place(x=650,y=300)
    b7=ctk.CTkButton(root,text="Delete Via RUID",command=delete)
    b7.place(x=650,y=350)
    style=ttk.Style()
    style.configure("Treeview",
        background="lightblue",
        foreground="darkblue",
        rowheight=25,
        fieldbackground="blue"

    )
    cols=("ruid","rname","rplace")
    list1=ttk.Treeview(root,columns=cols,show="headings")
    for coll in cols:
        list1.heading(coll,text=coll)
        list1.grid(row=1,column=0,columnspan=2)
        list1.place(x=10,y=250)

    show()
    list1.bind('<Double-Button-1>',Value1)


    #MYSQL

    
splashroot.after(5000, main_window)
lab.after(2000,loop)

mainloop()