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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.size ** 2

    def my_print(self):
        print(self.__str__())

    def __str__(self):
        if self.size == 0:
            return ""
        square_string = ""
        square_string += "\n" * self.__position[1]
        for i in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            square_string += line + "\n"
        return square_string[:-1]
