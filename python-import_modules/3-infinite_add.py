#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the total sum
    total = 0

    # Iterate over the command-line arguments starting from index 1 (to skip the script name)
    # Arguments are strings, so they must be cast to integers using int()
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])

    # Print the final result
    print(total)
