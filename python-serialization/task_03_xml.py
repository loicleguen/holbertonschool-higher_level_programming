#!/usr/bin/env python3
"""Module for serializing and deserializing
a dictionary to/from an XML file."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize a dictionary from an XML file."""
    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}
    for child in root:
        dict[child.tag] = child.text
    return dict
