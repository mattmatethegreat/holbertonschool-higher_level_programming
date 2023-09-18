#!/usr/bin/python3
""" defines rectangle class"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A representation of rectangle using #.
        """
        # Implementation...

    def __repr__(self):
        """
        Returns a string that can be used to recreate a new instance.

        Returns:
            str: A string representation of the rectangle.
        """
        # Implementation...

    def __del__(self):
        """
        Deletes an instance of the rectangle.

        Prints the message "Bye rectangle...".
        """
        print("Bye rectangle...")
