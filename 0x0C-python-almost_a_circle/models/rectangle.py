#!/usr/bin/python3
""""""

import json
from models.base import Base

class Rectangle(Base):
    """"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """"""
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
