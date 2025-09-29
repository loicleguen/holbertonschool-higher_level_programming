#!/usr/bin/python3
"""Module for serializing and deserializing
Python objects to/from JSON files."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """Load and deserialize a Python object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
