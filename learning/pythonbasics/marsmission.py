import turtle as t
proceed = True
screen = t.Screen()
screen.setup(1000, 500)
screen.bgpic('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-gif-maker.gif')
image='/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-resize.gif'
screen.addshape(image)
t.shape(image)
while proceed == True:
    x = int(input("Enter the X coordinate you want the helicopter to travel to: "))
    y = int(input("Enter the Y coordinate you want the helicopter to travel to: "))
    t.goto(x,y)
    cont = input("Would you like to try again?: ")
    if cont == "yes":
        proceed = True
    else:
        proceed = False
    
t.mainloop()
   