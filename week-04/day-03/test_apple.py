import unittest
from bertok_peter_work import Apples

class TestApples(unittest.TestCase):
    
    def test_apples(self):
        apple = Apples()
        self.assertEqual(apple.get_apple(),"apple")

if __name__=="__main__":
    unittest.main()