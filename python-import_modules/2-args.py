#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments, excluding the script name itself (sys.argv[0])
    num_args = len(sys.argv) - 1

    # Determine the correct pluralization and separator character
    if num_args == 1:
        plural = "argument"
        separator = ":"
    else:
        plural = "arguments"
        separator = "." if num_args == 0 else ":"

    # Print the header line
    print("{} {}{}".format(num_args, plural, separator))

    # Print each argument along with its position (1-based index)
    if num_args > 0:
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
