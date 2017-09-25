class Animal(object):
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
    
    def eat(self):
        self.hunger -= 1
    
    def drink(self):
        self.thirst -= 1

    def play(self):
        self.thirst += 1
        self.hunger += 1