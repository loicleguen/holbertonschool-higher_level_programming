#!/usr/bin/python3
"""Defines a function that checks if an object
is an instance of a specified class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or its subclasses.

    Args:
        obj (any type): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of
        a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
