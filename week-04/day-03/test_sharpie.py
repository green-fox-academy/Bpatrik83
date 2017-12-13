import unittest
from sharpie import Sharpie

class TestSharpie(unittest.TestCase):
    def setUp(self):
        self.sharpie = Sharpie("red", 47)

    def test_init(self):
        self.assertEqual(self.sharpie.color, "red")
        self.assertEqual(self.sharpie.width, 47)

    def test_use_method(self):
        self.assertEqual(self.sharpie.use(), None)

    def test_ink_amount_without_use(self):
        self.assertEqual(self.sharpie.ink_amount, 100)

    def test_ink_amount_with_use_method_ones(self):
        self.sharpie.use()
        self.assertEqual(self.sharpie.ink_amount, 99)

    def test_ink_amount_with_use_method_ten_times(self):
        for i in range(10):
            self.sharpie.use()
        self.assertEqual(self.sharpie.ink_amount, 90)

    def test_str_with_use_method_ten_times(self):
        for i in range(100):
            self.sharpie.use()
        self.assertEqual(self.sharpie.ink_amount, 0)

if __name__ == '__main__':
    unittest.main()