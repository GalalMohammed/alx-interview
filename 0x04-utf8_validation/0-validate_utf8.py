#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module is about UTF-8 Validation.

Example:
    print(validUTF8(data))

"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): list of characters.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.

    """
    i = 0
    while i < len(data):
        data_byte = data[i] & 255
        if (data_byte >> 6) & 3 == 2:
            return False
        while data_byte & 128 and data_byte & 64:
            i += 1
            if not i < len(data) or not ((data[i] >> 6) & 3) == 2:
                return False
            data_byte <<= 1
        i += 1
    return True
