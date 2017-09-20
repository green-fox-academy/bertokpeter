from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_width)
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
canvas_center = canvas_width//2

def line_play(distance,x,y):
    for j in range(canvas_center//distance):
        canvas.create_line(x,y+distance*j,x+distance*j+distance,y+canvas_center, fill="green")
        canvas.create_line(x+distance*j,y,x+canvas_center,y+distance*j+distance, fill="purple")

line_play(10,0,0)
line_play(10,canvas_center,0)
line_play(10,0,canvas_center)
line_play(10,canvas_center,canvas_center)

root.mainloop()