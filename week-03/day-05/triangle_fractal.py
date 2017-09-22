from tkinter import *
import math
root = Tk()

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

w = 600
x = 5
y = 5

canvas_width = 610
canvas_height = triangle_height(w) + 5
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

def triangle(x,y,w):
    if w < 2.5:
        pass
    else:
        h = triangle_height(w)
        canvas.create_polygon(x,y,x+w,y,x+w/2,y+h, outline="black", width=1, fill="")
        triangle(x, y, w/2)
        triangle(x+w/2, y, w/2)
        triangle(x+w/4, y+h/2, w/2)

triangle(x,y,w)

root.mainloop()