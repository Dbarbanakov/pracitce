def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 1]

bubble_sort(l1)

print(l1)
