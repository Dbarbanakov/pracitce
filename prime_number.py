def prime_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(prime_check(6))
print(prime_check(7))
