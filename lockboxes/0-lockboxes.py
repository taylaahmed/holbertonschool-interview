#!/usr/bin/python3

def canUnlockAll(boxes):

    visited = set([0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)