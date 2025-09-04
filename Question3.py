'''
<<<<<<< HEAD
This is the code for the straight line using turtle graphics.

'''

import turtle
screen = turtle.Screen()
screen.title("Straight Line Example")
t = turtle.Turtle()
t.hideturtle()  
t.forward(200)
screen.mainloop()
=======
this function belongs to indentation pointing inward
'''

import turtle
t = turtle.Turtle()
t.hideturtle()   
t.speed(3)
def inward_line(length):
    segment = length / 3
    t.forward(segment)
    t.right(60)
    t.forward(segment)
    t.left(120)
    t.forward(segment)
    t.right(60)
    t.forward(segment)
inward_line(300)
turtle.done()
>>>>>>> 0bf6751 (indentation pointing inward)
