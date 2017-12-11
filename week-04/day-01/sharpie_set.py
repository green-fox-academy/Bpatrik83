class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

    def __str__(self):
        return '[Color: {}, Width: {}, Ink amount: {}]'.format(self.color, self.width, self.ink_amount)


class Sharpie_Set(object):
    sharpie_list = []

    def count_usable(self):
        pass

    def remove_trash(self):
        for i in range(len(self.sharpie_list)):
            


sharpie_set = Sharpie_Set()
slist = Sharpie_Set.sharpie_list
red = Sharpie("Red", 20)
yellow = Sharpie("Yellow", 70)
blue = Sharpie("blue", 70)
slist.append(red)
slist.append(yellow)
slist.append(blue)
sharpie_set.remove_trash()


print(red)
for i in range(100):
    red.use()
    yellow.use()
    blue.use()
print(red)
print(*slist)
