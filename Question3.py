import turtle
import math

# Recursive function to draw one fractal edge
def draw_fractal_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_fractal_edge(t, length, depth - 1)  # 1st segment
        t.left(60)
        draw_fractal_edge(t, length, depth - 1)  # upward triangle side
        t.right(120)
        draw_fractal_edge(t, length, depth - 1)  # downward triangle side
        t.left(60)
        draw_fractal_edge(t, length, depth - 1)  # last segment


# Draw the fractal polygon
def draw_fractal_polygon(sides, length, depth):
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Recursive Fractal Polygon Pattern")

    t = turtle.Turtle()
    t.speed(0)  # fastest

    angle = 360 / sides

    for _ in range(sides):
        draw_fractal_edge(t, length, depth)
        t.right(angle)

    wn.mainloop()


# ---------------------------
# MAIN PROGRAM (User Input)
# ---------------------------
if __name__ == "__main__":
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length (pixels): "))
    depth = int(input("Enter the recursion depth: "))

    draw_fractal_polygon(sides, length, depth)



