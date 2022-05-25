#!/usr/bin/python3
"""Class Square """


def __init__(self, size=0):
    """ Class square
    param: size of a square
    """
    self.__size = size
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else
    self.__size = size
