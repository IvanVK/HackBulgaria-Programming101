import unittest
import solution


class CountVowelsTest(unittest.TestCase):
    """docstring for CountVowelsTest"""
    def test_count_vowels(self):
        self.assertEqual(3, solution.count_vowels('Programing'))
        self.assertEqual(8, solution.count_vowels('Theistareykjarbunga'))

if __name__ == '__main__':
    unittest.main()