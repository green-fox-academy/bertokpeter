from tkinter import *

try:
    root = Tk()

    canvas_width = 300
    canvas_height = 300
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # fill the canvas with a checkerboard pattern.
    def draw_checkboard(number_of_rows):
        size = canvas_width/number_of_rows
        start_width = 0
        start_height = 0
        for i in range(number_of_rows):
            for j in range((number_of_rows+1)//2):
                end_width = start_width + size
                end_height = start_height + size
                coords = [start_width, start_height, end_width, end_height]
                canvas.create_rectangle(coords, fill="black")
                start_width = end_width + size
            if i%2 == 0:
                start_width = size
            else:
                start_width = 0
            start_height += size 

    draw_checkboard(8)
    root.mainloop()
except TypeError:
    print("row_size must be integer")