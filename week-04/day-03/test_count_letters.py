import unittest
from count_letters import count_letters

class TestCounter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_letters(""), {})

    def test_one_element(self):
        self.assertEqual(count_letters("a"), {"a" : 1})

    def test_multiple_element(self):
        self.assertEqual(count_letters("aabbccqq"), {"a" : 2, "b" : 2, "c" : 2, "q" : 2})

if __name__ == '__main__':
    unittest.main()