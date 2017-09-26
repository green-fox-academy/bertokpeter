class Garden(object):
    def __init__(self):
        self.plants = []

    def add(self, plant):
        self.plants.append(plant)

    def water(self, amount):
        print("Watering with {}".format(amount))
        self.to_water = []
        for plant in self.plants:
            if plant.needs_water() == "needs water":
                self.to_water.append(plant)
        for plant in self.to_water:
            plant.watered(amount/len(self.to_water))
        print(self)

    def __str__(self):
        result = ""
        for i in range(len(self.plants)):
             result += self.plants[i].__str__() + "\n"
        return result

class Tree(object):
    def __init__(self, color):
        self.water_amount = 0
        self.color = color
    
    def needs_water(self):
        return "needs water" if self.water_amount < 10 else "doesn't need water"

    def __str__(self):
        return "The {} Tree {}".format(self.color, self.needs_water())

    def watered(self, amount):
        self.water_amount += amount*0.4    

class Flower(Tree):
    def needs_water(self):
        return "needs water" if self.water_amount < 5 else "doesn't need water"

    def __str__(self):
        return "The {} Flower {}".format(self.color, self.needs_water())

    def watered(self, amount):
        self.water_amount += amount*7.5    

mygarden = Garden()
mygarden.add(Flower("yellow"))
mygarden.add(Flower("blue"))
mygarden.add(Tree("purple"))
mygarden.add(Tree("orange"))
print(mygarden)
mygarden.water(40)
mygarden.water(70)