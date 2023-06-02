## Odd-Even Sort ##

# Variation of Bubble Sort.
# Sorts the list in 2 phases - Bubble Sort on odd indexes then on even.

# Comparison based, unstable.
# Time complexity - O(n^2) - worst and average cases. O(n) - best case(array is sorted).
# Auxiliary Space - O(1). In-place sort.


def odd_even(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        for i in range(1, n - 1, 2):
            print(arr[i], arr[i + 1])

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

odd_even(l1)

print(l1)
