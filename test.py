import unittest
from program import arabic_to_roman


class ArabToRomanTest(unittest.TestCase):
    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            arabic_to_roman(0)
            arabic_to_roman('num')

    def test_program_actually_works(self):
        nums = {
            5: "V",
            11: "XI",
            25: "XXV",
            30: "XXX",
            300: "CCC",
            700: "DCC",
            1009: "MIX",
            3222: "MMMCCXXII"
        }
        for key, val in nums.items():
            self.assertEqual(arabic_to_roman(key), val)

if __name__ == '__main__':
    unittest.main()
