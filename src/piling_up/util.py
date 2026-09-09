def piling_up(cases):
    results = []

    for z in cases:
        z = z.copy()
        L = []

        while z:
            if z[0] >= z[-1]:
                l_max = z.pop(0)
            else:
                l_max = z.pop()

            L.append(l_max)

        if L == sorted(L, reverse=True):
            results.append("Yes")
        else:
            results.append("No")

    return results