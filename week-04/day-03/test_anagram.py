import unittest
from anagram import check_anagram

class TestAngram(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(check_anagram("", ""), True)

    def test_is_anagram(self):
        self.assertEqual(check_anagram("dog", "god"), True)

    def test_is_not_anagram(self):
        self.assertEqual(check_anagram("doga", "god"), False)

    def test_is_anagram_lowerCase_upperCase(self):
        self.assertEqual(check_anagram("Dog", "God"), True)

if __name__ == '__main__':
    unittest.main()