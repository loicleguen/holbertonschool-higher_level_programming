#!/usr/bin/python3
"""Defines a function that converts an object's attributes to a dictionary."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (any): The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__.copy()
