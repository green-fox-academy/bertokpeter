class Garden(object):
    def __init__(self):
        self.flowers = []
        self.trees = []
    
    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_tree(self, tree):
        self.trees.append(tree)

    def water(self, amount):
        print("Watering with {}".format(amount))
        self.to_water = []
        for flower in self.flowers:
            if flower.status() == "needs water":
                self.to_water.append(flower)
        for tree in self.trees:
            if tree.status() == "needs water":
                self.to_water.append(tree)
        for plant in self.to_water:
            plant.watered(amount/len(self.to_water))

class Tree(object):
    def __init__(self, color):
        self.water_amount = 0
        self.color = color
    
    def needs_water(self):
        return "needs water" if self.water_amount < 10 else "doesn't need water"

    def __str__(self):
        return "The {} Tree {}".format(self.color, self.needs_water)

    def watered(self, amount):
        self.water_amount += amount*0.4    

class Flower(Tree):
    def needs_water(self):
        return "needs water" if self.water_amount < 5 else "doesn't need water"

    def __str__(self):
        return "The {} Flower {}".format(self.color, self.needs_water)

    def watered(self, amount):
        self.water_amount += amount*7.5    

mygarden = Garden()
mygarden.add_flower(Flower(yellow))
mygarden.add_flower(Flower(blue))
mygarden.add_tree(Tree(purple))
mygarden.add_tree(Tree(orange))