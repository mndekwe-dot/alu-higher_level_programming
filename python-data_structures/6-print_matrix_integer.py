def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    
    Args:
        matrix: A 2D list (matrix) of integers (default: empty matrix)
    """
    for row in matrix:
        for j in range(len(row)):
            if j > 0:
                print(" ", end="")
            print("{:d}".format(row[j]), end="")
        print()
