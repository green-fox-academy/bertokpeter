from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def draw_steps_3d(size,number):
    start_width = 5
    start_height = 5
    for i in range(1, number+1):
        end_width = start_width + size*i
        end_height = start_height + size*i
        if end_width > 300 or end_height > 300:
            break 
        coords = [start_width, start_height, end_width, end_height]
        canvas.create_rectangle(coords, fill="purple")
        start_width = end_width
        start_height = end_height

draw_steps_3d(7,10)

root.mainloop()