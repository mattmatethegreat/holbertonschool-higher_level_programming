#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments == 0:
    print("0 arguments.")
elif num_arguments == 1:
    print("1 argument:")
else:
    print(f"{num_arguments} arguments:")

for i, argument in enumerate(arguments):
    print(f"{i + 1}: {argument}")
