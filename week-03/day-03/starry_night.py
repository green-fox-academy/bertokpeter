import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg="black")
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def draw_square(x,y):
    canvas.create_rectangle(x, y, x+5, y+5,fill="grey")

coords = []
for i in range(100):
    for j in range(2):
        coords.append(random.randint(0, 295))
    draw_square(coords[0], coords[1])
    coords = []

root.mainloop()