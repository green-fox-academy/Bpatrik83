from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300", bg="white")
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def center_box_drawing():
    fill_color = "#%02x%02x%02x" % (176, 69, 242)
    rectangle = canvas.create_rectangle(x, x, x - 10, x - 10 , fill=fill_color, width="1")

for x in range(20, 210, 10):
    center_box_drawing()

root.mainloop()