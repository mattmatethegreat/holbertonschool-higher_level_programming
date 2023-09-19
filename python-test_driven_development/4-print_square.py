#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The length of the square sides.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is a negative integer.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print```
