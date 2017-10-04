from view import View
from map import Map
from entity import *
import random

class Game:
    def __init__(self):
        self.mymap = Map()
        self.myview = View()
        self.myhero = Hero()
        self.myview.root.bind("<KeyPress>", self.on_key_press)
        self.myview.draw_map(self.mymap.tiles)
        self.chars_on_screen = []
        self.draw_hero(self.myview.hero_down, 0, 0)
        self.draw_skeletons()
        self.draw_boss()
        self.myview.draw_hud(self.myhero.level,self.myhero.maxhp,self.myhero.currenthp,self.myhero.sp,self.myhero.dp)
        self.myview.display()
    
    def draw_hero(self, image, x, y):
        self.hero = self.myview.draw_entity(image, [x, y])
        self.chars_on_screen.append(self.hero)

    def draw_skeletons(self):
        self.skeleton1 = self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen())
        self.skeleton2 = self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen())
        self.skeleton3 = self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen())
        self.chars_on_screen.extend([self.skeleton1, self.skeleton2,self.skeleton3])

    def draw_boss(self):
        self.boss = self.myview.draw_entity(self.myview.boss_image, self.rand_gen())
        self.chars_on_screen.append(self.boss)  

    def rand_gen(self):
        coords = [0, 0]
        while self.is_occupied(coords[0],coords[1]) or self.mymap.get_cell(coords[0],coords[1]) == 1:
            coords[0] = random.randint(0,9)
            coords[1] = random.randint(0,8)
        return coords
        
    def is_occupied(self, x, y):
        for image in self.chars_on_screen:
            coords = self.myview.canvas.coords(image)
            its_occupied = coords[0] == x and coords[1] == y
            if its_occupied:
                break
        return its_occupied

    def move(self, char, dx, dy):
         self.myview.canvas.move(char, dx*72, dy*72)
    
    def turn_hero(self, image):
        self.myview.canvas.itemconfig(self.hero, image=self.myview.hero_images[image])

    def on_key_press(self, e):
        coords = self.myview.canvas.coords(self.hero)
        coords[0] = coords[0]//72
        coords[1] = coords[1]//72
        if e.keysym == 'Up':
            self.turn_hero("up")
            if coords[1] >= 1 and not self.mymap.get_cell(coords[0],coords[1]-1) == 1:
                self.move(self.hero, 0, -1)
        elif e.keysym == 'Down':
            self.turn_hero("down")
            if coords[1] <= 7 and not self.mymap.get_cell(coords[0],coords[1]+1) == 1:
                self.move(self.hero, 0, 1)
        elif e.keysym == 'Right':
            self.turn_hero("right")
            if coords[0] <= 8 and not self.mymap.get_cell(coords[0]+1,coords[1]) == 1:
                self.move(self.hero, 1, 0)
        elif e.keysym == 'Left':
            self.turn_hero("left")
            if coords[0] >= 1 and not self.mymap.get_cell(coords[0]-1,coords[1]) == 1:
                self.move(self.hero, -1, 0)

game = Game()