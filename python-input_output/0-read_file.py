#!/usr/bin/python3
"""Module that defines a function to read a
file and print its contents to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
