#!/usr/bin/python33

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print('  '.join(map(str, row)))
