

from no_idea.util import no_idea


if __name__ == "__main__":

    n, m = map(int, input().split())

    array = input().split()
    set_a = input().split()
    set_b = input().split()

    happy = no_idea(array, set_a, set_b)

    print(happy)