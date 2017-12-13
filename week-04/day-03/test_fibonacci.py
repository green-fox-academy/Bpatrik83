import unittest
from fibonacci import fibonacci_start_one

class TestFibonacci(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fibonacci_start_one(0), None)

    def test_negative(self):
        self.assertEqual(fibonacci_start_one(-1), None)

    def test_valid_number(self):
        self.assertEqual(fibonacci_start_one(11), 89)

    def test_too_big_number(self):
        self.assertEqual(fibonacci_start_one(36), "Too big!")

if __name__ == '__main__':
    unittest.main()