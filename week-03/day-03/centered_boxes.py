from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
def square_center(size,color):
    start_width = canvas_width/2-size/2
    start_height = canvas_height/2-size/2
    end_width = canvas_width/2+size/2
    end_height = canvas_height/2+size/2
    coords = [start_width, start_height, end_width, end_height]
    canvas.create_rectangle(coords, fill=color)

square_center(200,"red")
square_center(100,"blue")
square_center(50,"green")

root.mainloop()