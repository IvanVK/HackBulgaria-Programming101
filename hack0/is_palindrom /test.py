import unittest
import solution


class IsIntPalindromTest(unittest.TestCase):
    """docstring for IsIntPalindromTest"""
    def test_is_int_palindrom(self):
        self.assertEqual(True, solution.is_int_palindrom(1))
        self.assertEqual(False, solution.is_int_palindrom(42))
        self.assertEqual(True, solution.is_int_palindrom(100001))

if __name__ == '__main__':
    unittest.main()