#!/usr/bin/python3
"""Module square"""

import json
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Rectangle instance """

        st = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}")
        return (st)

    @property
    def size(self):
        """Get atribute size"""

        return self.__width

    @size.setter
    def size(self, value):
        """atribute size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        assigns a key/value argument to attributes"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dic_s = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return (dic_s)
