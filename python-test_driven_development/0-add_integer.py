#!/usr/bin/python3
"""
This module provides a function to add two numbers.
It ensures that inputs are integers or floats.
Floats are cast to integers before addition.
Errors are raised if inputs are not valid types.
Intended for simple math operations.
"""


def add_integer(a, b=98):
    """
    Adds two integers (or floats casted to integers).

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
