import numpy as np

def min_max(np_array):
    np_array = np.array(np_array)

    minimum = np.min(np_array)
    maximum = np.max(np_array)

    return minimum, maximum