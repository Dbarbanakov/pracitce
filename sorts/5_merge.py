## Merge Sort ##

# Divides the array into smaller subarrays, sorts each subarray.
# Merges the sorted subarrays into a final sorted array.

# Comparison based, stable, Divide and Conquer, Recursive.
# Time complexity - O(nlog(n)) - All cases.
# Auxiliary Space - Not in-place.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

merge_sort(l1)

print(l1)
