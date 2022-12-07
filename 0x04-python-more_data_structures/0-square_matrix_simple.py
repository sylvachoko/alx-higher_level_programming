#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for i in matrix:
        sqr.append(list(map(lambda i: i**2, i)))
    return (sqr)
