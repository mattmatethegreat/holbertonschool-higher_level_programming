#!/usr/bin/python3
"""shebang """


def write_file(filename="", text=""):
    """
    Writes the given text to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. If the file doesn't exist, it will be created.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        None

    Examples:
        >>> write_file("my_file.txt", "Hello, World!")
        13
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
