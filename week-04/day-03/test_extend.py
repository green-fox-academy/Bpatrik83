import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 6), 8)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 6), 10)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 10, 3), 10)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 10), 10)

    def test_median_four(self):
        self.assertEqual(extend.median([15, 5, 15, 5]), 10)

    def test_median_five(self):
        self.assertEqual(extend.median([4, 4, 10, 2, 5]), 5)

    def test_is_vovel_a(self):
        self.assertEqual(extend.is_vovel("a"), True)

    def test_is_vovel_u(self):
        self.assertEqual(extend.is_vovel("s"), False)

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate("bemutatkozik"), "bevemuvutavatkovozivik")

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate("kolostor"), "kovolovostovor")

if __name__ == '__main__':
    unittest.main()