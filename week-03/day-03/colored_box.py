from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
box_coord = [50, 50, 250, 250]
box = canvas.create_rectangle(box_coord, fill="grey")
canvas.create_line(box_coord[0], box_coord[0], box_coord[2], box_coord[0], fill="purple", width=3)
canvas.create_line(box_coord[0], box_coord[0], box_coord[0], box_coord[2], fill="red", width=3)
canvas.create_line(box_coord[0], box_coord[2], box_coord[2], box_coord[2], fill="blue", width=3)
canvas.create_line(box_coord[2], box_coord[0], box_coord[2], box_coord[2], fill="green", width=3)

root.mainloop()