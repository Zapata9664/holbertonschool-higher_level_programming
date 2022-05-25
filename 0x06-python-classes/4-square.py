#!/usr/bin/python3
""""""


class Square:
    """ """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return(self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        try:
            ("{:d}".format(value))
            self.__size = value
        except:
            raise TypeError("size must be an integer")
