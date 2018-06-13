import unittest
from program import arabic_to_roman


class ArabToRomanTest(unittest.TestCase):
    def test_run_with_string(self):
        with self.assertRaises(ValueError):
            arabic_to_roman('num')

    def test_run_with_invalid_number(self):
        with self.assertRaises(ValueError):
            arabic_to_roman(0)
            arabic_to_roman(-2)
            arabic_to_roman(4000)

    def test_run_with_no_argument(self):
        with self.assertRaises(TypeError):
            arabic_to_roman()

    def test_run_with_valid_numbers(self):
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
