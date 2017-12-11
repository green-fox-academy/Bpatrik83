class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

    def __str__(self):
        return '[Color: {}, Width: {}, Ink amount: {}]'.format(self.color, self.width, self.ink_amount)


red = Sharpie("Red", 20)
print(red)
for i in range(73):
    red.use()
print(red)
