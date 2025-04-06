import turtle as t

more=False
screen = t.Screen()
screen.setup(1000, 500)
screen.bgpic('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-gif-maker.gif')
image='/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-resize.gif'
screen.addshape(image)
t.shape(image)
def lc():
    def up():
        t.setheading(90)
        t.forward(20)
    def down():
        t.setheading(270)
        t.forward(20)
    def left():
        t.setheading(180)
        t.forward(20)
    def right():
        t.setheading(0)
        t.forward(20)
    t.listen()
    t.onkey(up, 'Up')
    t.onkey(down, 'Down')
    t.onkey(left, 'Left')
    t.onkey(right, 'Right')
    t.mainloop()
def pc():
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
def oc():
    x = int(input("Enter the X coordinate you want the helicopter to travel to: "))
    y = int(input("Enter the Y coordinate you want the helicopter to travel to: "))
    t.goto(x,y)
control=input("Type lc if you want to use the arrow keys, type pc if you want multiple tries, type oc if you want one chance to land the mars helicopter ")
if control == "lc":
    lc()
elif control == "pc":
    pc()
else:
    oc()

   