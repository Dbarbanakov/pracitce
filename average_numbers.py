n = int(input("Amount of numbers: "))

s = 0
for i in range(n):
    num = int(input(f"{i+1}: "))
    s += num

print(s / n)


def average(arr):
    s = 0

    for x in arr:
        s += x

    return s / len(arr)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(average(l1))
print(sum(l1) / len(l1))
