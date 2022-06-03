#!/usr/bin/python3
"""
Module by a function for add two numbers

"""


def add_integer(a, b=98):
    """
    Function that adds two integer and/or float numbers
    """
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        c = a + b
        if type(c) is float:
            c = int(c)
        return c
