#!/usr/bin/python3
"""Module magic_calculation"""


def magic_calculation(a, b, c):
    """xactly the same as bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
