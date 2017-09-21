from tkinter import *
import math
import time
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
    if w < 15:
        pass
    else:
        start_x = x - w/2
        height = triangle_height(w)
        canvas.create_line(start_x,y-height,start_x+w,y-height)
        canvas.create_line(start_x+w,y-height,start_x+1.5*w,y)
        canvas.create_line(start_x+1.5*w,y,start_x+w,y+height)
        canvas.create_line(start_x+w,y+height,start_x,y+height)
        canvas.create_line(start_x,y+height,start_x-w/2,y)
        canvas.create_line(start_x-w/2,y,start_x,y-height)
        diamond(start_x+w/4,y-height/2,w/2)
        diamond(start_x+w,y,w/2)
        diamond(start_x+w/4,y+height/2,w/2)

diamond(x,y,w)

root.mainloop()