import random

class Entity:
    def __init__(self, drawing):
        self.picture = drawing
        self.level = 1
        self.maxhp = 0
        self.currenthp = self.maxhp
        self.sp = 0
        self.dp = 0

    def get_stats(self):
        self.stats = {"level":self.level,
                      "maxhp":self.maxhp,
                      "currenthp":self.currenthp,
                      "sp":self.sp,
                      "dp":self.dp}
        
    def dice(self):
        return random.randint(1,6)

class Hero(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 20 + 3*self.dice()
        self.currenthp = self.maxhp
        self.sp = 2*self.dice()
        self.dp = 5 + self.dice()
        self.get_stats()
        print(self.stats)

class Skeleton(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 2*self.level*self.dice()
        self.currenthp = self.maxhp
        self.sp = self.level/2*self.dice()
        self.dp = self.level*self.dice()
        self.get_stats()
        print(self.stats)

class Boss(Entity):
    def __init__(self, drawing):
        super().__init__(drawing)
        self.maxhp = 2*self.level*self.dice() + self.dice()
        self.currenthp = self.maxhp
        self.sp = self.level/2*self.dice() + self.dice()/2
        self.dp = self.level*self.dice() + self.level
        self.get_stats()
        print(self.stats)