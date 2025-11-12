#!/usr/bin/python3
"""Module that defines is_same_class function."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class.
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
        
    Note:
        This function returns True only if obj is a direct instance of a_class,
        not if obj is an instance of a subclass of a_class.
    """
    return type(obj) is a_class
