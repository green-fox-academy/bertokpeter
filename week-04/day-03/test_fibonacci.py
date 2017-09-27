import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci(-5), 0)

    def test_fibonacci_string(self):
        self.assertRaises(TypeError, fibonacci("apple"))  

    def test_fibonacci_null(self):
        self.assertRaises(TypeError, fibonacci(None))  

    def test_fibonacci_float(self):
        self.assertRaises(TypeError, fibonacci(5.5))  
    
if __name__=="__main__":
    unittest.main()