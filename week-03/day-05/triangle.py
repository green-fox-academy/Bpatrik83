import turtle

my_turtle = turtle.Turtle(shape = "turtle")
canvas = turtle.Screen()
my_turtle.speed(0)
my_turtle.penup()
my_turtle.setposition(0, 0)
my_turtle.pendown()
my_turtle._tracer(0,0)

def triangles(size, n):
    if n == 0:
        for i in range(0, 3):
            my_turtle.forward(size)
            my_turtle.left(140)
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


size = 500
n = 3

triangles(size, n)
canvas.update()
canvas.exitonclick()