#!/usr/bin/python3
"""shebang."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize rectangle.

        Args:
            width of the new Rectangle.
            height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
