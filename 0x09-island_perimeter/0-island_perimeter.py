#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines function island_perimeter.
"""


def island_perimeter(grid):
    """Get the perimeter of the island.
    """
    perimeter = 0
    for i, row in enumerate(grid):
        for j, k in enumerate(row):
            if k:
                if j == 0 or row[j - 1] == 0:
                    perimeter += 1
                if j == len(row) - 1 or row[j + 1] == 0:
                    perimeter += 1
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
