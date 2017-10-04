from tkinter import *

class View:
    def __init__(self):
        self.root = Tk()
        self.size = 720
        self.canvas = Canvas(self.root, width=self.size, height=self.size, bg="white", bd=0)
        self.floor_image = PhotoImage(file = "floor.png")
        self.wall_image = PhotoImage(file = "wall.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_images = {"down": self.hero_down,
                            "up": self.hero_up,
                            "right": self.hero_right,
                            "left": self.hero_left}
        self.skeleton_image = PhotoImage(file = "skeleton.png")
        self.boss_image = PhotoImage(file= "boss.png")
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
    
    def draw_hud(self,level,max,hp,sp,dp):
        text = ("Hero (Level " + str(level) + ") HP: " + str(hp) + "/" + str(max) +
                " | DP: " + str(dp) + " | SP: " + str(sp))
        self.canvas.create_text(5,650, anchor=NW, font=24, text=text)    

    def display(self):
        self.root.mainloop()