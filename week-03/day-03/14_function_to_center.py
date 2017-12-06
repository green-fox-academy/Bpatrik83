from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


def line_drawing(x, y):
    green_line = canvas.create_line(150, 150, x, y, fill="green")

for x in range(0, 301, 20):
    line_drawing(x, y=0)

for y in range(0, 301, 20):
    line_drawing(x, y)

for x in range(300, -1, -20):
    line_drawing(x, y = 300)

for y in range(300, -1, -20):
    line_drawing(x, y)

root.mainloop()