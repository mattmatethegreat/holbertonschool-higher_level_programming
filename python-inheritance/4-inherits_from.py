#!/usr/bin/python
""" defines path """


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
    return any(a_class in cls.__bases__ for cls in type(obj).__mro__[1:])
