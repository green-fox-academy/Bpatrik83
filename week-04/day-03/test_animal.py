import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Goat")

    def test_init(self):
        self.assertEqual(self.animal.animal, "Goat")
        self.assertEqual(self.animal.thirst, 50)
        self.assertEqual(self.animal.hunger, 50)

    def test_eat_drink_ones(self):
        self.animal.eat()
        self.animal.drink()
        self.assertEqual(self.animal.thirst, 49)
        self.assertEqual(self.animal.hunger, 49)

    def test_eat_drink_ten_times(self):
        for index in range(10):
            self.animal.eat()
            self.animal.drink()
        self.assertEqual(self.animal.thirst, 40)
        self.assertEqual(self.animal.hunger, 40)

    def test_play_ones(self):
        self.animal.play()
        self.assertEqual(self.animal.thirst, 51)
        self.assertEqual(self.animal.hunger, 51)

if __name__ == '__main__':
    unittest.main()