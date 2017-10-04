import random

class Entity:
    def __init__(self):
        self.d6 = random.randint(1,6)
        self.level = 1
        self.maxhp = 20 + 3*self.d6
        self.currenthp = self.maxhp
        self.sp = 2*self.d6
        self.dp = 5 + self.d6

class Hero(Entity):
    pass

class Skeleton(Entity):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.maxhp = 2*level*self.d6
        self.sp = level/2*self.d6
        self.dp = level*self.d6

class Boss(Entity):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.maxhp = 2*level*self.d6 + self.d6
        self.sp = level/2*self.d6 + self.d6/2
        self.dp = level*self.d6 + level