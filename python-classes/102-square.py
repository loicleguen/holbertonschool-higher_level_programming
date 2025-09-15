#!/usr/bin/python3
"""
Module defining a Square with size and area
"""


class Square:
    """Class that defines a square"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
