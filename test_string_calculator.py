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


if __name__ == '__main__':
    unittest.main()