def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.
    
    Args:
        my_list: The list of integers to check (default: empty list)
    
    Returns:
        A new list with True or False for each element, indicating if it's divisible by 2
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
