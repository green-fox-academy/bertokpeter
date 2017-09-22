from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

w = canvas_width/2
x = canvas_width/2
y = canvas_height/2

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

def diamond(x,y,w):
    if w < 15:
        pass
    else:
        initx = x-w/2
        h = triangle_height(w)
        canvas.create_polygon(initx, y-h, initx+w, y-h, initx+1.5*w, y,
        initx+w, y+h, initx, y+h, initx-w/2, y, outline="black", width=1, fill="")
        diamond(x-w/4, y-h/2, w/2)
        diamond(x+w/2, y, w/2)
        diamond(x-w/4, y+h/2, w/2)

diamond(x,y,w)

root.mainloop()