from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
def square_center(size,color):
    start_width = canvas_width/2-size/2
    start_height = canvas_height/2-size/2
    end_width = canvas_width/2+size/2
    end_height = canvas_height/2+size/2
    coords = [start_width, start_height, end_width, end_height]
    canvas.create_rectangle(coords, fill=color)

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
biggest = 300
for i in range(len(rainbow)):
    square_center(biggest-(i*biggest/10),rainbow[i])


root.mainloop()