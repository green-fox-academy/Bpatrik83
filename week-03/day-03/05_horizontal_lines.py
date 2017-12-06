from random import randrange
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def random_coordinates():
    x = randrange(0, 250)
    y = randrange(0, 250)
    return x, y

def line_drawing(x, y):
    red_line = canvas.create_line(x + 50, y, x, y, fill="red")

for i in range(3):
    random_coordinates()
    line_drawing(*random_coordinates())

root.mainloop()