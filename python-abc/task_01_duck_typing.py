#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return (math.pi) * self.radius * self.radius

    def perimeter(self):
        return (math.pi) * self.radius * 2


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(self):
    area = self.area()
    perimeter = self.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
