#!/usr/bin/python3
"""Module Rectangle that defines a rectangle
by: (based on 7-base_geometry.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns the area of the square"""
        return self.__size * self.__size
