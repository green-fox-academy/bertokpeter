import unittest
from count_letters import count_letters

class TestCountLetters(unittest.TestCase):

    def test_count_letters_one_letter(self):
        self.assertEqual(count_letters("a"),{"a":1})  
    
    def test_count_letters_another_letter(self):
        self.assertEqual(count_letters("b"),{"b":1})  
    
    def test_count_letters_more_letters(self):
        self.assertEqual(count_letters("ab"),{"a":1,"b":1})  
    


if __name__=="__main__":
    unittest.main()