#!usr/bin/python3
""" defines implementation """


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of, or if the object is an
    instance of a class that inherited from specified class. False otherwise.
    """
    return type(obj) == a_class or isinstance(obj, a_class)
