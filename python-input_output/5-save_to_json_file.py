#!/usr/bin/python3
""" Shebang """


import json


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to a JSON representation and write it to a file.

    Args:
        my_obj (object): The object to be serialized.
        filename (str): name of file to write the JSON representation to.
    """
    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)
