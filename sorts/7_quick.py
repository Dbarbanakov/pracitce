## Quick Sort ##

# Picks an element as a pivot.
# Partitions the given array around the pivot.
# Places the pivot in its correct position in the sorted array.
# Repeats until the array is sorted.

# Comparison based, Unstable, Divide and Conquer, Recursive.
# Time complexity - O(nlog(n)) - Best and Average cases. O(n^2) - Worst case.
# Auxiliary Space - O(log(n)). - used for the recursive calls.


def quick_sort(arr, left, right):
    def partition(arr, left, right):
        pivot = arr[right]

        i = left - 1
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[right], arr[i + 1] = arr[i + 1], arr[right]
        return i + 1

    if left < right:
        pi = partition(arr, left, right)

        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

quick_sort(l1, 0, (len(l1) - 1))

print(l1)
