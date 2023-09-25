#!/usr/bin/python3
""" Shebang """


import sys
import json


def save_to_json_file(data, filename):
    """
    Save data to a JSON file.

    Parameters:
    - data: The data to be saved.
    - filename: The name of the file to save the data to.
    """
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

json_string = json.dumps(my_list)

save_to_json_file(json_string, 'add_item.json')
