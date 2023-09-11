#!/usr/bin/python3

def print_list_integer(*args):
    my_list = list(args)

    for num in my_list:
        print(num)

print_list_integer(1, 2, 3, 4, 5)
