"""
Day 14: Binary Search (DSA)

Topics Covered:
1. Binary Search (Basic)
2. First & Last Occurrence of an Element
3. Search in Rotated Sorted Array
4. Binary Search on Answer (Square Root)

Author: Vatsal Negi
Purpose: DSA + Interview Preparation
"""

# ---------------------------------------------------
# 1. Binary Search (Basic)
# ---------------------------------------------------

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ---------------------------------------------------
# 2. First Occurrence of an Element
# ---------------------------------------------------

def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


# ---------------------------------------------------
# 3. Last Occurrence of an Element
# ---------------------------------------------------

def last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


# ---------------------------------------------------
# 4. Search in Rotated Sorted Array
# ---------------------------------------------------

def search_rotated_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# ---------------------------------------------------
# 5. Binary Search on Answer (Square Root)
# ---------------------------------------------------

def square_root_binary_search(n):
    low = 0
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


# ---------------------------------------------------
# Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":
    arr = [2, 4, 4, 4, 6, 8, 10]

    print("Binary Search:", binary_search(arr, 6))
    print("First Occurrence:", first_occurrence(arr, 4))
    print("Last Occurrence:", last_occurrence(arr, 4))

    rotated = [4, 5, 6, 7, 1, 2, 3]
    print("Search in Rotated Array:", search_rotated_array(rotated, 2))

    print("Square Root:", square_root_binary_search(40))
  
