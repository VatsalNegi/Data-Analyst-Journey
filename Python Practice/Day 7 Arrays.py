"""
Day 7 – Array DSA Practice (After Question 33)
Repository: Data_analyst0-Journey
Focus: Core DSA + Data Analyst Interview Logic

Questions Covered:
34. Move all negative numbers to one side
35. Majority Element (Boyer–Moore)
36. Maximum Subarray Sum (Kadane’s Algorithm)
37. Longest Subarray with Given Sum
38. Count Subarrays with Given Sum
39. Mean, Median, Mode
"""

# --------------------------------------------------
# Q34: Move All Negative Numbers to One Side
# --------------------------------------------------
def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# --------------------------------------------------
# Q35: Majority Element (Boyer–Moore Voting Algorithm)
# --------------------------------------------------
def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verification step
    freq = 0
    for num in arr:
        if num == candidate:
            freq += 1

    if freq > len(arr) // 2:
        return candidate
    return None


# --------------------------------------------------
# Q36: Maximum Subarray Sum (Kadane’s Algorithm)
# --------------------------------------------------
def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# --------------------------------------------------
# Q37: Longest Subarray with Given Sum
# --------------------------------------------------
def longest_subarray_with_sum(arr, k):
    sum_so_far = 0
    max_length = 0
    seen = {}

    for i in range(len(arr)):
        sum_so_far += arr[i]

        if sum_so_far == k:
            max_length = i + 1

        if (sum_so_far - k) in seen:
            length = i - seen[sum_so_far - k]
            if length > max_length:
                max_length = length

        if sum_so_far not in seen:
            seen[sum_so_far] = i

    return max_length


# --------------------------------------------------
# Q38: Count Subarrays with Given Sum
# --------------------------------------------------
def count_subarrays_with_sum(arr, k):
    count = 0
    sum_so_far = 0
    freq = {0: 1}

    for num in arr:
        sum_so_far += num

        if (sum_so_far - k) in freq:
            count += freq[sum_so_far - k]

        freq[sum_so_far] = freq.get(sum_so_far, 0) + 1

    return count


# --------------------------------------------------
# Q39: Mean, Median, Mode
# --------------------------------------------------
def mean_median_mode(arr):
    n = len(arr)

    # Mean
    total = 0
    for num in arr:
        total += num
    mean = total / n

    # Median
    arr.sort()
    if n % 2 != 0:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2

    # Mode
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_freq = 0
    mode = None
    for key in freq:
        if freq[key] > max_freq:
            max_freq = freq[key]
            mode = key

    return mean, median, mode


# --------------------------------------------------
# DRIVER CODE (Testing)
# --------------------------------------------------
if __name__ == "__main__":

    print("Q34 Move Negatives:", move_negatives([1, -2, 3, -4, -1, 4]))
    print("Q35 Majority Element:", majority_element([2, 2, 1, 2, 3, 2, 2]))
    print("Q36 Max Subarray Sum:", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
    print("Q37 Longest Subarray Sum=15:",
          longest_subarray_with_sum([10,5,2,7,1,9], 15))
    print("Q38 Count Subarrays Sum=2:",
          count_subarrays_with_sum([1,1,1], 2))
    print("Q39 Mean, Median, Mode:",
          mean_median_mode([1,2,2,3,4]))

