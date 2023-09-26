#!/usr/bin/python3
""" shebang """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    This class represents a square, which is a special case of a rectangle
    where all sides have equal length.
    """

    def __init__(self, size):
        """
        Initialize a Square object with the given size.

        Args:
            size (int): The length of each side of the square.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return super().area()

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square in the format "[Square] <size>/<size>".
        """
        return f"[Square] {self.__size}/{self.__size}"
