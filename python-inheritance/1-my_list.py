#!/usr/bin/python3
"""Module that defines MyList class."""


class MyList(list):
    """A class that inherits from list with additional functionality.
    
    This class extends the built-in list class by adding a method
    to print the list in sorted order without modifying the original.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order.
        
        This method prints a sorted version of the list without
        modifying the original list.
        """
        print(sorted(self))
