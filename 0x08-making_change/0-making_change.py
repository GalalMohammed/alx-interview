#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines makeChange function.
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet total.
    """
    if total <= 0:
        return 0
    coins.sort()
    coins_number = 0
    for coin in coins[-1::-1]:
        if total >= coin:
            coins_number += total // coin
            total -= total // coin * coin
        if total == 0:
            return coins_number
    return -1
