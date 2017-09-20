from tkinter import *
try:
    root = Tk()

    canvas_width = 300
    canvas_height = 300
    canvas = Canvas(root, width=canvas_width, height=canvas_width)
    canvas.pack()

    # reproduce this:
    # [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
    def line_play(distance):
        for j in range(canvas_width//distance):
            canvas.create_line(0,distance*j,distance*j+distance,canvas_height, fill="green")
            canvas.create_line(distance*j,0,canvas_width,distance*j+distance, fill="purple")

    line_play(30)
    root.mainloop()
except TypeError:
    print("distance must be integer")