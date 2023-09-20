#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ""
    for char in string:
        uppercase_char = char.upper()
        uppercase_string += uppercase_char
    print(uppercase_string)

uppercase("best")
uppercase("Best School 98 Battery street")
