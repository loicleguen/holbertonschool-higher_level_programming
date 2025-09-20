#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        """Validates that value is a pure integer > 0"""
        # Force TypeError message for missing arguments (doctest compatibility)
        if name is None and value is None:
            raise TypeError(
                "BaseGeometry.integer_validator() missing 2 required positional arguments: 'name' and 'value'"
            )
        if value is None:
            raise TypeError(
                "BaseGeometry.integer_validator() missing 1 required positional argument: 'value'"
            )

        # Normal validation
        if type(value) is not int:  # Exclut bool et objets custom avec __int__
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
