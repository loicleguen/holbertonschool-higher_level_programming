#!/usr/bin/python3
"""Defines an abstract base class Shape with area and perimeter methods, and
concrete Circle and Rectangle classes implementing these methods.
Also includes a function to display shape information."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return (math.pi) * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return (math.pi) * self.radius * 2


class Rectangle(Shape):
    """Concrete class representing a rectangle."""
    def __init__(self, width, height):
        """Initialize the rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return (self.width + self.height) * 2


def shape_info(shape):
    """Display information about a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
