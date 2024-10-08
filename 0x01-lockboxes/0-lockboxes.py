#!/usr/bin/python3

'''A module for working with lockboxes'''

def canUnlockAll(boxes):

   '''
    Checks if all boxes in the set of the boxes can be unlocked
    boxes -> List(int)
   '''
    n = len(boxes)
    keySet = set(boxes[0])
    openedBoxes = 1
    for i in range(n):
        if i in keySet:
            openedBoxes += 1
        for j in range(len(boxes[i])):
            if boxes[i][j] not in keySet:
                keySet.add(boxes[i][j])
    return openedBoxes == n

crates =  [[1], [2], [3], [4], []]
print(canUnlockAll(crates))
