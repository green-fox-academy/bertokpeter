import unittest
from apple import Apples

apple = Apples()

class TestApples(unittest.TestCase):        
    
    def test_apple(self):
        self.assertEqual(apple.get_apple(),"apple")
    
    def test_not_apple(self):
        self.assertEqual(apple.get_apple(),"monkey")

if __name__=="__main__":
    unittest.main()