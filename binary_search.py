def binary_search(arr, left, right, x):
    if right >= left:
        mid = (right + left) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, right, x)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10

print(binary_search(arr, 0, len(arr) - 1, x))
