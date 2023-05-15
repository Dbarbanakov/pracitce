# Armstrong number - 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153


def arm_num(n):
    s = 0

    for x in str(n):
        s += int(x) ** 3

    return True if n == s else False


print(arm_num(153))
print(arm_num(154))
