#!/usr/bin/python3
"""Module for rotate 2D matrix submission."""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
