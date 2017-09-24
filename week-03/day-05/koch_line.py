from tkinter import *
import math
root = Tk()

w = 600
x = 0
y = 0

canvas_width = 600
canvas_height = 350
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

def koch_line(x,y,w):
    canvas.create_line(x,y+w/2,x+w,y+w/2)
    koch_fractal(x+w/3,y+w/2,w/3,300,60,0)
    koch_fractal(x+w/9,y+w/2,w/9,300,60,0)
    koch_fractal(x+w*7/9,y+w/2,w/9,300,60,0)
    koch_fractal(x+w*1/27,y+w/2,w/27,300,60,0)
    koch_fractal(x+w*7/27,y+w/2,w/27,300,60,0)
    koch_fractal(x+w*19/27,y+w/2,w/27,300,60,0)
    koch_fractal(x+w*25/27,y+w/2,w/27,300,60,0)

def turn(x,y,w,a):
    radians = a * math.pi / 180
    end_x = x + w * math.cos(radians)
    end_y = y + w * math.sin(radians)
    return [end_x,end_y]

def koch_fractal(x,y,w,a,b,c):
    if w < 10:
        pass
    else:
        end = turn(x,y,w,a)
        canvas.create_line(x,y,end)
        end2 = turn(end[0],end[1],w,b)
        canvas.create_line(end,end2)
        end3 = turn(x,y,w,c)
        canvas.create_line(x,y,end3,fill="white",width=2)
        koch_fractal(turn(x,y,w/3,a)[0],turn(x,y,w/3,a)[1],w/3,a+300,b-60,c+300)
        koch_fractal(turn(x,y,w/9,a)[0],turn(x,y,w/9,a)[1],w/9,a+300,b-60,c+300)
        koch_fractal(turn(x,y,w*7/9,a)[0],turn(x,y,w*7/9,a)[1],w/9,a+300,b-60,c+300)
        koch_fractal(turn(end[0],end[1],w/3,b)[0],turn(end[0],end[1],w/3,b)[1],w/3,a-300,b+60,c-300)
        koch_fractal(turn(end[0],end[1],w/9,b)[0],turn(end[0],end[1],w/9,b)[1],w/9,a-300,b+60,c-300)
        koch_fractal(turn(end[0],end[1],w*7/9,b)[0],turn(end[0],end[1],w*7/9,b)[1],w/9,a-300,b+60,c-300)

koch_line(x,y,w)

root.mainloop()