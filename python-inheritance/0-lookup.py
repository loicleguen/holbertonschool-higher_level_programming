#!/usr/bin/python3
"""
Module that defines a function to list
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any type): The object to inspect.

    Returns:
        list: List of attribute and method names as strings.
    """
    return dir(obj)
