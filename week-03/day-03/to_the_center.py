from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width=canvas_width, height=canvas_width)
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
def draw_line(x,y):
    canvas.create_line(x,y,canvas_width/2, canvas_height/2)

for i in (10, 50, 70):
    draw_line(1*i, 2*i)

root.mainloop()