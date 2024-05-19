#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """Calculate the minimum number of operations needed to reach n H characters in a text file."""
    if n <= 1:
        return 0
    i = 2
    result = 0
    while i <= n:
        if n % i == 0:
            result += i
            n /= i
        else:
            i += 1
    return result

