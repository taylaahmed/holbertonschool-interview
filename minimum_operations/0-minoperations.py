#!/usr/bin/python3
"""Minimum Operations Question"""


def minOperations(n):
    """finding the minimum operation to get n"""

    cache = {}

    def helper(count, paste):
        if count == n:
            return 0
        if count > n:
            return 1000
        if (count, paste) in cache:
            return cache[(count, paste)]

        # paste
        res1 = 1 + helper(count + paste, paste)
        # copy & paste
        res2 = 2 + helper(count + count, count)
        cache[(count, paste)] = min(res1, res2)

        return cache[(count, paste)]

    if n == 1:
        return 0

    return 1 + helper(1, 1)
