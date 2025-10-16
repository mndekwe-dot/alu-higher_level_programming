#!/usr/bin/python3
"""
A script that prints the result of the addition of all command-line arguments.
Arguments are assumed to be castable into integers and can handle large numbers.
"""
import sys


def add_args():
    """
    Calculates and prints the sum of all command-line arguments passed to the script.
    The script name (sys.argv[0]) is excluded from the calculation.
    """
    # sys.argv contains the list of command-line arguments.
    # We start from index 1 to skip the script name (sys.argv[0]).
    arguments = sys.argv[1:]
    total = 0

    # Iterate over the arguments and add them to the total
    for arg in arguments:
        # We assume all arguments can be safely cast into integers,
        # which Python handles with arbitrary precision (for large numbers).
        try:
            total += int(arg)
        except ValueError as e:
            # This case should not happen based on the prompt's assumption,
            # but it's good practice to handle potential conversion errors.
            print(f"Error: Argument '{arg}' could not be converted to an integer. {e}", file=sys.stderr)
            return

    # Print the final result followed by a new line
    print(total)


if __name__ == "__main__":
    add_args()
