#!/usr/bin/python3
import dis
import sys

def print_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()
        dis.dis(code)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_names()
