"""
Day 15: Recursion (DSA)

Topics Covered:
1. Factorial of a Number
2. Fibonacci Number
3. Reverse an Array
4. Generate All Subsets (Power Set)

Author: Vatsal Negi
Purpose: DSA + Interview Preparation
"""

# ---------------------------------------------------
# 1. Factorial of a Number (Recursion)
# ---------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:      # Base case
        return 1
    return n * factorial(n - 1)


# ---------------------------------------------------
# 2. Fibonacci Number (Recursion)
# ---------------------------------------------------

def fibonacci(n):
    if n == 0:               # Base case
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------------------
# 3. Reverse an Array (Recursion)
# ---------------------------------------------------

def reverse_array(arr, left, right):
    if left >= right:        # Base case
        return

    # Swap elements
    arr[left], arr[right] = arr[right], arr[left]

    # Recursive call
    reverse_array(arr, left + 1, right - 1)


# ---------------------------------------------------
# 4. Generate All Subsets (Power Set)
# ---------------------------------------------------

def generate_subsets(arr, index, current):
    if index == len(arr):    # Base case
        print(current)
        return

    # Include current element
    generate_subsets(arr, index + 1, current + [arr[index]])

    # Exclude current element
    generate_subsets(arr, index + 1, current)


# ---------------------------------------------------
# Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":
    # Factorial
    print("Factorial of 5:", factorial(5))

    # Fibonacci
    print("Fibonacci of 6:", fibonacci(6))

    # Reverse Array
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr, 0, len(arr) - 1)
    print("Reversed Array:", arr)

    # Generate Subsets
    print("Subsets:")
    generate_subsets([1, 2, 3], 0, [])
  
