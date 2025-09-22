#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


@abstractmethod
class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius=0):
        Circle.radius = radius

    def area(self):
        return (math.pi) * Circle.radius * Circle.radius

    def perimeter(self):
        return (math.pi) * Circle.radius * 2


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        Rectangle.width = width
        Rectangle.height = height

    def area(self):
        return Rectangle.width * Rectangle.height

    def perimeter(self):
        return (Rectangle.width + Rectangle.height) * 2


def shape_info(self):
    area = self.area()
    perimeter = self.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
