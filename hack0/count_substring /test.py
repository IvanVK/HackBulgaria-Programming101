import unittest
import solution


class CountSubstringsTest(unittest.TestCase):
    """docstring for CountSubstringsTest"""
    def test_count_substrings(self):
        self.assertEqual(2, solution.count_substrings("This is a test string", "is"))
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))

if __name__ == '__main__':
    unittest.main()