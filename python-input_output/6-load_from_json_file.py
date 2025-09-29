#!/usr/bin/python3
"""Defines a function that creates an Object from a "JSON file"."""
import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
