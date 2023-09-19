#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Print the name with the given first name and last name.

    :param first_name: The first name as a string.
    :param last_name: The last name as a string. Defaults to an empty string.
    :raises TypeError: If either `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

# Call the function with appropriate arguments
say_my_name("John", "Doe")
