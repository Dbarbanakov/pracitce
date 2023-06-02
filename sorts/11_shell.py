## Shell Sort ##

# Variation of Insertion Sort.The idea is to exchange far items, not just adjacent.
# We make the array h-sorted for a large value of h.
# We reduce the value of h, until it becomes 1.
# An array is said to be h-sorted if every subarray starting with h-th element are sorted.

# Comparison based, stable.
# Time complexity - O(n^2) - Worst case, O(nlog(n)) - Best and Average cases.
# Auxiliary Space - O(1)


def shell_sort(arr):
    n = len(arr)

    gap = n // 2
    while gap > 0:
        j = gap

        while j < n:
            i = j - gap

            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break

                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap
            j += 1
        gap = gap // 2


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

shell_sort(l1)

print(l1)
