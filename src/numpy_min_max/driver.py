import numpy as np

from src.numpy_min_max.util import min_max

if __name__ == '__main__':

    n, m = map(int, input().split())

    np_array = np.array(
        [input().split() for _ in range(n)],
        int
    )
    print(min_max(np_array))