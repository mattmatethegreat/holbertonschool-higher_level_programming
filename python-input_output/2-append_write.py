#!/usr/bin/python3
""" shebang """


def append_write(filename="", text=""):
    """
    Appends text at end of file (UTF8) returns the number of characters added.

    Args:
        filename (str): Name of the file to append to. If no file, create one.
        text (str): The text to append to the file

    Returns:
        int: The number of characters added to the file.

    Examples:
        >>> append_write("file_append.txt", "This School is so cool!\n")
        24
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
