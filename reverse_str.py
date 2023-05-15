def reverse1(s):
    rev_s = ""

    for i in range(-1, -(len(s) + 1), -1):
        rev_s += s[i]

    return rev_s


def reverse2(s):
    rev_s = ""

    for x in reversed(s):
        rev_s += x

    return rev_s


print(reverse1("hello"))
print(reverse2("hello"))
print("hello"[::-1])
