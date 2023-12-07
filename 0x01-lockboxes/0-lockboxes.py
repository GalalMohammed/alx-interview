#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines canUnlockAll function.

Example:
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

"""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (list): list of lists.

    Returns:
        True if all boxes can be opened, else return False.

    """
    locked = [1 for box in boxes[1:]]
    locked.insert(0, 0)
    keys = boxes[0].copy()
    while len(keys) > 0:
        key = keys.pop()
        if locked[key]:
            locked[key] = 0
            for newKey in boxes[key]:
                if locked[newKey]:
                    keys.append(newKey)
    return locked.count(1) == 0
