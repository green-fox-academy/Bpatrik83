from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300", bg="white")
canvas.pack()

# fill the canvas with a checkerboard pattern.

def checker_board(x, y):
    rectangle = canvas.create_rectangle(x, y, x + 10, y + 10, fill="black", width="0")

for x in range(0, 300, 10):
    if (x / 10) % 2 == 0:
        z = 10
    else:
        z = 0
    for y in range(z, 300, 20):
        checker_board(x, y)


root.mainloop()