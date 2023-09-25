#!/usr/bin/python3
"""defines path """


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class. False otherwise.
    """
    cls = type(obj)
    if cls == a_class:
        return False
    return issubclass(cls, a_class)
