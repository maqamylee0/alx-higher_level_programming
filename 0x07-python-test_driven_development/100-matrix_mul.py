#!/usr/bin/python3
"""module to multiply 2 matrices"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    for matrix in (m_a, m_b):
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("m_a must be a list of lists or m_b must "
                            "be a list of lists")
        if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
            raise ValueError("m_a can't be empty or m_b can't be empty")
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("m_a should contain only integers or "
                                    "floats or m_b should contain only "
                                    "integers or floats")
        if len(m_a[0]) != len(m_b[0]):
            raise ValueError("m_a and m_b can't be multiplied")
        matrix_mul = []
        for i in range(len(m_a)):
            new_row = []
            for k in range(len(m_b[0])):
                element = sum(m_a[i][h] * m_b[h][k] for h in range(len(m_b)))
                new_row.append(element)
            matrix_mul.append(new_row)
        return matrix_mul
