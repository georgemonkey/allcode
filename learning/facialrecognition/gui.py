
import tkinter as tk
import test
root=tk.Tk()
button=tk.Button(root,text="Click to record",command=test.cmd)
button.pack()

root.mainloop()