## Cycle Sort ##

# Divide the input array into Cycles.
# Each Cycle consists of elements that belong to the same position in the sorted array.
# Swaps are made to place each element in its correct position within its Cycle.

# Comparison based, Unstable,
# Time complexity - O(n) - All cases.
# Auxiliary Space - O(1). In-place sort.


def cycle_sort(arr):
    n = len(arr)
    writes = 0

    for cycleStart in range(0, n - 1):
        item = arr[cycleStart]

        # Find where to put the item.
        pos = cycleStart
        for i in range(cycleStart + 1, n):
            if arr[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:
            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

    return writes


l1 = [12, -5, 15, 1, 0, 8, 6, 20, 2, 0, -5, 1]

print(cycle_sort(l1))

print(l1)
