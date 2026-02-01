"""
===========================================================
DAY 8 – DBSCAN (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Clustering?
2. What is DBSCAN?
3. Why DBSCAN is needed?
4. Key Terms: eps, min_samples
5. Types of Points in DBSCAN
6. How DBSCAN Works (Step-by-Step)
7. DBSCAN From Scratch (Conceptual Logic)
8. DBSCAN using sklearn
9. Advantages & Disadvantages
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS CLUSTERING?
# =========================================================
"""
Clustering is an UNSUPERVISED learning technique.

Goal:
- Group similar data points
- No predefined labels

Examples:
- Customer segmentation
- Fraud detection
- Noise / anomaly detection
"""

# =========================================================
# 2. WHAT IS DBSCAN?
# =========================================================
"""
DBSCAN stands for:
Density-Based Spatial Clustering of Applications with Noise

DBSCAN groups points that are closely packed together
and marks points in low-density regions as NOISE.
"""

# =========================================================
# 3. WHY DBSCAN IS NEEDED?
# =========================================================
"""
Problems with K-Means:
1. Must specify K beforehand
2. Sensitive to outliers
3. Poor with irregular shaped clusters

DBSCAN solves:
✔ No need to specify K
✔ Detects outliers
✔ Works with arbitrary shapes
"""

# =========================================================
# 4. KEY TERMS IN DBSCAN
# =========================================================
"""
eps (ε):
- Radius around a point

min_samples:
- Minimum number of points required inside eps

These two decide cluster formation.
"""

# =========================================================
# 5. TYPES OF POINTS IN DBSCAN
# =========================================================
"""
1. Core Point:
   - At least min_samples within eps

2. Border Point:
   - Less than min_samples but near a core point

3. Noise Point:
   - Not part of any cluster
"""

# =========================================================
# 6. HOW DBSCAN WORKS (STEP-BY-STEP)
# =========================================================
"""
1. Select an unvisited point
2. Find neighbors within eps
3. If neighbors >= min_samples → Core point
4. Expand cluster
5. Repeat until all points are visited
"""

# =========================================================
# 7. DBSCAN FROM SCRATCH (CONCEPTUAL LOGIC)
# =========================================================
"""
Below is NOT a full production DBSCAN,
but helps understand the idea clearly.
"""

import math

# Sample dataset (2D points)
data = [
    [1, 2], [2, 2], [2, 3],
    [8, 7], [8, 8], [25, 80]
]

eps = 2
min_samples = 2

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def region_query(point):
    neighbors = []
    for p in data:
        if euclidean_distance(point, p) <= eps:
            neighbors.append(p)
    return neighbors

# Identify core points
for point in data:
    neighbors = region_query(point)
    if len(neighbors) >= min_samples:
        print(point, "→ Core Point")
    else:
        print(point, "→ Border / Noise Point")

# =========================================================
# 8. DBSCAN USING SKLEARN
# =========================================================

from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

X = np.array(data)

dbscan = DBSCAN(eps=2, min_samples=2)
labels = dbscan.fit_predict(X)

print("\nCluster Labels:", labels)
# -1 label means NOISE

# Visualization
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.title("DBSCAN Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. No need to choose number of clusters
2. Detects noise and outliers
3. Works with non-linear cluster shapes

Disadvantages:
1. Difficult to choose eps
2. Poor performance on varying density
3. Not ideal for very high-dimensional data
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is DBSCAN?
Ans: Density-based clustering algorithm.

Q2. Is DBSCAN supervised?
Ans: No, it is unsupervised.

Q3. What are the main parameters?
Ans: eps and min_samples.

Q4. What is a core point?
Ans: A point with at least min_samples neighbors within eps.

Q5. What does label -1 mean?
Ans: Noise point.

Q6. DBSCAN vs K-Means?
Ans:
- DBSCAN detects outliers
- K-Means needs K value

Q7. Can DBSCAN handle arbitrary shapes?
Ans: Yes.

Q8. Is DBSCAN sensitive to feature scaling?
Ans: Yes.

Q9. Can DBSCAN work with large datasets?
Ans: It can be slow without optimization.

Q10. When should DBSCAN be preferred?
Ans: When outliers and irregular clusters exist.
"""

print("\nDAY 8 DBSCAN COMPLETED ✅")

