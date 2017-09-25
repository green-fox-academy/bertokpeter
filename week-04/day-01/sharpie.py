class Sharpie(object):
    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        ink_amount = 100.0

sharp = Sharpie("medve",50)
print(sharp.color)
print(sharp.width)