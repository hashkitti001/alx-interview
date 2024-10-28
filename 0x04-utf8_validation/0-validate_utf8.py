#!/usr/bin/env python3
"""Module for UTF-8 validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes: int = 0
    for item in data:
        # Check if it falls in the range of 0 - 255 (byte)
        if item < 0 or item > 255:
            return False
        # Get the first byte of a character
        mask_one = 1 << 7
        mask_two = 1 << 6

        if num_bytes == 0:
            mask = 1 << 7
            while mask & item:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (item & mask_one and not (item & mask_two)):
                return False

        num_bytes -= 1
    return num_bytes == 0
