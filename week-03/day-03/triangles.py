from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

little_triangle=10
triangle_height = math.sqrt(little_triangle**2-(little_triangle/2)**2)
def triangle(size):
    for i in range(11):
        canvas.create_polygon(45+i*size,295,150,295-triangle_height*(21-i*2),255-i*size,295,outline="black",width=2,fill="")
        canvas.create_polygon(45+i*(size/2),295-triangle_height*i,150-i*(size/2),295-triangle_height*(21-i),255-i*size*1.5,295-triangle_height*i,outline="black",width=2,fill="")
        canvas.create_polygon(45+i*size*1.5,295-triangle_height*i,150+i*(size/2),295-triangle_height*(21-i),255-i*(size/2),295-triangle_height*i,outline="black",width=2,fill="")

triangle(little_triangle)

root.mainloop()