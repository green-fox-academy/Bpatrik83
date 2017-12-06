import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# draw four different size and color rectangles.

def randomize():
    rgb_random = lambda: random.randint(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random(), rgb_random(), rgb_random()))
    x = random.randrange(0, 250)
    y = random.randrange(0, 250)
    z = random.randrange(0, 250)
    q = random.randrange(0, 250)
    return x, y, q, z, random_color

def square_drawing(x, y, z, q, random_color):
    rectangle = canvas.create_rectangle(z, q, x, y, fill=random_color, width="0")

for i in range(4):
    randomize()
    square_drawing(*randomize())

root.mainloop()