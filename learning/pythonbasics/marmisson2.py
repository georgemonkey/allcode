import turtle as t

more=False
screen = t.Screen()
screen.setup(1000, 500)
screen.bgpic('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-gif-maker.gif')
image='/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-resize.gif'
screen.addshape(image)
t.shape(image)

more=int(input("How many entries would you like: "))
l1=[]
l2=[]
while more>=1:
    x = int(input("Enter the X coordinate you want the helicopter to travel to: "))
    y = int(input("Enter the Y coordinate you want the helicopter to travel to: "))
    l1.append(x)
    l2.append(y)

    
    more -= 1
for i in range(len(l1)):

    t.goto(l1[i],l2[i])    
t.mainloop()
   