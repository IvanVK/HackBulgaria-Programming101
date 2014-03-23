import unittest
import solution


class SumOfMinAndMaxTest(unittest.TestCase):
    """docstring for SumOfMinAndMaxTest"""
    def test_sum_of_min_and_max(self):
        self.assertEqual(10, solution.sum_of_min_and_max([1,2,3,4,5,6,8,9]))
        self.assertEqual(90, solution.sum_of_min_and_max([-10,5,10,100]))
        self.assertEqual(2, solution.sum_of_min_and_max([1]))

if __name__ == '__main__':
    unittest.main()