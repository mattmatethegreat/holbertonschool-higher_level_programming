#!/usr/bin/python3

class Rectangle:
    """
    A class representing a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += "#" * self._width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
            str: The string representation of the rectangle object.
        """
        return f"<Rectangle width={self._width}, height={self._height}>"
