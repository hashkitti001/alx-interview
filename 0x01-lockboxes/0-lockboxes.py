#!/usr/bin/python3

from collections import deque
'''A module for working with lockboxes'''


def canUnlockAll(boxes):
    '''
    Checks if all boxes in the set of the boxes
    can be unlocked
    boxes -> List(int)
    '''
    n = len(boxes)
    keySet = set({0})
    openedBoxes = set([0])
    queue = [0]
    while queue:
        currentBox = queue.pop(0)

        for newKey in boxes[currentBox]:
            if newKey not in openedBoxes and newKey < n:
                queue.append(newKey)
                openedBoxes.add(newKey)

    return len(openedBoxes) == n

