def no_idea(n, a, b):
    a = set(map(int, a))
    b = set(map(int, b))

    happiness = 0

    for num in n:
        num = int(num)

        if num in a:
            happiness += 1

        if num in b:
            happiness -= 1

    return happiness
