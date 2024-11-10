#!/usr/bin/python3
"""Module containing a solution for the N-Queens puzzle"""
import sys

solutions = []

def input_helper():
    """Gets input for the N-Queens function."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos1, pos2):
    """Checks if two queens are attacking each other."""
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])

def build_solution(n, row=0, group=[]):
    """Builds a solution for the N-Queens problem using backtracking."""
    if row == n:
        solutions.append(group.copy())
        return

    for col in range(n):
        queen_pos = (row, col)
        if all(not is_attacking(queen_pos, q) for q in group):
            group.append(queen_pos)
            build_solution(n, row + 1, group)
            group.pop()  # Backtrack

def print_solutions():
    """Prints the solutions in the required format."""
    for solution in solutions:
        print([[r, c] for r, c in solution])

n = input_helper()
build_solution(n)
print_solutions()
