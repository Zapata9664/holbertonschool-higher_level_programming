#!/usr/bin/python3
"""
Module by a function for add two numbers

"""


def add_integer(a, b=98):
    """
    Function that adds two integer and/or float numbers
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int and type(a) is not float or a is None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or a is None:
        raise TypeError("b must be an integer")

    else:
        return a + b
