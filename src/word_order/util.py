from collections import Counter 
def word_order(n):
    ls = []

    for i in range(n):
        row = str(input())
        ls.append(row)

    cntr = Counter(ls)

    print(len(cntr))
    print(*cntr.values())