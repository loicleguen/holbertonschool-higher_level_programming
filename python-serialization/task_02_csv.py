#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save it as data.json.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)

        return True
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
