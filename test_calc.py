# Jan 19 2020

# The naming convention to write test with test_ underscore
# import calc -> import calc.py from the same direcotory!
# 🧠 import unittest

import unittest
import calc

# 🧠 inherit from unittest.TestCase
# 🧠 self.assertRaises(ValueError, calc.divide, 10, 0)


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(calc.divide(1, 2), .5)

        # Apply context manager - call the function normally like we normally would
        # with context manager:
        # module.func(x, y) like we normally would
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
