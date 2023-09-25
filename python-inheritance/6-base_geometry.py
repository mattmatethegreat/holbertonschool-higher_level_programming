#!/usr/bin/python3
"""definens path """


class BaseGeometry:
    """
    A base class for geometry calculations.

    Public instance method:
    - area(self): Raises exception with message 'area() is not implemented'
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the base class.
        Subclasses should override this method to provide
        the specific implementation for calculating the area.

        Raises:
            Exception: Always raises an Exception with
            the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
