
import turtle as t

more=False
screen = t.Screen()
screen.setup(1000, 500)
screen.bgpic('/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-gif-maker.gif')
image='/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/MarsLanding/ezgif.com-resize.gif'
screen.addshape(image)
t.shape(image)

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
   