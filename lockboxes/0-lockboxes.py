#!/usr/bin/python3
"""Locked Boxes Task"""


def canUnlockAll(boxes):
    """Module to unlock boxes"""

    visited = set([0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)
