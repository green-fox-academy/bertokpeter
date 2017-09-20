import random
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
colors = ["red", "green", "blue", "pink"]
coords = []
for i in range(4):
    for j in range(4):
        coords.append(random.randint(0, 300))
    canvas.create_rectangle(coords, fill=colors[i])
    coords = []

root.mainloop()