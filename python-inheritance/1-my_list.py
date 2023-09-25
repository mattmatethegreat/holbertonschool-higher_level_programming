class MyList(list):
    """ Custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """
        Print in ascending order.

        Returns:
            None
        """


        sorted_list = sorted(self)
        print(sorted_list)
