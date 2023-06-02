## Cocktail Shaker Sort ##

# Variation of Bubble Sort.
# Traverses the list of elements both forward and backwards until the list is sorted.

# Comparison based, unstable.
# Time complexity - O(n^2) - worst and average cases. O(n) - best case(array is sorted).
# Auxiliary Space - O(1). In-place sort.


def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        start += 1


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

shaker_sort(l1)

print(l1)
