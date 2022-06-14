#!/usr/bin/python3
""" Module Rectangle """

import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @property
    def height(self):
        """"""
        return self.__height

    @property
    def x(self):
        """"""
        return self.__x

    @property
    def y(self):
        """"""
        return self.__y

    @width.setter
    def width(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    

    @height.setter
    def height(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """"""
        return(self.__width * self.__height)

    def display(self):
        """"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()
    
    def __str__(self):
        """"""
        st = (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
        return (st)

    def update(self, *args, **kwargs):
        """"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) == 2:
                self.width = args[1]
            if len(args) == 3:
                self.height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
