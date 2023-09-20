#!/usr/bin/python3
import argparse

def add_arguments():
    parser = argparse.ArgumentParser(description='Addition of arguments')
    parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='an integer to be added')
    return parser.parse_args()

def main():
    args = add_arguments()
    result = sum(args.numbers)
    print(result)

if __name__ == '__main__':
    main()
