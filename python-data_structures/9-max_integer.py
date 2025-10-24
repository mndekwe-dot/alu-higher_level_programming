def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.
    
    Args:
        my_list: The list of integers to search (default: empty list)
    
    Returns:
        The maximum integer in the list, or None if the list is empty
    """
    if not my_list:
        return None
    
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    
    return max_value
