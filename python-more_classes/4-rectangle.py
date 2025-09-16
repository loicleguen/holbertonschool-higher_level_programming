#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_list = []
        for i in range(self.__height):
            rectangle_list.append("#" * self.__width)
        return "\n".join(rectangle_list)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
