def insort(arr):
    for i in range(1, len(arr)):
        b = arr[i]

        k = i - 1
        while k >= 0 and b < arr[k]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]
            k -= 1


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 1]

insort(l1)

print(l1)
