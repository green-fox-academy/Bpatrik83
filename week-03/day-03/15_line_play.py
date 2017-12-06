from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_drawing(i):
    fill_color_purple = "#%02x%02x%02x" % (176, 69, 242)
    fill_color_green = "#%02x%02x%02x" % (93, 217, 100)
    purple_line = canvas.create_line(40 + i, 2, 298, i, fill=fill_color_purple)
    green_line = canvas.create_line(2, 40 + i, i, 298, fill=fill_color_green)

for i in range(10, 270, 20):
        line_drawing(i)


root.mainloop()