#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines isWinner function.
"""


def isWinner(x, nums):
    """Determine who the winner of each game.
    """
    maria = 0
    ben = 0
    for i in range(x):
        primes = 0
        for j in list(range(nums[i] + 1)):
            if j > 1:
                prime = True
            else:
                continue
            for k in range(2, j):
                if j % k == 0:
                    prime = False
                    break
            if prime:
                primes += 1
        if primes % 2:
            maria += 1
        else:
            ben += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
