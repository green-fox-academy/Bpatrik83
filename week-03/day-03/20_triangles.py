from tkinter import *

root = Tk()

canvas = Canvas(root, width="400", height="600")
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

def draw_triangles(x, y):
    black_line = canvas.create_line(x, y, x + 7.5, y + 15, fill="black")
    black_line = canvas.create_line(x, y, x - 7.5, y + 15, fill="black")
    black_line = canvas.create_line(x - 7.5, y + 15, x + 7.5, y + 15, fill="black")

x = 200
y = 100

for i in range(25):
    y += 15
    x -= 7.5
    for j in range(i):
        x += 15
        draw_triangles(x, y)
    x -= i * 15
root.mainloop()