import unittest
from anagram import anagram

class TestAnagram(unittest.TestCase):        
    
    def test_is_anagram(self):
        word1 = "baba"
        word2 = "baab"
        self.assertTrue(anagram(word1, word2))

if __name__=="__main__":
    unittest.main()