import unittest
from calculator import calc_sum, calc_multiple


class Test(unittest.TestCase):
    def test_calc_sum(self):
        self.assertEqual(calc_sum(1, 2), 3, "Should be 3")

    def test_multiple(self):
        self.assertEqual(calc_multiple(3, 4), 12, "Should be 12")
        self.assertEqual(calc_multiple(5, 6), 30, "Should be 30")


if __name__ == '__main__':
    unittest.main()
