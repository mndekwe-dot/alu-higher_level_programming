def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index without modifying the original.
    
    Args:
        my_list: The original list
        idx: The index position to replace
        element: The new element to insert
    
    Returns:
        A new list with the element replaced, or a copy of the original if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
