import random

class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()


dice = Dice()
print(dice.get_current())
dice.roll()
print(dice.get_current())
dice.reroll(3)
print(dice.get_current(3))
print(dice.get_current())

def all_six(dice_list):
    for i in range(len(dice_list.dice)):
        if dice_list.dice[i] != 6:
            while dice_list.dice[i] != 6:
                dice_list.reroll(i)

all_six(dice)
print(dice.get_current())