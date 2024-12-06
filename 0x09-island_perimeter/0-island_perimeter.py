#!/usr/bin/python3
"""Module containing solution to the island perimeter problem."""


def island_perimeter(grid):
    """Solution to the island perimeter problem."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if (grid[r][c] == 1):
                perimeter += 4
                # Top adj cell
                if (r > 0 and grid[r - 1][c] == 1):
                    perimeter -= 1
                # Down adj cell
                if (r < rows - 1 and grid[r + 1][c]):
                    perimeter -= 1
                # Left adj cell
                if (c > 0 and grid[r][c - 1] == 1):
                    perimeter -= 1
                # Right adj cell
                if (c < cols - 1 and grid[r][c + 1] == 1):
                    perimeter -= 1

    return perimeter
