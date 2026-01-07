"""
=========================================
DAY 4 – NUMPY FOR DATA ANALYST
Author: Vatsal Negi
Purpose: NumPy fundamentals + advanced concepts
=========================================

Topics Covered:
1. Array Creation
2. Array Attributes
3. Indexing & Slicing
4. Mathematical Operations
5. Broadcasting
6. Aggregation Functions
7. Reshaping & Flattening
8. Boolean Indexing
9. Random Module
10. Sorting & Unique
11. Linear Algebra
12. Handling Missing Values
13. Performance Tips
"""

import numpy as np

print("\n========== 1. ARRAY CREATION ==========")

arr1 = np.array([10, 20, 30, 40])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
print("Zeros Array:\n", zeros)
print("Ones Array:\n", ones)

range_arr = np.arange(1, 10, 2)
lin_arr = np.linspace(0, 1, 5)
print("Arange:", range_arr)
print("Linspace:", lin_arr)


print("\n========== 2. ARRAY ATTRIBUTES ==========")

print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)


print("\n========== 3. INDEXING & SLICING ==========")

print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice [1:3]:", arr1[1:3])

print("2D Element [1,2]:", arr2[1, 2])
print("First row:", arr2[0, :])
print("Second column:", arr2[:, 1])


print("\n========== 4. MATHEMATICAL OPERATIONS ==========")

nums = np.array([1, 4, 9, 16])
print("Add 5:", nums + 5)
print("Multiply:", nums * 2)
print("Square root:", np.sqrt(nums))
print("Log:", np.log(nums))


print("\n========== 5. BROADCASTING ==========")

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
print("Broadcast Result:\n", A + B)


print("\n========== 6. AGGREGATION FUNCTIONS ==========")

data = np.array([10, 20, 30, 40, 50])
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))


print("\n========== 7. RESHAPING & FLATTENING ==========")

reshape_arr = np.arange(1, 7).reshape(2, 3)
print("Reshaped Array:\n", reshape_arr)

print("Flatten:", reshape_arr.flatten())
print("Ravel:", reshape_arr.ravel())


print("\n========== 8. BOOLEAN INDEXING ==========")

scores = np.array([45, 60, 72, 90, 38])
passed = scores[scores >= 60]
print("Passed Scores:", passed)


print("\n========== 9. RANDOM MODULE ==========")

print("Random Float:", np.random.rand())
print("Random Array:\n", np.random.rand(2, 3))
print("Random Integers:\n", np.random.randint(1, 100, size=5))


print("\n========== 10. SORTING & UNIQUE ==========")

arr = np.array([3, 1, 4, 2, 3, 1])
print("Sorted:", np.sort(arr))
print("Unique Values:", np.unique(arr))


print("\n========== 11. LINEAR ALGEBRA ==========")

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", X + Y)
print("Matrix Multiplication:\n", np.dot(X, Y))
print("Transpose:\n", X.T)
print("Determinant:", np.linalg.det(X))
print("Inverse:\n", np.linalg.inv(X))


print("\n========== 12. HANDLING MISSING VALUES ==========")

nan_arr = np.array([1, 2, np.nan, 4, np.nan])
print("Original:", nan_arr)
print("Is NaN:", np.isnan(nan_arr))
print("Mean without NaN:", np.nanmean(nan_arr))


print("\n========== 13. COPY VS VIEW ==========")

original = np.array([10, 20, 30])
view_arr = original.view()
copy_arr = original.copy()

view_arr[0] = 999

print("Original after view change:", original)
print("Copy remains:", copy_arr)


print("\n========== 14. PERFORMANCE TIPS ==========")

# Vectorized operation (FAST)
big_arr = np.arange(1_000_000)
result = big_arr * 2
print("Vectorized operation completed")

print("\n========== DAY 4 NUMPY COMPLETED ==========")
