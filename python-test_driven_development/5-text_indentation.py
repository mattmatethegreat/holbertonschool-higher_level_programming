#!/usr/bin/python3

def text_indentation(text):
    """
    Print the text with 2 new lines after each occurrence of '.', '?', and ':'.

    :param text: The input text.
    :raises TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")
