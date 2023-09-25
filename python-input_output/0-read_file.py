#!/user/bin/python3
""" shebang """


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Parameters:
    filename (str): The name of the file to read. Default is an empty string.

    Returns:
    None
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
