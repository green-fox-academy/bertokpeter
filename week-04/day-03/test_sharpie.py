import unittest
from sharpie import Sharpie


class TestSharpie(unittest.TestCase):
    
    def test_sharpie_use_whole_number(self):
        sharpie = Sharpie("red", 50)
        self.assertEqual(sharpie.use(60), 40)
    
    def test_sharpie_use_float_number(self):
        sharpie = Sharpie("red", 50)
        self.assertEqual(sharpie.use(6.5), 93.5)
    
    def test_sharpie_use_zero(self):
        sharpie = Sharpie("red", 50)
        self.assertEqual(sharpie.use(0), 100)
    
    def test_sharpie_use_negative(self):
        sharpie = Sharpie("red", 50)
        sharpie.use(50)
        self.assertEqual(sharpie.use(-5), 55)
    
    def test_sharpie_use_max(self):
        sharpie = Sharpie("red", 50)
        self.assertEqual(sharpie.use(-5), 100)

if __name__=="__main__":
    unittest.main()