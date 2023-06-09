#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        length_matrix = set(len(row))
        if length_matrix != 1:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_row.append(element / div)
        new_matrix.append(new_row)

