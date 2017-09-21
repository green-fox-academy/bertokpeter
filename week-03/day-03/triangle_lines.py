from tkinter import *
import math
root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

size=10

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

# def triangle(size):
#     for i in range(11):
#         canvas.create_polygon(45+i*size,295,150,295-triangle_height*(21-i*2),255-i*size,295,outline="black",width=2,fill="")
#         canvas.create_polygon(45+i*(size/2),295-triangle_height*i,150-i*(size/2),295-triangle_height*(21-i),255-i*size*1.5,295-triangle_height*i,outline="black",width=2,fill="")
#         canvas.create_polygon(45+i*size*1.5,295-triangle_height*i,150+i*(size/2),295-triangle_height*(21-i),255-i*(size/2),295-triangle_height*i,outline="black",width=2,fill="")

big_triangle(size)

root.mainloop()