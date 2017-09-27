import unittest
from count_letters import count_letters

class TestCountLetters(unittest.TestCase):

    def test_count_letters_one_letter(self):
        self.assertEqual(count_letters("a"),{"a":1})  
    


if __name__=="__main__":
    unittest.main()