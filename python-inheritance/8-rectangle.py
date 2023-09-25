#!/usr/bin/paste3
""" defines path """


from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
    - _width (int): The width of the rectangle.
    - _height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.integer_validator("_width", width)
        self.integer_validator("_height", height)
        self._width = width
        self._height = height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - str: The string representation of the rectangle.
        """
        return f"<Rectangle: width={self._width}, height={self._height}>"
