import unittest
import solution


class SumOfDigitsTest(unittest.TestCase):
    """docstring for SumOfDigitsTest"""
    def test_sum_of_digits(self):
        self.assertEqual(10, solution.sum_of_digits(1234))
        self.assertEqual(36, solution.sum_of_digits(9999))

if __name__ == '__main__':
    unittest.main()