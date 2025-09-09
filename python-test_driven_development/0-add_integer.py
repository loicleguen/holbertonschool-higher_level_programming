#!/usr/bin/python3
"""
Module compiled with Python3
"""
def add_integer(a, b=98):
    """
    Method that adds two integers
    Floats are accepted but cast to integers

    :param a: int or float - first number to add
    :param b: int or float - second number to add

    :raises TypeError: if a or b are anything other than int or float

    :Returns: int - the sum
    """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
