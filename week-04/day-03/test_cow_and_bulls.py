import unittest
from cow_and_bulls import CAB

class TestCab(unittest.TestCase):
    def setUp(self):
        self.cab = CAB()

    def test_check_number_format(self):
        self.assertEqual(self.cab.check_number_format(999), False)

    def test_check_number_format(self):
        self.assertEqual(self.cab.check_number_format(455), True)

    def test_count_guesses(self):
        self.cab.count_guesses()
        self.assertEqual(self.cab.count, 1)

    def test_guessing(self):
        self.cab.origin_number = 1234
        self.cab.guess_number = 1555
        self.assertEqual(self.cab.playing, "cow")

if __name__ == '__main__':
    unittest.main()