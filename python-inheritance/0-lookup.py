#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    Args:
        obj: The object to look up.

    Returns:
        A list of attribute and method names as strings.
    """
    return dir(obj)
