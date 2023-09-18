#!/usr/bin/python3

"""defines rectangle class"""


class Rectangle:
    """ class representing a rectangle."""
    def __init__(self, width=0, height=0):

        """ initializes rectangle.

        arg:
            width: rectangles with, default is 0.
            height: rectangles height, default is 0.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ int: width of rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """ set rectangle width

        args:
            value: new value of width

        raises:
            typeError: if value isnt integer.
            VAlueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height

        args
            value: new height value

        raises:
            TypeError: value isnt integer.
            ValueError: value less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
