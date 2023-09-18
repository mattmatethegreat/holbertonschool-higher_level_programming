#!/usr/bin/python3

"""defines a square class."""

class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a square with the given size.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints a square pattern using the '#' character.
    """

    def __init__(self, size=0):
        """Initializes a square with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Prints a square pattern using the '#' character."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
