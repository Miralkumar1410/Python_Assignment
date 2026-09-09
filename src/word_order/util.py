from collections import Counter 
def word_order(n):
    ls =[]
    for i in range(n):
        row = str(input())
        ls.append(row)
    cntr = Counter(ls)
    return (
    print(len(cntr)),
    print(*cntr.values())
    )