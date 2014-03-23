import unittest
import solution


class BiggestDifferenceTest(unittest.TestCase):
    """docstring for BiggestDifferenceTest"""
    def test_empty_array(self):
        self.assertEqual(0, solution.biggest_difference(None))

    def test_empty_array(self):
        self.assertEqual(-1, solution.biggest_difference([1, 2]))

    def test_ordinary_array(self):
        self.assertEqual(-4, solution.biggest_difference([1,2,3,4,5]))

    def test_with_negative_integers(self):
        self.assertEqual(-9, solution.biggest_difference([-10, -9, -1]))

    def test_array_of_equals(self):
        self.assertEqual(0, solution.biggest_difference([1,1,1,1,1]))

        
if __name__ == '__main__':
    unittest.main()