from itertools import combinations
from math import comb


def itertools(letters, k):

    total = comb(len(letters), k)
    count = sum('A' in i for i in combinations(letters, k))

    return f'{count / total:.3f}'