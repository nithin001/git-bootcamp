import unittest
from calculator import calc_sum


class Test(unittest.TestCase):
    def test_calc_sum(self):
        self.assertEqual(calc_sum(1, 2), 3, "Should be 3")


if __name__ == '__main__':
    unittest.main()
