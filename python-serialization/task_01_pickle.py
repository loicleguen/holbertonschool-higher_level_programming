#!/usr/bin/env python3
"""
This module defines a CustomObject class with methods
to serialize and deserialize its instances using the
pickle module. It includes error handling for file operations
and serialization/deserialization processes.
"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize the CustomObject with name,
        age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
