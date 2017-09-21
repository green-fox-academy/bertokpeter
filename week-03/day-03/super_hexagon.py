from tkinter import *
import math
root = Tk()

canvas_width = 600
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

size=20
row_number = 7

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

def middle_hexagon(size):
    middle = canvas_width/2
    height = triangle_height(size)
    half = size/2
    far_left_x = middle-size
    near_left_x = middle-half
    near_right_x = middle+half
    far_right_x = middle+size
    top_height = middle-height  
    bottom_height = middle+height 
    return [far_left_x,near_left_x,near_right_x,far_right_x,top_height,middle,bottom_height]

def hexagon(size,number):
    c = middle_hexagon(size)
    co = [c[0],c[5],c[1],c[4],c[2],c[4],c[3],c[5],c[2],c[6],c[1],c[6]]
    canvas.create_polygon(co,outline="black",fill="")


        
hexagon(size,row_number)

root.mainloop()