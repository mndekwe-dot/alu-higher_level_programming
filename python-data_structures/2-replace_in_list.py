def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index.
    
    Args:
        my_list: The list to modify
        idx: The index position to replace
        element: The new element to insert
    
    Returns:
        The modified list, or the original list if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    my_list[idx] = element
    return my_list
