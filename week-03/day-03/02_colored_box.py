from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# draw a box that has different colored lines on each edge.
red_line = canvas.create_line(100, 100, 200, 100, width ="3", fill="blue")
green_line = canvas.create_line(100, 100, 100, 200, width ="3", fill="green")
yellow_line = canvas.create_line(100, 200, 200, 200, width ="3", fill="red")
purple_line = canvas.create_line(200, 100, 200, 200, width ="3", fill="purple")

root.mainloop()