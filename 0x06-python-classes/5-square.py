#!/usr/bin/python3
""""""

class Square:
    """ """
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        try:
            ("{:d}".format(value))
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except:
            raise TypeError("size must be an integer")

    def area(self):
        return(self.__size * self.__size)
    
    def my_print(self):
        size = self.__size

        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end="")
                print()
