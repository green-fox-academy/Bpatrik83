from tkinter import *

root = Tk()

canvas = Canvas(root, width="298", height="298")
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_drawing(i):
    fill_color_purple = "#%02x%02x%02x" % (176, 69, 242)
    fill_color_green = "#%02x%02x%02x" % (93, 217, 100)
    purple_line = canvas.create_line(2 + i, 2, 2, 150 - i, fill=fill_color_purple)
    green_line = canvas.create_line(150, 20 + i, 150 - i, 150, fill=fill_color_green)

    yellow_line = canvas.create_line(150, 20 + i, 150 + i, 150, fill="yellow")
    blue_line = canvas.create_line(20 + i, 150, 150, 150 + i, fill="blue")

    blue_line = canvas.create_line(150 + i, 150, 150, 299 - i, fill="orange")
    purple_line = canvas.create_line(150 + i, 2, 298, i, fill="lightblue")

    purple_line = canvas.create_line(160 + i, 298, 298, 298 - i, fill="red")
    green_line = canvas.create_line(2, 190 + i, i, 298, fill="green")


for i in range(10, 140, 10):
        line_drawing(i)

root.mainloop()