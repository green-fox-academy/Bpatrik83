import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    return random_color

def rainbow_square_drawing(random_color, square_size):
    rectangle = canvas.create_rectangle(150 + square_size, 150 + square_size, 150 - square_size, 150 - square_size, fill=random_color, width="0")

for square_size in range(300, 0, - 10):
    randomize()
    rainbow_square_drawing(randomize(), square_size)


root.mainloop()