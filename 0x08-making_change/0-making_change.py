#!/usr/bin/python3
"""Module for Task 8: Making Change."""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the minimum number of coins needed to meet a given total.
    
    Args:
        coins (list): The values of the coin in your possession.
        total (int): The total amount to meet.
    Returns:
        int: The min number of coins needed to meet total or
        -1 if total can't be met.
    """
    if total <= 0:
        return 0
    # Reverse the list of coins
    coins.sort(reverse=True)

    count = 0
    # Go through them in descending order
    for coin in coins:
        if total <= 0:
            break

        count += total // coin
        total %= coin

    if total != 0:
        return -1
    return count
