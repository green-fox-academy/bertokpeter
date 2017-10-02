from tkinter import *
import time

class View:
    def __init__(self):
        self.root = Tk()
        self.size = 720
        self.canvas = Canvas(self.root, width=self.size, height=self.size-72, bg="white", bd=0)
        self.floor_image = PhotoImage(file = "floor.png")
        self.wall_image = PhotoImage(file = "wall.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.root.bind("<KeyPress>", self.on_key_press)
        self.canvas.pack()
        self.canvas.focus_set()    

    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                image = self.floor_image if map[i][j]==0 else self.wall_image
                self.level = self.canvas.create_image(j*72, i*72, anchor=NW, image=image)
    
    def draw_entity(self, image, x, y):
        if image == "hero":
            image = self.hero_down
        self.entity = self.canvas.create_image(x*72, y*72, anchor=NW, image=image)
    
    def move(self, char, dx, dy):
        for i in range(10):
            time.sleep(0.05)
            self.canvas.update()
            self.canvas.move(char, dx*7.2, dy*7.2)
    
    def on_key_press(self, e):
        coords = self.canvas.coords(self.entity)
        self.canvas.delete(self.entity)
        if e.keysym == 'Up':
            self.entity = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.hero_up)
            self.move(self.entity, 0, -1)
        elif e.keysym == 'Down':
            self.entity = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.hero_down)
            self.move(self.entity, 0, 1)
        elif e.keysym == 'Right':
            self.entity = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.hero_right)
            self.move(self.entity, 1, 0)
        elif e.keysym == 'Left':
            self.entity = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.hero_left)
            self.move(self.entity, -1, 0)

    def display(self):
        self.root.mainloop()