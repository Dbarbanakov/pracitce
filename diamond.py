# n must be an odd number.
def print_diamond(n):
    for i in range(n):
        if i < n // 2:
            print(" " * (n // 2 - i) + "*" * (i * 2 + 1))
        if i == n // 2:
            print("*" * n)
        if i > n // 2:
            print(" " * (i - n // 2) + "*" * ((n - i) * 2 - 1))


print_diamond(13)
