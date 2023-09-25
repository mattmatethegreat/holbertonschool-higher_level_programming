#!/usr/bin/python3
""" Shebang """


import json

def from_json_string(my_str):
    """
    Deserialize a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
