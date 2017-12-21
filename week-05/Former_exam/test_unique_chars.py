import unittest
from unique_chars import unique_characters

class TestUniqueChars(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(unique_characters(""), [])

    def test_string_non_unique_chars(self):
        self.assertEqual(unique_characters("aabbccddeeff"), [])

    def test_string_only_unique_chars(self):
        self.assertEqual(unique_characters("abcdefghijkl"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])

    def test_different_chars(self):
        self.assertEqual(unique_characters("monthypython"), ["m", "p"])

if __name__ == '__main__':
    unittest.main()