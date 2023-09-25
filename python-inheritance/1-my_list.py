class MyList(list):
    """ Defines list class that inherits from the built-in list class."""

    def print_sorted(self):
        """
        Print in ascending order.

        Returns:
            None
        """
    print(sorted(self))
