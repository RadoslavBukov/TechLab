'''
Напишете unit test, който тества функцията за изчисление bisection. Преценете сами какви тестове трябва да съдържа.
'''
import unittest
import math

from task1 import bisection, f, g, InvalidIntervalError, NonNumericInputError


class TestBisectionMethod(unittest.TestCase):

    def test_bisection_f(self):
        # Test the function f(x) = x^3 + 3*x - 5
        root = bisection(1, 2, f)
        expected_root = 1.154296875
        self.assertAlmostEqual(root, expected_root)

    def test_bisection_g(self):
        # Test the function g(x) = exp(x) - 2*x - 2
        root = bisection(0, 2, g)
        expected_root = 1.677734375
        self.assertAlmostEqual(root, expected_root)

    def test_invalid_interval_same_sign(self):
        # Test invalid interval where f(a) and f(b) have the same sign
        with self.assertRaises(InvalidIntervalError):
            bisection(1, 1, f)

    def test_invalid_input_non_numeric(self):
        # Test invalid input where a or b is not a number
        with self.assertRaises(NonNumericInputError):
            root = bisection("a", "b", f)

    def test_correct_interval_negative_to_positive(self):
        # Test an interval where the function changes from negative to positive
        def h(x):
            return x ** 2 - 4  # Root at x = -2 and x = 2

        root = bisection(1, 3, h)
        expected_root = 2.0
        self.assertAlmostEqual(root, expected_root)

    def test_correct_interval_positive_to_negative(self):
        # Test an interval where the function changes from positive to negative
        def h(x):
            return x ** 2 - 4  # Root at x = -2 and x = 2

        root = bisection(-3, -1, h)
        expected_root = -2.0
        self.assertAlmostEqual(root, expected_root)


if __name__ == '__main__':
    unittest.main()


