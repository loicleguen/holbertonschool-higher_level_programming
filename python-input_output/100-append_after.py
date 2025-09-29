#!/usr/bin/python3
"""Module that appends a string after each line
containing a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string after each line containing
    a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after each line
        containing the search string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
