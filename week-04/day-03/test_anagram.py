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
    
    def test_diff_length_same_letters(self):
        word1 = "bababababa"
        word2 = "baba"
        self.assertFalse(anagram(word1, word2))
    
    def test_same_length_same_letters(self):
        word1 = "babacababa"
        word2 = "bbbbcaaaaa"
        self.assertTrue(anagram(word1, word2))
    
    def test_same_length_same_letters_but_not_all(self):
        word1 = "babacababa"
        word2 = "bkkkcaaaaa"
        self.assertFalse(anagram(word1, word2))

if __name__=="__main__":
    unittest.main()