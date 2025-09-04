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
