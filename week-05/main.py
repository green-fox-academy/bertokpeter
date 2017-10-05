from view import View
from map import Map
from entity import *
import random

class Game:
    def __init__(self):
        self.mymap = Map()
        self.myview = View()
        self.myview.root.bind("<KeyPress>", self.on_key_press)
        self.myview.draw_map(self.mymap.tiles)
        self.chars_on_screen = []
        self.myhero = Hero(self.myview.draw_entity(self.myview.hero_down, [0, 0]))
        self.chars_on_screen.append(self.myhero)
        self.skeleton1 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton1)
        self.skeleton2 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton2)
        self.skeleton3 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton3)
        self.myboss = Boss(self.myview.draw_entity(self.myview.boss_image, self.rand_gen()))
        self.chars_on_screen.append(self.myboss)  
        self.myview.draw_stats(self.myhero.name, self.myhero.stats)
        self.myview.display()
    
    def rand_gen(self):
        coords = [0, 0]
        while (self.is_occupied(self.chars_on_screen, coords[0],coords[1]) 
              or self.mymap.get_cell(coords[0],coords[1]) == 1):
            coords[0] = random.randint(0,9)
            coords[1] = random.randint(0,8)
        return coords
        
    def is_occupied(self, char_list, x, y):
        for char in char_list:
            coords = self.myview.canvas.coords(char.picture)
            its_occupied = int(coords[0]//72) == x and int(coords[1]//72) == y
            if its_occupied:
                break
        return its_occupied

    def move(self, char, dx, dy):
         self.myview.canvas.move(char, dx*72, dy*72)
    
    def turn_hero(self, image):
        self.myview.canvas.itemconfig(self.myhero.picture, image=self.myview.hero_images[image])

    def on_key_press(self, e):
        coords = self.myhero.get_coords(self.myview.canvas.coords(self.myhero.picture))
        if e.keysym == 'Up':
            self.turn_hero("up")
            if coords[1] >= 1 and not self.mymap.get_cell(coords[0],coords[1]-1) == 1:
                self.move(self.myhero.picture, 0, -1)
        elif e.keysym == 'Down':
            self.turn_hero("down")
            if coords[1] <= 7 and not self.mymap.get_cell(coords[0],coords[1]+1) == 1:
                self.move(self.myhero.picture, 0, 1)
        elif e.keysym == 'Right':
            self.turn_hero("right")
            if coords[0] <= 8 and not self.mymap.get_cell(coords[0]+1,coords[1]) == 1:
                self.move(self.myhero.picture, 1, 0)
        elif e.keysym == 'Left':
            self.turn_hero("left")
            if coords[0] >= 1 and not self.mymap.get_cell(coords[0]-1,coords[1]) == 1:
                self.move(self.myhero.picture, -1, 0)
        coords = self.myhero.get_coords(self.myview.canvas.coords(self.myhero.picture))
        if self.is_occupied(self.chars_on_screen[1:], coords[0], coords[1]):
           self.myview.draw_stats(self.skeleton1.name,self.skeleton1.stats)

game = Game()