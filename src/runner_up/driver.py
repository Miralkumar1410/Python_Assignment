from src.runner_up.util import runner_up_score

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(runner_up_score(arr))