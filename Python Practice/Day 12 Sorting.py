"""
Day 12: Sorting Algorithms (Section 4: Q59–Q64)

This file covers basic to advanced sorting techniques.
All implementations are written in pure DSA style
without using built-in sorting functions.

Topics Covered:
59. Bubble Sort
60. Selection Sort
61. Insertion Sort
62. Merge Sort
63. Quick Sort
64. Sort array without using built-in function
"""

# --------------------------------------------------
# 59. Bubble Sort
# --------------------------------------------------
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# --------------------------------------------------
# 60. Selection Sort
# --------------------------------------------------
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # place minimum at correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# --------------------------------------------------
# 61. Insertion Sort
# --------------------------------------------------
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # shift elements to right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# --------------------------------------------------
# 62. Merge Sort
# --------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# --------------------------------------------------
# 63. Quick Sort
# --------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


# --------------------------------------------------
# 64. Sort array without using built-in function
# --------------------------------------------------
def manual_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# --------------------------------------------------
# Sample Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]

    print("Original Array:", arr)
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
    print("Manual Sort:", manual_sort(arr.copy()))
