#!/usr/bin/python3
"""Module that defines the function update_dictionary."""


def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value (any): The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
