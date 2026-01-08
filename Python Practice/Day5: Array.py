"""
Day 5 – Arrays DSA Practice (Python)
Repository: Data_analyst0-Journey
Focus: Core Array Logic for Data Analyst Interviews

Questions Covered:
24. Second Largest Element
25. Second Smallest Element
26. Reverse an Array
27. Rotate Array by K Positions
28. Find Missing Number
"""

# --------------------------------------------------
# Question 24: Second Largest Element
# --------------------------------------------------
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None


# --------------------------------------------------
# Question 25: Second Smallest Element
# --------------------------------------------------
def second_smallest(arr):
    smallest = float('inf')
    second = float('inf')

    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num

    return second if second != float('inf') else None


# --------------------------------------------------
# Question 26: Reverse an Array (In-place)
# --------------------------------------------------
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


# --------------------------------------------------
# Question 27: Rotate Array by K Positions (Right)
# --------------------------------------------------
def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    # Reverse entire array
    arr.reverse()

    # Reverse first k elements
    arr[:k] = reversed(arr[:k])

    # Reverse remaining elements
    arr[k:] = reversed(arr[k:])

    return arr


# --------------------------------------------------
# Question 28: Find Missing Number
# --------------------------------------------------
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2

    actual_sum = 0
    for num in arr:
        actual_sum += num

    return expected_sum - actual_sum


# --------------------------------------------------
# DRIVER CODE (Sample Testing)
# --------------------------------------------------
if __name__ == "__main__":

    arr = [1, 2, 2, 3, 1, 2]

    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Is Sorted:", is_sorted([1, 2, 3, 4]))
    print("Pascal Triangle:")
    for row in pascal_triangle(4):
        print(row)
    print("Frequency:", frequency_count(arr))
    print("Max Frequency:", max_frequency_element(arr))
    print("Second Largest:", second_largest([10, 5, 20, 8]))
    print("Second Smallest:", second_smallest([10, 5, 20, 8]))
    print("Reversed:", reverse_array([1, 2, 3, 4, 5]))
    print("Rotated:", rotate_array([1, 2, 3, 4, 5], 2))
    print("Missing Number:", find_missing_number([1, 2, 4, 5]))
