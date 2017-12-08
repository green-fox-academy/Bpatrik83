import random
import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()
my_turtle.speed(0)
my_turtle.penup()
my_turtle.setposition(-300, -300)
my_turtle.pendown()

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    return random_color

def triangles(size, n):
    if n == 0:
        my_turtle.color(randomize())
        for i in range(0, 3):
            my_turtle.forward(size)
            my_turtle.left(120)
    else:
        triangles(size / 2, n - 1)
        my_turtle.forward(size / 2)
        triangles(size / 2, n - 1)
        my_turtle.backward(size / 2)
        my_turtle.left(60)
        my_turtle.forward(size / 2)
        my_turtle.right(60)
        triangles(size / 2, n - 1)
        my_turtle.left(60)
        my_turtle.backward(size / 2)
        my_turtle.right(60)


size = 400
n = 4

triangles(size, n)
canvas.exitonclick()