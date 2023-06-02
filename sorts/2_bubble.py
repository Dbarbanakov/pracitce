## Bubble Sort ##

# Iterate through the array, compares adjacent pairs, swaps if the order is incorrect.
# Repeats until the array is sorted.

# Comparison based, stable.
# Time complexity - O(n^2) - worst and average cases. O(n) - best case(array is sorted).
# Auxiliary Space - O(1). In-place sort.


def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

bubble_sort(l1)

print(l1)

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
