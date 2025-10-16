#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names (attributes) defined in the imported module
    names = dir(hidden_4)

    # Filter and print names
    # 1. Sort the names alphabetically
    # 2. Filter out names that start with '__'
    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
