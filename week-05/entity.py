import random

class Entity:
    def __init__(self, drawing):
        self.picture = drawing
        self.level = 1
        self.maxhp = 0
        self.currenthp = self.maxhp
        self.sp = 0
        self.dp = 0
        self.status = "peace"

    def get_stats(self):
        self.stats = {"level":self.level,
                      "maxhp":self.maxhp,
                      "currenthp":self.currenthp,
                      "sp":self.sp,
                      "dp":self.dp}

    def get_coords(self, coords):
        self.coords = coords
        self.coords[0] = int(self.coords[0])//72
        self.coords[1] = int(self.coords[1])//72
        return self.coords
        
    def dice(self):
        return random.randint(1,6)

class Hero(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 20 + 3*self.dice()
        self.currenthp = self.maxhp
        self.sp = 2*self.dice()
        self.dp = 5 + self.dice()
        self.name = "Hero"
        self.get_stats()

    def level_up(self):
        self.level += 1
        self.maxhp += self.dice()
        self.currenthp = self.maxhp
        self.sp += self.dice()
        self.dp += self.dice()

class Skeleton(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 2*self.level*self.dice()
        self.currenthp = self.maxhp
        self.sp = self.level/2*self.dice()
        self.dp = self.level*self.dice()
        self.name = "Skeleton"
        self.get_stats()

class Boss(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 1000 + 3*self.level*self.dice() + self.dice()
        self.currenthp = self.maxhp
        self.sp = self.level*self.dice() + self.dice()/2
        self.dp = self.level*self.dice() + self.level
        self.name = "Boss"
        self.get_stats()