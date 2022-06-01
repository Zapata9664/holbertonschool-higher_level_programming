#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle:
    """
    clase rectangulo con base y altura

    """

    def __init__(self, width=0, height=0):
        """
        Instancia de rectangulo 
        width - altura del rectangulo
        height - base del rectangulo

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        obtiene la altura del rectangulo
        """
        return self.___width

    @width.setter
    def width(self, value):
        """
        establecer ancho del rectangulo
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Obtiene la base del rectangulo
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Establecer la base del rectangulo
        """
        if value is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        retornar el area de un rectangulo
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        retornar el perimetro de una rectangulo
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
