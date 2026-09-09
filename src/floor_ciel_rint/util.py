import numpy

def floor_ceil_rint(array):

    return (
        numpy.floor(array).tolist(),
        numpy.ceil(array).tolist(),
        numpy.rint(array).tolist()
    )