from src.lists.util import list_operations

if __name__ == '__main__':

    N = int(input())
    list = []

    for num in range(N):
        command = input().split()
        list_operations(list, command)