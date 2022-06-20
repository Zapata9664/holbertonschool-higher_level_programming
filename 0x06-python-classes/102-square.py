#!/usr/bin/python3
"""define a square"""


class Square:
    """ Make a square """

    def __init__(self, size=0):
        """ Initialize a square"""
        self.__size = size

    def __eq__(self, other):
        """Compare equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """compra not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare less """
        return self.area() < other.area()

    def __le__(self, other):
        """compare less or equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """compare >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Compare > or equal"""
        return (self.area() >= other.area())

    def area(self):
        """public square"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """return size square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size square attribute"""
        try:
            ("{:d}".format(value))
            self.__size = value
        except Exception:
            raise TypeError("size must be an integer")
