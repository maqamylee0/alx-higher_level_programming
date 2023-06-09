#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length_matrix = len(matrix[0])
    for row in matrix:
        if length_matrix != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
