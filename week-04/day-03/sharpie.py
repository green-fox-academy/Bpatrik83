class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

    def __str__(self):
        if self.ink_amount <= 0:
            return "Negative!"
        return '[Color: {}, Width: {}, Ink amount: {}]'.format(self.color, self.width, self.ink_amount)
