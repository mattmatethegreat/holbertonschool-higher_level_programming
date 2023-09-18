#!/usr/bin/python3
""" defines square class"""


# rectangle.py

class Rectangle:
    """A class representing a rectangle.

    Attributes:
        number_of_instances (int): The number of instances of the Rectangle class.
        print_symbol (str): The symbol used for printing the rectangle.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return str(self.print_symbol) * self.__width + '\n' + (str(self.print_symbol) * self.__width + '\n') * (self.__height - 1)

    def __repr__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Destructor for the Rectangle class.

        Prints a message when an instance of the Rectangle class is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
