## Heap Sort ##

# Based on the Binary Heap data structure.
# Place the largest element in its correct position.
# Heapify the data structure.
# Repeat until done.

# Heapify is the process of creating a Heap data structure from a Binary Tree represented by an array.
# Can only be applied to a Node if its children are Heapified.

# Comparison based, Unstable.
# Time complexity - O(Nlog(N))
# Auxiliary Space - O(1). In-place sort.


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

heap_sort(l1)

print(l1)
