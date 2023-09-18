#!/usr/bin/python3

""" defines a square class """


class Square:
    """
    A class that represents a square.

    Attributes:
    _size (int): The size of the square.

    Methods:
    size: Getter and setter for the size attribute.
    area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
        size (int): The size of the square. Default is 0.
        """
        self._size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        value (int): The size of the square.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self._size * self._size
