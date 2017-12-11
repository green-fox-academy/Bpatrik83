class Postit(object):

    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

postit1 = Postit("orange", "Idea 1", "blue")
postit2 = Postit("pink", "Awsome", "black")
postit3 = Postit("yellow", "Superb!", "green")

print(postit1.text, postit1.background_color, postit1.text_color)
