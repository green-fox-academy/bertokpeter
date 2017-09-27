import unittest
from anagram import anagram

class TestAnagram(unittest.TestCase):        
    
    def test_is_anagram(self):
        word1 = "kocsi"
        word2 = "ickso"
        self.assertTrue(anagram(word1, word2))
    
    def test_diff_length(self):
        word1 = "bakocsi"
        word2 = "kocsi"
        self.assertFalse(anagram(word1, word2))

if __name__=="__main__":
    unittest.main()