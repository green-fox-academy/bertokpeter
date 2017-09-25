from sharpie import Sharpie

class SharpieSet(object):
    def __init__(self):
        self.sharpies = [Sharpie("red", 50), Sharpie("green", 10), Sharpie("blue", 90)]

    def count_usable(self):
        self.number_of_usable = 0
        for sharpie in self.sharpies:
            if sharpie.ink_amount > 0:
                self.number_of_usable += 1
        return self.number_of_usable
    
    def remove_trash(self):
        for sharpie in self.sharpies:
            if sharpie.ink_amount == 0:
                self.sharpies.remove(sharpie)
        return self.sharpies

sharpie_set = SharpieSet()
sharpie_set.sharpies[0].use(100)
print(sharpie_set.count_usable())
print(sharpie_set.remove_trash())
