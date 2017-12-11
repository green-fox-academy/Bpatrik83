class Animal(object):
    def __init__(self, hunger, thirst):
        self.hunger = hunger
        self.thirst = thirst

    postit1 = Postit("orange", "Idea 1", "blue")
    postit2 = Postit("pink", "Awsome", "black")
    postit3 = Postit("yellow", "Superb!", "green")

    print(postit1.text, postit1.background_color, postit1.text_color)