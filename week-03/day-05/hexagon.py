import random
import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    return random_color


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
    my_turtle.color(randomize())
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
hexagon(size = 300, n =5)
canvas.exitonclick()