import unittest
import bertok_peter_work

class TestApples(unittest.TestCase):
    
    def test_apples(self):
        self.assertEqual(get_apple(),"apple")

if __name__=="__main__":
    unittest.main()