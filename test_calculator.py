import unittest
from calculator import calc_sum, calc_multiple, calc_subtract, calc_division, calc_absolute


class Test(unittest.TestCase):
    def test_calc_sum(self):
        self.assertEqual(calc_sum(1, 2), 3, "Should be 3")
        self.assertEqual(calc_sum(4, 5), 9, "Should be 9")

    def test_multiple(self):
        self.assertEqual(calc_multiple(3, 4), 12, "Should be 12")
        self.assertEqual(calc_multiple(5, 6), 30, "Should be 30")

    def test_calc_subtract(self):
        self.assertEqual(calc_subtract(1, 4), -3, "Should be -3")

    def test_calc_division(self):
        self.assertEqual(calc_division(500, 5), 100, "Should be 100")

    def test_calc_divide_by_zero(self):
        self.assertEqual(calc_division(500, 0), 0, "Should be 0")

    def test_calc_absolute(self):
        self.assertEqual(calc_absolute(-500), 500, "Should be 500")
        self.assertEqual(calc_absolute(500), 500, "Should be 500")


if __name__ == '__main__':
    unittest.main()
