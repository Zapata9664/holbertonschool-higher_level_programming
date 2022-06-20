#!/usr/bin/python3
"""Module for magic calculation"""


def magic_calculation(a, b):
    """does exactly the same of a Python bytecode for Holberton"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)
