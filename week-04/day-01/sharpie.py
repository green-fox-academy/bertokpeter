class Sharpie(object):
    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = 100.0

    def use(self, amount):
        self.ink_amount -= amount
        return self.ink_amount

    def __repr__(self):
       return "Sharpie color: {}, Sharpie width: {}".format(self.color, self.width)

sharp = Sharpie("medve",50)
print(sharp.color)
sharp.use(6.5)
print(sharp.ink_amount)