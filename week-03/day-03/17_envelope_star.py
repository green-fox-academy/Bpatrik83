from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

def line_drawing(i):
    fill_color_green = "#%02x%02x%02x" % (93, 217, 100)
    green_line = canvas.create_line(150, 2 + i, 150 + i, 151, fill=fill_color_green)
    green_line = canvas.create_line(150, 2 + i, 150 - i, 151, fill=fill_color_green)
    green_line = canvas.create_line(150, 298 - i, 150 - i, 150, fill=fill_color_green)
    green_line = canvas.create_line(150, 298 - i, 150 + i, 150, fill=fill_color_green)


for i in range(0, 150, 10):
        line_drawing(i)

root.mainloop()