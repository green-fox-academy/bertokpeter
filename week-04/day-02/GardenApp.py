class Garden(object):
    def __init__(self):
        self.flowers = []
        self.trees = []
    
    def water(self, amount):
        self.to_water = []
        for flower in self.flowers:
            if flower.status == "needs water":
                self.to_water.append(flower)
        for tree in self.trees:
            if tree.status == "needs water":
                self.to_water.append(tree)
        for plant in self.to_water:
            amount/len(self.to_water)