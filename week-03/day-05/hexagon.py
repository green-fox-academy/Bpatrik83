import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()

def start():
    my_turtle.speed(11)
    my_turtle.penup()
    my_turtle.setposition(-200, -250)
    my_turtle.pendown()

def find_pos(size):
    my_turtle.forward(size / 2)
    my_turtle.left(60)
    my_turtle.forward(size)

def draw_hexa(size):
    for i in range(0, 6):
        my_turtle.forward(size)
        my_turtle.left(60)

def hexagon(size, n):
    if n == 0:
        return
    else:
        draw_hexa(size / 2)
        hexagon(size / 3, n - 1)
        my_turtle.forward(size)
        for i in range(5):
            draw_hexa(size / 2)
            hexagon(size / 3, n - 1)
            find_pos(size)
        my_turtle.forward(size / 2)
        my_turtle.left(60)

start()
hexagon(size = 200, n = 2)
canvas.exitonclick()