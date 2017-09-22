from tkinter import *
import math
root = Tk()


canvas_width = 610
canvas_height = 610
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
w = 600
x = canvas_width/2
y = canvas_height/2

def triangle_side(h):
    return math.sqrt(4*h**2/3)

def circle(x,y,w):
    if w < 15:
        pass
    else:
        initx = x - w/2
        inity = y - w/2
        tri_height = 0.75*w
        tri_side = triangle_side(tri_height)
        canvas.create_oval(initx,inity,initx+w,inity+w, outline="black", width=1, fill="")
        circle(x, y-w/4, w/2)
        circle(x-tri_side/4, y+w/8, w/2)
        circle(x+tri_side/4, y+w/8, w/2)

circle(x,y,w)

root.mainloop()