import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    x = random.randrange(0, 250)
    y = random.randrange(0, 250)
    return x, y, random_color

def square_drawing(x, y, random_color):
    rectangle = canvas.create_rectangle(x, y, x + 50, y + 50, fill=random_color, width="0")

for i in range(3):
    randomize()
    square_drawing(*randomize())

root.mainloop()