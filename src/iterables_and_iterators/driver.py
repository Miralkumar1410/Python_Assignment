
from iterables_and_iterators.util import itertools

if __name__=='__main__':
    n = int(input())
    letters = "".join(input().split())
    k = int(input())
    print(itertools(letters,k))
