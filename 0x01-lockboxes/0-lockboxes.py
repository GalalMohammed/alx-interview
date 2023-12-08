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
        if key < len(locked) and locked[key]:
            locked[key] = 0
            for new_key in boxes[key]:
                if new_key < len(locked) and locked[new_key]:
                    keys.append(new_key)
    return locked.count(1) == 0
