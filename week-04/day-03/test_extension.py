import unittest
from extend import *

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(add(4, 1), 5)

    def test_add_4_and_5_is_9(self):
        self.assertEqual(add(4, 5), 9)

    def test_add_negatives(self):
        self.assertEqual(add(-4, -5), -9)

    def test_add_floats(self):
        self.assertEqual(add(4.5, 4.5), 9)

    def test_max_of_three_first(self):
        self.assertEqual(max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(max_of_three(3, 5, 4), 5)

    def test_median_four(self):
        self.assertEqual(median([7,4,3,5]), 4.5)

    def test_median_five(self):
        self.assertEqual(median([1,2,3,4,5]), 3)

    def test_median_five_scrambled(self):
        self.assertEqual(median([5,2,4,1,3]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(is_vovel('u'))

    def test_is_vovel_ú(self):
        self.assertTrue(is_vovel('ú'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(translate('kolbice'), 'kovolbiviceve')

    def test_translate_makaroni(self):
        self.assertEqual(translate('makaróni'), 'mavakavaróvónivi')

if __name__ == '__main__':
    unittest.main()