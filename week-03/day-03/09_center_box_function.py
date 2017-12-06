import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def randomize():
    random_size = random.randrange(0, 150)
    return random_size

def center_box_drawing(random_size):
    rectangle = canvas.create_rectangle(150 + random_size, 150 + random_size, 150 - random_size, 150 - random_size, fill="", width="1")

for i in range(3):
    randomize()
    center_box_drawing(randomize())

root.mainloop()