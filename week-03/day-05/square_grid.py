from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

w = 600
x = 0
y = 0
border = 25

def black_square(x,y,w,border):
    if w < 40:
        pass
    else:
        canvas.create_rectangle(x+w/4,y+w/4,x+w*3/4,y+w*3/4, outline="black", width=border, fill="")
        black_square(x, y, w/2, border/2)
        black_square(x+w/2, y, w/2,border/2)
        black_square(x, y+w/2, w/2,border/2)
        black_square(x+w/2, y+w/2, w/2,border/2)

black_square(x,y,w,border)

root.mainloop()