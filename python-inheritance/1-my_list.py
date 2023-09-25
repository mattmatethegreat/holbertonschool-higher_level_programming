#!/usr/bin/python3
""" defines list class that inherits from built in list class"""


class MyList(list):
    """ implements sorted printing for built-in list class."""

    def print_sorted(self):
        """
        Print in ascending order.

        Returns:
            None
        """
    print(sorted(self))
