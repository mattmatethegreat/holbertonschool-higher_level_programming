#!/usr/bin/python3

def print_numbers():
    print("01", end="")
    for num in range(10, 100):
        if num % 10 != num // 10:
            print(", {:02d}".format(num), end="")
    print()

print_numbers()

