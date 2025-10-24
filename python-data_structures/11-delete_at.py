def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    
    Args:
        my_list: The list to modify (default: empty list)
        idx: The index position to delete (default: 0)
    
    Returns:
        The modified list, or the original list if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    del my_list[idx]
    return my_list
