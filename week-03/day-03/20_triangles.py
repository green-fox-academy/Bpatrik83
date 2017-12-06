from tkinter import *

root = Tk()

canvas = Canvas(root, width="1000", height="1300")
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

def draw_triangles(x):
    black_line = canvas.create_line(500 + x, 80 + x, 280 + x * 2, 300, fill="black")
    black_line = canvas.create_line(490 - x - 10, 100 + x, 510 + x + 10, 100 + x, fill="black")
    black_line = canvas.create_line(500 - x, 80 + x, 720 - x * 2, 300, fill="black")

for x in range(0, 220, 20):
    draw_triangles(x)

root.mainloop()