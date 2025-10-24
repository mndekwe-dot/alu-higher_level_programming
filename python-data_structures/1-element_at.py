#!/usr/bin/python3
def element_at(my_list, idx):
    
    # 1. Check for negative index
    if idx < 0:
        return None

    # 2. Check if index is out of range (>= length of the list)
    if idx >= len(my_list):
        return None

    # If the index is valid, retrieve and return the element
    return my_list[idx]

if __name__ == '__main__':
    # Example usage based on the provided main file
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

    # Testing invalid indices
    idx_neg = -1
    print("Element at index {:d} is {}".format(idx_neg, element_at(my_list, idx_neg)))
    
    idx_out = 5
    print("Element at index {:d} is {}".format(idx_out, element_at(my_list, idx_out)))

