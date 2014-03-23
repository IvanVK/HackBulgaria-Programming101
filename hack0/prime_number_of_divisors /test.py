import unittest
import solution


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    """docstring for PrimeNumberOfDivisorsTest"""
    def test_prime_number_of_divisors(self):
        self.assertEqual(True, solution.prime_number_of_divisors(7))
        self.assertEqual(False, solution.prime_number_of_divisors(8))
        self.assertEqual(True, solution.prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()