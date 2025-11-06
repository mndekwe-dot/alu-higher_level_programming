#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key from a dictionary.

    Args:
        a_dictionary: Dictionary to delete from
        key: Key to delete (string)

    Returns:
        The same dictionary (modified in place)
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
