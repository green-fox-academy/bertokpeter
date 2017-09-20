from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas_height_middle = canvas_height/2

# draw the canvas' diagonals in green.
for i in (1, -1):
    canvas.create_line(0, canvas_height_middle - canvas_height_middle*i, canvas_width, canvas_height_middle - canvas_height_middle*-i)

root.mainloop()