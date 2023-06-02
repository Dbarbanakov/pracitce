## Selection Sort ##

# Find the minimum element in the unsorted portion of the array.Swaps it with the 1st element from that sub-array.
# Repeats until the array is sorted.

# Comparison based, unstable.
# Time complexity - O(n^2) in all cases(worst, average, best).
# Auxiliary Space - O(1). In-place sort.


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

selection_sort(l1)

print(l1)
