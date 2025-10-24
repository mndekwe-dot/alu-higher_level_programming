#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    """
    Performs basic arithmetic operations using functions imported
    from calculator_1 and prints the results.
    """
    a = 10
    b = 5

    # Use a single blank line to separate logical sections of the code,
    # as seen here between the variable assignments and the print statements.
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    # Add two blank lines after function/class definitions (main in this case)
    # before the next top-level code block (if __name__ == "__main__":).
    main()
