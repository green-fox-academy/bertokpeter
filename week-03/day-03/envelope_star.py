from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_width)
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]
center = canvas_width//2

def half_envelope(distance):
    for j in range(center//distance+1):
        for i in (1, -1):
            canvas.create_line(distance*j,center,center,center-distance*j*i, fill="green")
            canvas.create_line(center+distance*j,center,center,center-(center-distance*j)*i, fill="green")

half_envelope(10)

root.mainloop()