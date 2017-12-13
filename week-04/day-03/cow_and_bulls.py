import random

class CAB(object):
    def __init__(self):
        self.origin_number = self.generate_random_number()
        self.count = 0
        self.playing = ""
        self.finished = False

    def generate_random_number(self):
        return random.randint(999, 9999)

    def check_number_format(self, number):
        return number < 9999 and type(number) == int and number > 999

    def count_guesses(self):
        self.count += 1

    def guessing(self):
        while(not self.finished):
            self.count_guesses()
            try:
                self.guess_number = int(input("Please enter your guess: "))
                if not self.check_number_format(self.guess_number):
                    raise ValueError
                else:
                    self.guess_number = str(self.guess_number)
                    self.origin_number = str(self.origin_number)
                    self.playing = ""
                    for index in range(len(self.guess_number)):
                        if self.guess_number[index] == self.origin_number[index]:
                            self.playing += "cow"
                        elif self.guess_number[index] in self.origin_number:
                            self.playing += "bull"
                    print(self.playing)

                    if self.playing == "cow" * 4:
                        return print("You found the correct number!")
            except ValueError:
                print("Please enter four digits positive integer number!")
            print("This is your " + str(self.count) + ". guesses")

cab = CAB()
cab.guessing()
