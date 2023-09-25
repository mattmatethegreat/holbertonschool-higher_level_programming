#!/usr/bin/python3
""" shebang """
import json


def load_from_json_file(filename):
    """
    Read JSON data from a file and deserialize it into a Python object.

    Args:
        filename (str): The name of the file to read the JSON data from.

    Returns:
        object: The Python object deserialized from the JSON data.
    """
    with open(filename, 'r') as infile:
        data = json.load(infile)

        return data
