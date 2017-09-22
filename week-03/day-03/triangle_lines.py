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

def triangle_height(size):
     return math.sqrt(size**2-(size/2)**2)

def big_triangle(size):
    big_width = size*21
    big_height = triangle_height(big_width)
    left_x =  canvas_width/2 - big_width/2
    left_y = canvas_height/2 + big_height/2
    right_x = canvas_width/2 + big_width/2
    right_y = canvas_height/2 + big_height/2
    top_x = canvas_width/2
    top_y = canvas_height/2 - big_height/2
    return [left_x,left_y,right_x,right_y,top_x,top_y]

def triangles_in_triangles(size):
    height = triangle_height(size)
    coords = big_triangle(size)
    for i in range(21):
        canvas.create_line(coords[0]+i*(size/2),coords[1]-i*height,coords[2]-i*(size/2),coords[3]-i*height)
        canvas.create_line(coords[0]+i*size,coords[1],coords[4]+i*(size/2),coords[5]+i*height)
        canvas.create_line(coords[4]-i*(size/2),coords[5]+i*height,coords[2]-i*size,coords[3])

triangles_in_triangles(size)

root.mainloop()