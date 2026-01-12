"""
=====================================================
DAY 1: LINEAR ALGEBRA BASICS FOR MACHINE LEARNING
=====================================================

Linear Algebra is the backbone of Machine Learning.

Almost everything in ML can be represented as:
- Vectors  → data points
- Matrices → datasets / model parameters
- Linear transformations → learning process

This file covers:
1. Coordinate Geometry & Straight Lines
2. Vectors (Algebra + Geometry)
3. Matrix Algebra
4. Determinants (Mathematical meaning)
5. Eigenvalues & Eigenvectors (core ML concept)
"""

import numpy as np

# =====================================================
# 1. COORDINATE GEOMETRY & STRAIGHT LINES
# =====================================================

"""
Equation of a straight line (slope-intercept form):

    y = m*x + c

where:
m = slope (rate of change)
c = y-intercept

Slope formula between two points:
    m = (y2 - y1) / (x2 - x1)

In ML:
- Linear Regression learns 'm' and 'c'
- Decision boundaries are straight lines/planes
"""

def straight_line(x, m, c):
    return m * x + c

x = np.array([-2, -1, 0, 1, 2])
y = straight_line(x, m=2, c=1)

print("Straight Line Example:")
print("x:", x)
print("y = 2x + 1:", y)
print("-" * 50)


# =====================================================
# 2. VECTORS (ALGEBRA + GEOMETRY)
# =====================================================

"""
A vector is an ordered collection of numbers.

Mathematically:
    v ∈ Rⁿ

Geometrically:
- Represents direction and magnitude
- In ML → one data point

Example:
    v = [x1, x2, x3]  → feature vector
"""

v1 = np.array([1, 2])
v2 = np.array([3, 4])

# Vector addition
"""
v1 + v2 = [1+3, 2+4] = [4, 6]
"""
v_add = v1 + v2

# Scalar multiplication
"""
k * v = [k*x1, k*x2]
"""
v_scalar = 3 * v1

# Dot Product
"""
Dot product formula:
    v1 · v2 = |v1||v2|cosθ
            = x1*x2 + y1*y2

In ML:
- Measures similarity
- Used in cosine similarity, neural networks
"""
dot_product = np.dot(v1, v2)

# Magnitude (Euclidean norm)
"""
||v|| = sqrt(x² + y²)
"""
magnitude_v1 = np.linalg.norm(v1)

print("Vector Operations:")
print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v_add)
print("3 * v1:", v_scalar)
print("v1 · v2:", dot_product)
print("||v1||:", magnitude_v1)
print("-" * 50)


# =====================================================
# 3. MATRICES & MATRIX OPERATIONS
# =====================================================

"""
A matrix is a 2D array of numbers.

A ∈ R^(m×n)

In ML:
- Dataset → matrix
- Weights → matrix
- Transformations → matrix multiplication
"""

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 2]])

# Matrix Addition
"""
A + B = element-wise addition
"""
matrix_add = A + B

# Matrix Multiplication
"""
Matrix multiplication rule:
(A)_(m×n) × (B)_(n×p) = (C)_(m×p)

Used heavily in:
- Linear Regression
- Neural Networks
"""
matrix_mul = A @ B

# Transpose
"""
Transpose:
Aᵀ → rows become columns
"""
transpose_A = A.T

print("Matrix Operations:")
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", matrix_add)
print("A × B:\n", matrix_mul)
print("Transpose of A:\n", transpose_A)
print("-" * 50)


# =====================================================
# 4. DETERMINANT (VERY IMPORTANT)
# =====================================================

"""
Determinant (2×2 matrix):

|a  b|
|c  d| = ad - bc

Geometric Meaning:
- Area scaling factor
- det = 0 → matrix is singular (no inverse)

In ML:
- Needed for matrix inversion
- Important in optimization algorithms
"""

det_A = np.linalg.det(A)

print("Determinant:")
print("det(A):", det_A)
print("-" * 50)


# =====================================================
# 5. EIGENVALUES & EIGENVECTORS
# =====================================================

"""
Definition:
A vector v is an eigenvector of matrix A if:

    A v = λ v

where:
λ = eigenvalue

Rewriting:
    (A - λI)v = 0

Non-trivial solution exists only if:
    det(A - λI) = 0

This is the characteristic equation.
"""

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Verification of eigen equation
for i in range(len(eigenvalues)):
    Av = A @ eigenvectors[:, i]
    lv = eigenvalues[i] * eigenvectors[:, i]

    print(f"\nVerification for Eigenvalue λ{i+1}:")
    print("A v =", Av)
    print("λ v =", lv)

"""
In ML:
- PCA uses eigenvectors of covariance matrix
- Eigenvalues indicate importance of directions
- Higher eigenvalue → more variance/information
"""

print("-" * 50)
print("DAY 1 LINEAR ALGEBRA COMPLETED ✔")

