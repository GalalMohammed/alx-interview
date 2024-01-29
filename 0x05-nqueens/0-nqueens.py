#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module solves the N queens problem.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
board = [0] + [-1] * (n - 1)
solutions = []
i = 1
while i >= 0:
    col = board[i] + 1
    if col == n:
        board[i] = -1
        i -= 1
        continue
    while col < n:
        valid = False
        if col not in board:
            valid = True
            for k, j in enumerate(range(i - 1, -1, -1)):
                if board[j] == col - k - 1 or board[j] == col + k + 1:
                    valid = False
                    break
        if valid:
            board[i] = col
            if i == n - 1 and board not in solutions:
                solutions.append(board.copy())
            elif i < n - 1:
                break
        col += 1
        if col == n:
            board[i] = -1
            i -= 2
    i += 1
for solution in solutions:
    print([ [i, j] for i, j in enumerate(solution)])
