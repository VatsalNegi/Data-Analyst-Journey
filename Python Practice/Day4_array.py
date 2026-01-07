"""
Day 4 – Arrays (DSA Practice)
Repository: Data_analyst0-Journey
Focus: Core Array Problems for Data Analyst Interviews

Questions Covered:
19. Two Sum (Hashing – DSA)
20. Check if Array is Sorted
21. Pascal's Triangle
22. Frequency of Elements in Array
23. Smallest and Largest Element
"""

# --------------------------------------------------
# Question 19: Two Sum (DSA Hashing)
# --------------------------------------------------
def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        required = target - arr[i]

        if required in seen:
            return seen[required], i

        seen[arr[i]] = i

    return None


# --------------------------------------------------
# Question 20: Check if Array is Sorted
# --------------------------------------------------
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# --------------------------------------------------
# Question 21: Pascal's Triangle
# --------------------------------------------------
def pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle


# --------------------------------------------------
# Question 22: Frequency of Elements
# --------------------------------------------------
def frequency_count(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# --------------------------------------------------
# Question 23: Smallest and Largest Element
# --------------------------------------------------
def min_max(arr):
    smallest = arr[0]
    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
        if arr[i] > largest:
            largest = arr[i]

    return smallest, largest


# --------------------------------------------------
# DRIVER CODE (TESTING)
# --------------------------------------------------
if __name__ == "__main__":

    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Is Sorted:", is_sorted([1, 2, 3, 4]))
    print("Pascal Triangle:", pascals_triangle(4))
    print("Frequency:", frequency_count([1, 2, 2, 3, 1, 4, 2]))
    print("Min & Max:", min_max([7, 2, 9, 4, 1, 6]))
