import unittest
import solution


class SlopeStyleScoreTest(unittest.TestCase):
    """docstring for SlopeStyleScoreTest"""
    def test_slope_style_score(self):
        self.assertEqual('94.67',solution.slope_style_score([94, 95, 95, 95, 90]))
        

if __name__ == '__main__':
    unittest.main()