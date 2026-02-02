"""
===========================================================
DAY 9 – PCA (PRINCIPAL COMPONENT ANALYSIS)
===========================================================

This file covers:
1. What is Dimensionality Reduction?
2. What is PCA?
3. Why PCA is needed?
4. Key Terms in PCA
5. How PCA Works (Step-by-Step)
6. Mathematical Intuition
7. PCA From Scratch (Concept)
8. PCA using sklearn
9. Advantages & Disadvantages
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS DIMENSIONALITY REDUCTION?
# =========================================================
"""
Dimensionality Reduction means reducing the number of features
while keeping maximum important information.

Example:
- 100 features → 10 features
"""

# =========================================================
# 2. WHAT IS PCA?
# =========================================================
"""
PCA (Principal Component Analysis) is an UNSUPERVISED
dimensionality reduction technique.

It transforms original features into new features
called PRINCIPAL COMPONENTS.
"""

# =========================================================
# 3. WHY PCA IS NEEDED?
# =========================================================
"""
Problems with high dimensions:
1. Curse of dimensionality
2. Slow training
3. Overfitting
4. Visualization difficulty

PCA solves:
✔ Reduces dimensions
✔ Removes correlated features
✔ Improves performance
"""

# =========================================================
# 4. KEY TERMS IN PCA
# =========================================================
"""
Principal Component:
- New axis with maximum variance

Eigenvalues:
- Amount of variance captured

Eigenvectors:
- Direction of new axis
"""

# =========================================================
# 5. HOW PCA WORKS (STEP-BY-STEP)
# =========================================================
"""
1. Standardize data
2. Compute covariance matrix
3. Compute eigenvalues & eigenvectors
4. Sort by eigenvalues
5. Select top K components
6. Transform data
"""

# =========================================================
# 6. MATHEMATICAL INTUITION
# =========================================================
"""
Covariance Matrix:
Shows relationship between features

Goal:
Maximize variance along new axes
"""

# =========================================================
# 7. PCA FROM SCRATCH (CONCEPTUAL)
# =========================================================

import numpy as np

# Sample dataset
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2, 1.6],
    [1, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

# Step 1: Mean centering
X_meaned = X - np.mean(X, axis=0)

# Step 2: Covariance matrix
cov_matrix = np.cov(X_meaned, rowvar=False)

# Step 3: Eigen decomposition
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)

print("Eigen Values:", eigen_values)
print("Eigen Vectors:\n", eigen_vectors)

# Step 4: Sort eigenvalues
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

# Step 5: Select top 1 component
W = sorted_eigenvectors[:, 0:1]

# Step 6: Transform data
X_reduced = np.dot(X_meaned, W)

print("Reduced Data:\n", X_reduced)

# =========================================================
# 8. PCA USING SKLEARN
# =========================================================

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Standardize
X_scaled = StandardScaler().fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. Reduces dimensionality
2. Removes multicollinearity
3. Improves model speed
4. Helps visualization

Disadvantages:
1. Loss of interpretability
2. Information loss
3. Linear method only
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is PCA?
Ans: Unsupervised dimensionality reduction technique.

Q2. Is PCA supervised?
Ans: No.

Q3. What is principal component?
Ans: New feature with maximum variance.

Q4. Why standardization is required?
Ans: PCA is scale-sensitive.

Q5. What does explained variance mean?
Ans: Amount of information captured.

Q6. PCA vs Feature Selection?
Ans:
- PCA creates new features
- Feature selection keeps original features

Q7. Can PCA increase accuracy?
Ans: Sometimes, by reducing noise.

Q8. Does PCA remove multicollinearity?
Ans: Yes.

Q9. Is PCA good for non-linear data?
Ans: No.

Q10. What are eigenvalues?
Ans: Variance captured by components.
"""

print("\nDAY 9 PCA COMPLETED ✅")

