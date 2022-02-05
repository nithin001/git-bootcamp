import unittest
from calculator import calc_sum, calc_multiple, calc_subtract


class Test(unittest.TestCase):
    def test_calc_sum(self):
        self.assertEqual(calc_sum(1, 2), 3, "Should be 3")

    def test_multiple(self):
        self.assertEqual(calc_multiple(3, 4), 12, "Should be 12")
        self.assertEqual(calc_multiple(5, 6), 30, "Should be 30")

    def test_calc_subtract(self):
        self.assertEqual(calc_subtract(1, 4), -3, "Should be -3")


if __name__ == '__main__':
    unittest.main()
