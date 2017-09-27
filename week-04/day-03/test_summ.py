import unittest
from summ import Sum

summa = Sum()

class TestSum(unittest.TestCase):        
    
    def test_sums_list(self):
        int_list = [5, 7, 3]
        self.assertEqual(summa.summ(int_list),15)

    def test_empty_list(self):
        int_list = []
        self.assertEqual(summa.summ(int_list), 0)

if __name__=="__main__":
    unittest.main()