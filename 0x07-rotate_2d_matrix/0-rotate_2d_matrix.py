#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines rotate_2d_matrix function.
"""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise.
    """
    size = len(matrix)
    matrix_copy = [mtx.copy() for mtx in matrix]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = matrix_copy[size - 1 - j][i]
