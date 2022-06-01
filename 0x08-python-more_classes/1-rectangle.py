#!/usr/bin/python3
"""Module for import 1-rectangle"""


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
        self.height = height
        self.width = width

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
