#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines minOperations function.

Example:
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

"""


def minOperations(n):
    """Calculate the fewest number of operations needed,
    to result in exactly n H characters in the file.

    Args:
        n (int): number of characters.

    Returns:
        int.

    """
    c = 1
    copied = 0
    op = 0
    while c < n:
        if n % c == 0:
            copied = c
            op += 1
        c += copied
        op += 1
    return op
