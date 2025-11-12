#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Check if object is instance of class that inherited from specified class.
    
    Args:
        obj: The object to check
        a_class: The class to check inheritance from
        
    Returns:
        True if obj is an instance of a class that inherited (directly or
        indirectly) from a_class, False otherwise.
        
    Note:
        Returns False if obj is an instance of a_class itself (not inherited).
        Only returns True if obj's class is a subclass of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
