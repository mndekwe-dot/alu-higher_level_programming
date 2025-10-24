def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples element-wise.
    
    Args:
        tuple_a: First tuple (default: empty tuple)
        tuple_b: Second tuple (default: empty tuple)
    
    Returns:
        A tuple with 2 integers representing the sum of corresponding elements
    """
    # Get first elements (use 0 if not present)
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >=
