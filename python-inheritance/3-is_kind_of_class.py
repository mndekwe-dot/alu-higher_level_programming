#!/usr/bin/python3
"""Module that defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or inherited from, specified class.
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        True if obj is an instance of a_class or a class that inherited
        from a_class, False otherwise.
        
    Note:
        This function returns True for both direct instances and instances
        of subclasses, unlike is_same_class which only checks exact match.
    """
    return isinstance(obj, a_class)
