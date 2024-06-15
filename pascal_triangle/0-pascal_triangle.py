#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function to return a list of pascal triangle up to row n.
    Attributes:
        n(integer): Number of rows of pascal triangle.
    """
    if n <= 0:
        return []
    if n < 2:
        return [[1 for _ in range(n)]]
    else:
        two_sum = 0
        prev_pascals = pascal_triangle(n-1)
        new_pascal = [1]
        for i in range(len(prev_pascals[-1][:-1])):
            two_sum = prev_pascals[-1][i] + prev_pascals[-1][i+1]
            new_pascal.append(two_sum)
            two_sum = 0
        new_pascal.append(1)
        prev_pascals.append(new_pascal)
        return prev_pascals
