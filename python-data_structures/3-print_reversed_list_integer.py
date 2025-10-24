def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order.
    
    Args:
        my_list: The list of integers to print (default: empty list)
    """
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
