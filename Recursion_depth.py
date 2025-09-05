import turtle

def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        
        segment = length / 3
        draw_edge(segment, depth - 1)
        turtle.right(60)
        draw_edge(segment, depth - 1)
        turtle.left(120)
        draw_edge(segment, depth - 1)
        turtle.right(60)
        draw_edge(segment, depth - 1)

def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

# Main program
def main():
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length/2, length/2)  
    turtle.pendown()
    
    draw_polygon(sides, length, depth)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()