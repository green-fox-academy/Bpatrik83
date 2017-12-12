class Garden(object):
    def __init__(self, plants = []):
        self.plants = plants

    def add_plants(self, plant):
        self.plants.append(plant)

    def watering(self, water):
        count = 0
        for i in self.plants:
            if i.amount_water < 5 and i.type == "Flower" or i.amount_water < 10 and i.type == "Tree":
                count += 1
        water = water / count
        for i in self.plants:
            if i.type == "Flower" and i.amount_water < 5:
                i.amount_water += water * 0.75
            if i.type == "Tree" and i.amount_water < 10:
                i.amount_water += water * 0.4

    def __str__(self):
        result = ""
        for i in range(0, len(self.plants)):
            result += self.plants[i].__str__() + "\n"
        return result

class Flower():
    def __init__(self, amount_water = 0, color = "yellow", type = "Flower"):
        self.amount_water = amount_water
        self.type = type
        self.color = color

    def __str__(self):
        if self.amount_water < 5:
            result = "The " + self.color + " " + self.type + " needs water"
        else:
            result = "The " + self.color + " " + self.type + " doesnt need water"
        return result

class Tree():
    def __init__(self, amount_water = 0, color="yellow", type="Tree"):
        self.amount_water = amount_water
        self.color = color
        self.type = type

    def __str__(self):
        if self.amount_water < 10:
            result = "The " + self.color + " " + self.type + " needs water"
        else:
            result = "The " + self.color + " " + self.type + " doesnt need water"
        return result



yellow = Flower(0, "yellow", "Flower")
blue = Flower(0, "blue", "Flower")
purple = Tree(0, "purple", "Tree")
orange = Tree(0, "orange", "Tree")

garden = Garden()
garden.add_plants(yellow)
garden.add_plants(blue)
garden.add_plants(purple)
garden.add_plants(orange)

print(garden)

garden.watering(40)

print(garden)

garden.watering(70)

print(garden)