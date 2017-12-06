import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300", bg="black")
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def randomize():
    rgb_random = random.randrange(0, 255)
    random_color = ("#%02X%02X%02X" % (rgb_random, rgb_random, rgb_random))
    x = random.randrange(0, 295)
    y = random.randrange(0, 295)
    return x, y, random_color

def square_drawing(x, y, random_color):
    rectangle = canvas.create_rectangle(x, y, x + 5, y + 5, fill=random_color, width="0")

for i in range(200):
    randomize()
    square_drawing(*randomize())

root.mainloop()