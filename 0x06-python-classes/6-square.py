#!/usr/bin/python3
"""Make Square"""


class Square:
    """Represent Square """

    def __init__(self, size=0, position=(0, 0)):
        """private square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size return"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """inirializes square"""
        try:
            ("{:d}".format(value))
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except Exception:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public square"""
        return(self.__size * self.__size)

    def my_print(self):
        """print square"""
        size = self.__size

        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end="")
                print()
