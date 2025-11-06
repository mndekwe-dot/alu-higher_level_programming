#!/usr/bin/python3
"""Module that defines a function to print a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary (dict): The dictionary to print.

    Returns:
        None
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
