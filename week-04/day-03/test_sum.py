import unittest
from summa import sum_numbers

class TestSum(unittest.TestCase):
    def test_sum_an_empty_list(self):
        self.assertEqual(sum_numbers([]), 0)

    def test_sum_with_one_element(self):
        self.assertEqual(sum_numbers([5]), 5)

    def test_sum_with_three_numbers(self):
        self.assertEqual(sum_numbers([4, 5, 6]), 15)

    def test_sum_with_null(self):
        self.assertEqual(sum_numbers([0]), 0)

if __name__ == '__main__':
    unittest.main()