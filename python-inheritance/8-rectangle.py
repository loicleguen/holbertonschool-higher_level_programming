#!/usr/bin/python3
"""Module Rectangle that defines a rectangle
by: (based on 7-base_geometry.py)"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
