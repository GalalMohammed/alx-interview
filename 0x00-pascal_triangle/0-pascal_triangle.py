#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines pascal_triangle function.

Example:
    print(pascal_triangle(5))

"""


def pascal_triangle(n):
    """creates a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): number of rows.

    Retunrs:
        list of lists.

    """
    pascals_triangle = []
    for i in range(n):
        if i == 0:
            pascals_triangle.append([1])
        else:
            row = [1]
            for x in range(i - 1):
                row.append(pascals_triangle[-1][x]
                           + pascals_triangle[-1][x + 1])
            row.append(1)
            pascals_triangle.append(row)
    return pascals_triangle
