#!/usr/bin/python3
"""Defines a function that checks if an object
is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj (any type): The object to check.
        a_class (type): The class to compare against.
    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
