import unittest

from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_newlines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    def test_custom_single_character_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2;3"), 6)

    def test_custom_single_character_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2;3"), 6)

    def test_custom_multi_character_delimiter(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)
    
    def test_numbers_larger_than_1000(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_delimiters_with_different_lengths(self):
        self.assertEqual(self.calculator.add("//[***][%%%]\n1***2%%%3"), 6)

    def test_mixed_numbers_and_numbers_greater_than_1000(self):
        self.assertEqual(self.calculator.add("2,1000,1001"), 1002)

    def test_mixed_custom_delimiters_and_numbers_larger_than_1000(self):
        self.assertEqual(self.calculator.add("//[***][%%%]\n1***2%%%1001***3"), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-1,2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -3")

    def test_all_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,-2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -2, -3")


if __name__ == '__main__':
    unittest.main()