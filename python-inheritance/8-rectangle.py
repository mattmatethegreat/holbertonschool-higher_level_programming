#!/usr/bin/pyython3
"""shebang """


from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class and provides
    functionality specific to rectangles.

    Attributes:
        None

    Methods:
        __init__: Initialize the Rectangle object.
        __str__: Get a string representation of the Rectangle object.

    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle object.

        Arguments:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to 0.

        """
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def __str__(self):
        """
        Get a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object.

        """
        return f"<Rectangle width={self.__width}, height={self.__height}>"
