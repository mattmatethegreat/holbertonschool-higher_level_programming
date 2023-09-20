#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        uppercase_char = chr(ord(char) - 32)
        result += uppercase_char
    print(result)

# Test the function
uppercase("best")
uppercase("Best School 98 Battery street")
