#!/usr/bin/python3
"""
Module that defines the class MyList inheriting from list.
"""


class MyList(list):
    """
    A class that inherits from list and adds a method
    to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order,
        without modifying the original list.
        """
        print(sorted(self))
