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
    start_number = random.randint(0, 150)
    draw_line(1*start_number, 2*start_number)

root.mainloop()