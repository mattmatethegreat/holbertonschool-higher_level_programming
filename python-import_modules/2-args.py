#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

output = ""

if num_arguments == 0:
    output += "0 arguments.\n"
elif num_arguments == 1:
    output += "1 argument:\n"
else:
    output += f"{num_arguments} arguments:\n"

for i, argument in enumerate(arguments):
    output += f"{i + 1}: {argument}\n"

print(output)
