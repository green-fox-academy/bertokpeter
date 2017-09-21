from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
w = canvas_width/2
x=canvas_width/2
y=canvas_height/2

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

def diamond(x,y,w):
    if w < 1:
        pass
    else:
        h = triangle_height(w)
        canvas.create_polygon(x-w/2, y-h, x-w/2+w, y-h, x-w/2+1.5*w, y,
        x-w/2+w, y+h, x-w/2, y+h, x-w/2-w/2, y, outline="black",width=1,fill="")
        diamond(x-w/2+w/4,y-h/2,w/2)
        diamond(x-w/2+w,y,w/2)
        diamond(x-w/2+w/4,y+h/2,w/2)

diamond(x,y,w)

root.mainloop()