def calc(n):
    s = 0
    p = 1

    n1 = int(input("1st number: "))
    n2 = int(input("2nd number: "))

    if n == 1:
        return n1 + n2
    elif n == 2:
        return n1 - n2
    elif n == 3:
        return n1 * n2
    else:
        return n1 / n2


print("1 - add, 2 - subtract, 3 - multiply, 4 - divide.")

i = int(input("Choose an operation to perform: "))

if i in (1, 2, 3, 4):
    print(calc(i))
else:
    print("Choose a valid operation.")
