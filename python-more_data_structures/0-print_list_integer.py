#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2-dimensional array (default: empty list)

    Returns:
        A new matrix with the same size where each value is the square
        of the corresponding value in the input matrix
    """
    return [[element ** 2 for element in row] for row in matrix]
