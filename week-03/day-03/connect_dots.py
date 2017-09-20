from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
def connect(list_of_dots):
    for i in range(len(list_of_dots)):
        if i == len(list_of_dots)-1:
            canvas.create_line(list_of_dots[i], list_of_dots[0], fill="green")
        else:
            canvas.create_line(list_of_dots[i], list_of_dots[i+1], fill="green")

box_list = [[10, 10], [290,  10], [290, 290], [10, 290]]
fox_list = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],[120, 100], [85, 130], [50, 100]]
connect(box_list)
connect(fox_list)

root.mainloop()