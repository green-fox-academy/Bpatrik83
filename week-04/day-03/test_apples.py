import unittest
from apple import Apple

class test_apple(unittest.TestCase):
    def setUp(self):
        self.apple = Apple()

    def test_apple(self):
        self.assertEqual(self.apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()
