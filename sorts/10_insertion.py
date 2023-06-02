## Insertion Sort ##

# Splits the array into two parts - sorted and unsorted
# Takes elements from the unsorted part and places them at their correct position in the sorted one.

# Comparison based, stable.
# Time complexity - O(n^2) - worst and average cases. O(n) - best case(array is sorted).
# Auxiliary Space - O(1)


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

insertion_sort(l1)

print(l1)
