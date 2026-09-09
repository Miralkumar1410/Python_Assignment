import numpy.linalg as nl


def lin_alg(arr):
    determinant = round(nl.det(arr), 2)
    inverse = nl.inv(arr).tolist()

    inverse = [
        [round(value, 2) for value in row]
        for row in inverse
    ]

    return determinant, inverse