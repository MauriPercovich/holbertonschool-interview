#!/usr/bin/python3

"""
this function will unlock boxes
"""


def canUnlockAll(boxes):

    length = len(boxes) - 1
    unlocked = []
    for keys in boxes[0]:
        if keys not in unlocked and keys <= length:
            unlocked.append(keys)
    for x in range(length + 1):
        if x in unlocked:
            for y in boxes[x]:
                if y not in unlocked and y <= length:
                    unlocked.append(y)
    if (len(unlocked) == length) or\
            (length == 0 and len(unlocked) == 1):
        return True
    else:
        return False
