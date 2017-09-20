from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def draw_steps(size,number):
    start_width = 5
    start_height = 5
    for i in range(number):
        end_width = start_width + size
        end_height = start_height + size
        coords = [start_width, start_height, end_width, end_height]
        canvas.create_rectangle(coords, fill="purple")
        start_width = end_width
        start_height = end_height

draw_steps(10,23)

root.mainloop()