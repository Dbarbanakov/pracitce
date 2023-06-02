## Bitonic Sort ##

# Form a Bitonic Sequence.
# Create a sorted Sequence from the Bitonic Sequence.

# Bitonic Sort works only on arrays with length by the power of 2.

# A sequence with elements in increasing order then decreasing is Bitonic.
# Sorted array is a Bitonic Sequence, which is missing its decreasing or increasing part.

# Comparison based, stable.
# Time complexity - O(log^2(n))
# Auxiliary Space - O(log^2(n))


# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
def compAndSwap(arr, i, j, dire):
    if (dire == 1 and arr[i] > arr[j]) or (dire == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]


# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(arr, i, i + k, direction)
        bitonicMerge(arr, low, k, direction)
        bitonicMerge(arr, low + k, k, direction)


# This function first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(arr, low, k, 1)
        bitonicSort(arr, low + k, k, 0)
        bitonicMerge(arr, low, cnt, dire)


# Caller of bitonicSort for sorting the entire array of length N
# in ASCENDING order
def sort(arr):
    n = len(arr)
    bitonicSort(arr, 0, n, 1)


l1 = [3, 7, 4, 8, 6, 2, 1, 5]

sort(l1)

print(l1)
