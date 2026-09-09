def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range(1,n+1):
        print(
        f"{i:>{width}} "
        f"{oct(i)[2:]:>{width}} "
        f"{hex(i)[2:].upper():>{width}} "
        f"{bin(i)[2:]:>{width}}"
        )
