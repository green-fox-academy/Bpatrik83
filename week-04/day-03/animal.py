class Animal(object):
    def __init__(self, name):
        self.animal = name
        self.hunger = 50
        self.thirst = 50

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

    def __str__(self):
        return '[Race: {}, Hunger level: {}, Thirst level {}]'.format(self.animal, self.hunger, self.thirst)
