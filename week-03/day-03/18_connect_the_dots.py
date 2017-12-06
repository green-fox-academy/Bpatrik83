from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

rectangle_list = [[10, 10], [290,  10], [290, 290], [10, 290]]
dots_list = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]




def connect_dots(rectangle_list):
    list_length = len(rectangle_list) - 1
    for i in range(list_length):
        green_line = canvas.create_line(rectangle_list[i][0], rectangle_list[i][1], rectangle_list[i + 1][0], rectangle_list[i + 1][1], fill="green")
    green_line = canvas.create_line(rectangle_list[0][0], rectangle_list[0][1], rectangle_list[list_length][0],
                                    rectangle_list[list_length][1], fill="green")

connect_dots(rectangle_list)
connect_dots(dots_list)

root.mainloop()