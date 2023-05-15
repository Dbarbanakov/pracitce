def gcd(a, b):
    # a and b should be greater than 1.
    gcd = 0
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


print(gcd(5, 6))
print(gcd(5, 5))
print(gcd(6, 36))
