#!/usr/bin/python3

"""Defines the division function."""


def matrix_divided(matrix, div):
    """Divide all elements.

    Args:
        matrix (list): a list of lists of ints/floats.
        div (int/float): divisor.
    Raises:
        TypeError: matrix contains non-numbers.
        TypeError: matrix contains different sized rows.
        TypeError: div is not an int/float.
        ZeroDivisionError: div is 0.
