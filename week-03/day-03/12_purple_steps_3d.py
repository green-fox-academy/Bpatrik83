from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.configure(background='white')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

x = 10
y = 10

def center_box_drawing(x, y):
    fill_color = "#%02x%02x%02x" % (176, 69, 242)
    rectangle = canvas.create_rectangle(x, x, y, y, fill=fill_color, width="1")

for i in range(10, 70, 10):
    x += i - 10
    y = x + i
    print(y)
    center_box_drawing(x, y)



root.mainloop()