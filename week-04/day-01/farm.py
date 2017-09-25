class Animal(object):
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
    
    def eat(self):
        self.hunger -= 1
        return self.hunger

    def drink(self):
        self.thirst -= 1
        return self.thirst

    def play(self):
        self.thirst += 1
        self.hunger += 1
        return self.hunger, self.thirst

    def __repr__(self):
        return self.name

class Farm(object):
    def __init__(self):
        self.animals = [Animal("Boy"), Animal("Girl"), Animal("Pig")]
        self.slots = 8
    
    def breed(self):
        if self.slots > 0:
            self.animals.append(Animal("Malac"))
            self.slots -= 1
        return self.animals

    def feed(self, animal):
        for i in self.animals:
            if i.name == animal:
                evett = i
                i.eat()
        return evett.hunger

    def slaughter(self):
        self.hunger_list = []
        for i in self.animals:
            self.hunger_list.append(i.hunger)
        self.animals.remove(self.animals[self.hunger_list.index(min(self.hunger_list))])
        return self.animals

farm = Farm()
farm.feed("Boy")
print(farm.slaughter())