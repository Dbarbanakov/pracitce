def bin_search(arr, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            return bin_search(arr, mid + 1, right, x)

        else:
            return bin_search(arr, left, mid - 1, x)

    return False


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(bin_search(l1, 0, len(l1), 10))
