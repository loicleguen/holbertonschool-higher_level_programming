#!/usr/bin/python3
"""Defines a Student class with a method to
convert its nameibutes to a dictionary."""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance."""
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
