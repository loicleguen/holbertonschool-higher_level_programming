#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
