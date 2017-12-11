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

def all_six(dice):
    check = 0
    while(check != 36):
        check = 0
        dice.roll()
        print(dice.get_current())
        for i in dice.get_current():
            check += i
        if check == 36:
            print(dice.get_current())



all_six(dice)