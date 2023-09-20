#!/usr/bin/python3
def print_last_digit(number):
    last_digit_str = str(number)[-1]
    last_digit = int(last_digit_str)
    return last_digit

# Test the function
result = print_last_digit(8044)
print(result)
