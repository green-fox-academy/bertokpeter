import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
def draw_line(x,y):
    canvas.create_line(x, y, x+50, y)

for i in range(3):
    start_width = random.randint(0, 250)
    start_height = random.randint(0, 300)
    draw_line(start_width, start_height)

root.mainloop()