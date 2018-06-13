import unittest
from program import arabic_to_roman


class ArabToRomanTest(unittest.TestCase):
    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            arabic_to_roman('num')

    def test_program_actually_works(Self):
        test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,
            50,60,69,70,80,90,99,100,200,300,400,500,600,666,700,800,900,
            1000,1009,1444,1666,1945,1997,1999,2000,2008,2010,2011,2500,
            3000,3999)
        for val in test:
            return arabic_to_roman(val)

if __name__ == '__main__':
    unittest.main()
