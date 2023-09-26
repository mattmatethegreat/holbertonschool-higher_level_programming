#!/usr/bin/python3
""" shebang """

class BaseGeometry:
    """A base class for geometry calculations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that the given value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

