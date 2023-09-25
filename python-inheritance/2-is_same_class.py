#!/usr/bin/python3
""" defines the execution. """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is instance: otherwise false
    """
    return type(obj) is a_class
