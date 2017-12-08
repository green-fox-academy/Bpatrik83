import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()
my_turtle.speed(0)
my_turtle.penup()
my_turtle.setposition(-300, -300)
my_turtle.pendown()

def triangles(size, n):
    if n == 0:
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