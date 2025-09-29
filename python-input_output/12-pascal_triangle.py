#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n rows."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
        prev_row = row
    return triangle
