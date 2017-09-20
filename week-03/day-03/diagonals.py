from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
middle = canvas_height/2

# draw the canvas' diagonals in green.
for i in (1, -1):
    canvas.create_line(0, middle - middle*i, canvas_width, middle - middle*-i, fill="green")

root.mainloop()