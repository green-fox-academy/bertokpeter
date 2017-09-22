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

def black_square(x,y,w):
    if w < 2.5:
        pass
    else:
        margin = w/240
        canvas.create_rectangle(x+w/3,y+w/3,x+w*2/3,y+w*2/3, outline="", fill="")
        canvas.create_rectangle(x+w/3+margin,y+w/3+margin,x+w*2/3-margin,y+w*2/3-margin, fill="black")
        black_square(x, y, w/3)
        black_square(x+w/3, y, w/3)
        black_square(x+w*2/3, y, w/3)
        black_square(x, y+w/3, w/3)
        black_square(x, y+w*2/3, w/3)
        black_square(x+w/3, y+w*2/3, w/3)
        black_square(x+w*2/3, y+w*2/3, w/3)
        black_square(x+w*2/3, y+w/3, w/3)

black_square(x,y,w)

root.mainloop()