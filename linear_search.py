def lsearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return f"{n} is at position {i+1}"
    return 0


l1 = [1, 2, 3, 4, 5, 6, 7]

print(lsearch(l1, 5))
print(lsearch(l1, 0))
