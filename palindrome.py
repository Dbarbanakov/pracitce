def check1(n):
    return True if str(n) == str(n)[::-1] else False


def check2(n):
    s = str(n)

    mid = len(s) // 2

    if len(s) % 2 == 0:
        # if the number is even. then includes the middle index in the comparison.
        stop = mid + 1
    else:
        # if the number is odd, the middle index is excluded in the comparison.
        stop = mid

    for i in range(stop):
        if s[i] != s[-(i + 1)]:
            return False

    return True


print(check1(121))

print(check2(112211))
print(check2(11211))

print(check2(11231))
