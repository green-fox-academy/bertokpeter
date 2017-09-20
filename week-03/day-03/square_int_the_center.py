from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# draw a green 10x10 square to the center of the canvas.

green_square = canvas.create_rectangle(canvas_width/2-10, canvas_height/2-10, canvas_width/2+10, canvas_height/2+10, fill="green")

root.mainloop()