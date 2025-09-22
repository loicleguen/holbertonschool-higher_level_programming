#!/usr/bin/env python3
"""Defines an abstract base class Shape with area and perimeter methods, and
concrete Circle and Rectangle classes implementing these methods.
Also includes a function to display shape information."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi) * self.radius * self.radius

    def perimeter(self):
        return (math.pi) * self.radius * 2


class Rectangle(Shape):
    """Concrete class representing a rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
