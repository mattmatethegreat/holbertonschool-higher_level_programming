#!/usr/bin/python3
""" Shebang """


def class_to_json(obj):
    """
    Converts an instance of a Class to a dictionary description with a simple data structure for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representing the serialized attributes of the object.

    Note:
        This function only includes attributes that are of type list, dict, str, int, bool, or None.

    Example:
        >>> m = MyClass("John")
        >>> m.number = 89
        >>> mj = class_to_json(m)
        >>> print(mj)
        {'name': 'John', 'number': 89}
    """
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool, type(None))):
            json_dict[attr] = value
    return json_dict
