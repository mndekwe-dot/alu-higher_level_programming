#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one integer per line.

    Args:
        my_list (list): The list of integers to print. Defaults to [].

    The function adheres to constraints:
    - Does not import any module.
    - Assumes the list only contains integers.
    - Uses str.format() to print each integer on a new line.
    """
    # Iterate through each element (which we assume is an integer) in the list
    for number in my_list:
        # Use str.format() with the ':d' format specifier for integers.
        # print() automatically handles the newline character.
        print("{:d}".format(number))

if __name__ == '__main__':
    # Example usage based on the provided main file
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)

