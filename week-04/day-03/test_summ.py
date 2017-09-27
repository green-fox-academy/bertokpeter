import unittest
from summ import Sum

summa = Sum()

class TestSum(unittest.TestCase):        
    
    int_list = [5, 7, 3]
    def test_sums_list(self):
        self.assertEqual(summa.summ(int_list),15)

if __name__=="__main__":
    unittest.main()