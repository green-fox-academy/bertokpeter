from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_width)
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def draw_line(x,y):
    canvas.create_line(x,y,canvas_width/2, canvas_height/2)

for j in range(canvas_width//20+1):
    draw_line(20*j,0)
    draw_line(0,20*j)
    draw_line(20*j,canvas_height)
    draw_line(canvas_width,20*j)


root.mainloop()