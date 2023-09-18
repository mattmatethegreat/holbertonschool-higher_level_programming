#!/user/bin/python3
"""Defines the rectangle class"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
    - width: The width of the rectangle.
    - height: The height of the rectangle.
    - print_symbol: The symbol used to represent the rectangle when printed.

    Methods:
    - __init__(self, width=0, height=0): Initializes a new instance of class.
    - area(self): Calculates the area of the rectangle.
    - perimeter(self): Calculates the perimeter of the rectangle.
    - __str__(self): Returns a string representation of the rectangle.
    - __repr__(self): Returns a string representation that creates rectangle.
    - __del__(self): Performs cleanup when the rectangle is deleted.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width: The width of the rectangle (default: 0).
        - height: The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        - The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - A string representation of the rectangle.
        """
        return f'Rectangle(width={self.width}, height={self.height})'

    def __repr__(self):
        """
        Returns a string representation used to recreate the rectangle.

        Returns:
        - A string representation used to recreate the rectangle.
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """
        Performs cleanup when the rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
