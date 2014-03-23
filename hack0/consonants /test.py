import unittest
import solution


class CountConsonantsTest(unittest.TestCase):
    """docstring for CountConsonantsTest"""
    def test(self):
        self.assertEqual(4, solution.count_consonants('Python'))
        self.assertEqual(11, solution.count_consonants('Theistareykjarbunga'))
        self.assertEqual(7, solution.count_consonants('grrrrgh!'))
        self.assertEqual(44, solution.count_consonants('Github is the second best thing that happend to programmers, after the keyboard!'))

if __name__ == '__main__':
    unittest.main()