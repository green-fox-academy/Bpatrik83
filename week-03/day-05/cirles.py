import random
import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    return random_color

def start(size):
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.setposition(0, -300)
    my_turtle.pendown()
    draw_circle(size)
    my_turtle.circle(size, 180)

def draw_circle(size):
    my_turtle.color(randomize())
    my_turtle.circle(size)

def circle(size, n):
    if n == 0:
        return
    else:
        draw_circle(size / 2)
        circle(size / 2, n - 1)
        my_turtle.circle(size, 120)
        draw_circle(size / 2)
        circle(size / 2, n - 1)
        my_turtle.circle(size, 120)
        draw_circle(size / 2)
        circle(size / 2, n - 1)
        my_turtle.circle(size, 120)

start(size = 300)
circle(size = 300, n = 5)
canvas.exitonclick()