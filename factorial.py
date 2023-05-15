def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))
