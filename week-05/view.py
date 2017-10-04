from tkinter import *
import random
from map import Map

class View:
    def __init__(self):
        self.mymap = Map()
        self.root = Tk()
        self.size = 720
        self.pressnum = 0
        self.canvas = Canvas(self.root, width=self.size, height=self.size-72, bg="white", bd=0)
        self.floor_image = PhotoImage(file = "floor.png")
        self.wall_image = PhotoImage(file = "wall.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.skeleton_image = PhotoImage(file = "skeleton.png")
        self.chars_on_screen = []
        self.root.bind("<KeyPress>", self.on_key_press)
        self.canvas.pack()
        self.canvas.focus_set()    

    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                image = self.floor_image if map[i][j]==0 else self.wall_image
                self.tile = self.canvas.create_image(j*72, i*72, anchor=NW, image=image)
    
    def draw_entity(self, image, coords):
        self.entity = self.canvas.create_image(coords[0]*72, coords[1]*72, anchor=NW, image=image)
        return self.entity
    
    def draw_hero(self, image, x, y):
        self.hero = self.draw_entity(image, [x, y])
        self.chars_on_screen.append(self.hero)

    def draw_skeletons(self):
        self.skeleton1 = self.draw_entity(self.skeleton_image, self.rand_gen())
        self.skeleton2 = self.draw_entity(self.skeleton_image, self.rand_gen())
        self.skeleton3 = self.draw_entity(self.skeleton_image, self.rand_gen())
        self.chars_on_screen.extend([self.skeleton1, self.skeleton2,self.skeleton3])
    
    def rand_gen(self):
        coords = [0, 0]
        while self.is_occupied(coords[0],coords[1]) or self.mymap.get_cell(coords[0],coords[1]) == 1:
            coords[0] = random.randint(0,9)
            coords[1] = random.randint(0,8)
        return coords
        
    def is_occupied(self, x, y):
        for image in self.chars_on_screen:
            coords = self.canvas.coords(image)
            its_occupied = coords[0] == x and coords[1] == y
            if its_occupied:
                break
        return its_occupied

    def move(self, char, dx, dy):
        self.canvas.move(char, dx*72, dy*72)

    def on_key_press(self, e):
        coords = self.canvas.coords(self.hero)
        coords[0] = coords[0]//72
        coords[1] = coords[1]//72
        self.canvas.delete(self.hero)
        self.pressnum += 1
        if e.keysym == 'Up':
            self.draw_hero(self.hero_up,coords[0], coords[1])
            if coords[1] >= 1 and not self.mymap.get_cell(coords[0],coords[1]-1) == 1:
                self.move(self.hero, 0, -1)
        elif e.keysym == 'Down':
            self.draw_hero(self.hero_down,coords[0], coords[1])
            if coords[1] <= 7 and not self.mymap.get_cell(coords[0],coords[1]+1) == 1:
                self.move(self.hero, 0, 1)
        elif e.keysym == 'Right':
            self.draw_hero(self.hero_right,coords[0], coords[1])
            if coords[0] <= 8 and not self.mymap.get_cell(coords[0]+1,coords[1]) == 1:
                self.move(self.hero, 1, 0)
        elif e.keysym == 'Left':
            self.draw_hero(self.hero_left,coords[0], coords[1])
            if coords[0] >= 1 and not self.mymap.get_cell(coords[0]-1,coords[1]) == 1:
                self.move(self.hero, -1, 0)

    def display(self):
        self.root.mainloop()