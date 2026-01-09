"""
Day 6 – Arrays (Part 2)
Repository: Data_analyst0-Journey
Focus: DSA for Data Analyst Role

Questions Covered:
29. Find Duplicate Elements in an Array
30. Remove Duplicates from an Array
31. Union of Two Arrays
32. Intersection of Two Arrays
33. Move All Zeros to End of Array
"""

# --------------------------------------------------
# Q29: Find Duplicate Elements in an Array
# --------------------------------------------------
def find_duplicates(arr):
    freq = {}
    duplicates = []

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key in freq:
        if freq[key] > 1:
            duplicates.append(key)

    return duplicates


# --------------------------------------------------
# Q30: Remove Duplicates from an Array (Preserve Order)
# --------------------------------------------------
def remove_duplicates(arr):
    seen = {}
    result = []

    for num in arr:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result


# --------------------------------------------------
# Q31: Union of Two Arrays
# --------------------------------------------------
def union_arrays(arr1, arr2):
    seen = {}
    union = []

    for num in arr1:
        if num not in seen:
            seen[num] = True
            union.append(num)

    for num in arr2:
        if num not in seen:
            seen[num] = True
            union.append(num)

    return union


# --------------------------------------------------
# Q32: Intersection of Two Arrays
# --------------------------------------------------
def intersection_arrays(arr1, arr2):
    seen = {}
    intersection = []

    for num in arr1:
        seen[num] = True

    for num in arr2:
        if num in seen:
            intersection.append(num)
            del seen[num]

    return intersection


# --------------------------------------------------
# Q33: Move All Zeros to End of Array
# --------------------------------------------------
def move_zeros_to_end(arr):
    pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < len(arr):
        arr[pos] = 0
        pos += 1

    return arr


# --------------------------------------------------
# DRIVER CODE (Testing)
# --------------------------------------------------
if __name__ == "__main__":

    arr = [1, 2, 3, 2, 4, 1, 5]
    print("Duplicates:", find_duplicates(arr))

    print("After removing duplicates:", remove_duplicates(arr))

    arr1 = [1, 2, 3, 4]
    arr2 = [3, 4, 5, 6]
    print("Union:", union_arrays(arr1, arr2))
    print("Intersection:", intersection_arrays(arr1, arr2))

    arr_zero = [0, 1, 0, 3, 12]
    print("Move zeros:", move_zeros_to_end(arr_zero))
