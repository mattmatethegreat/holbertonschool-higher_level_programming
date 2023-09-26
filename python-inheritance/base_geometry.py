#!/usr/bin/python3
""" shebang """


class BaseGeometry:
    """A base class for geometry operations.

    This class provides a foundation for implementing specific
    geometry operations. Subclasses can override the `area` method
    to calculate the area of a specific geometry.

    Attributes:
        None

    Methods:
        area: Calculate the area of the geometry (to be implemented by subclasses)
        integer_validator: Validate an integer value

    """

    def area(self):
        """Calculate the area of the geometry.

        This method should be implemented by subclasses.

        Arguments:
            self: The instance of the geometry object.

        Returns:
            None

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        This method validates that the given value is an integer and
        greater than 0.

        Arguments:
            name: The name of the value.
            value: The value to validate.

        Returns:
            None

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
