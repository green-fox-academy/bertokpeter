from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
box_coord = [50, 50, 250, 250]
box = canvas.create_rectangle(box_coord, fill="red")

root.mainloop()