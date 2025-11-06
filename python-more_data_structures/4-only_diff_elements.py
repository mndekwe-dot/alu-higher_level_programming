#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return elements present in only one set (symmetric difference).

    Args:
        set_1: First set
        set_2: Second set

    Returns:
        A new set containing elements in either set but not in both
    """
    return set_1 ^ set_2
