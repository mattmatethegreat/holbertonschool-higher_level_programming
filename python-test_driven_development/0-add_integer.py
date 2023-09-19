#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function adds two integers.
    """

    """
    Parameters:
    a (int): The first integer.
    b (int): The second integer. Default is 98.
    """

    """
    Returns:
    int: The sum of the two integers.

    Raises:
    TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(str(a).strip())
    b = int(str(b).strip())
    return a + b
