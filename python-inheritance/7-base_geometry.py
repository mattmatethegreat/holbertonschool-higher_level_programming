#!/usr/bin/python3
""" Defines path """


class BaseGeometry:
    """
    A base class for geometry calculations.

    Public instance methods:
    - area(self): Raises an Exception with the message
'area() is not implemented'
    - integer_validator(self, name, value): Validates value as integer.

    Attributes:
    - name: A string representing the name of the value being validated
    - value: The value to be validated
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the base class.
        Subclasses should override this method to provide
        the specific implementation for calculating the area.

        Raises:
            Exception: Raises an Exception 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
