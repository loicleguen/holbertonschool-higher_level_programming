#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_middle(self):
        self.assertEqual(max_integer([2, 8, 3, 5, 12, 7, 1]), 12)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -3, -100]), -3)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_equal_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.4, 2.2]), 3.4)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_empty_string_list(self):
        self.assertEqual(max_integer([""]), "")

if __name__ == "__main__":
    unittest.main()
