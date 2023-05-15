def biggest_num(arr):
    n = len(arr)

    biggest = arr[0]
    for i in range(1, n):
        if arr[i] > biggest:
            biggest = arr[i]

    return biggest


l1 = [1, 2, 3, 6, 8]
l2 = [-1, 2, 13, 5]

print(biggest_num(l1))
print(biggest_num(l2))

print(max(l2))
