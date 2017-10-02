from tkinter import *

class View:
    def __init__(self):
        self.root = Tk()
        self.size = 720
        self.canvas = Canvas(self.root, width=self.size, height=self.size, bg="white", bd=0)
        self.floor_image = PhotoImage(file = "floor.png")
        self.canvas.pack()
        self.canvas.focus_set()    

    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                self.floor = self.canvas.create_image(j*72, i*72, anchor=NW, image=self.floor_image)

    def display(self):
        self.root.mainloop()