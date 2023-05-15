def root(n):
    for i in range(2, n + 1):
        print(i)
        if n / i == i:
            return i
        if n / i < i:
            return False


print(root(16))
print(root(17))

print(25**0.5)
