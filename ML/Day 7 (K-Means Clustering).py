"""
===========================================================
DAY 7 – K-MEANS CLUSTERING (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Clustering?
2. What is K-Means Clustering?
3. Why K-Means is Unsupervised?
4. How K-Means Algorithm Works
5. Mathematical Intuition
6. K-Means From Scratch (Logic)
7. K-Means using sklearn
8. Choosing K (Elbow Method)
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
- Group similar data points together
- No output labels are given

Example:
- Customer segmentation
- Grouping similar documents
- Image compression
"""

# =========================================================
# 2. WHAT IS K-MEANS CLUSTERING?
# =========================================================
"""
K-Means is the most popular clustering algorithm.

K = number of clusters

It divides data into K groups such that:
➡ Distance between data point and its cluster center is minimum
"""

# =========================================================
# 3. WHY K-MEANS IS UNSUPERVISED?
# =========================================================
"""
Because:
- There is NO target variable (Y)
- Algorithm discovers patterns by itself
"""

# =========================================================
# 4. HOW K-MEANS WORKS (STEP-BY-STEP)
# =========================================================
"""
1. Choose number of clusters K
2. Initialize K centroids randomly
3. Assign each data point to nearest centroid
4. Update centroid positions
5. Repeat steps 3 & 4 until convergence
"""

# =========================================================
# 5. MATHEMATICAL INTUITION
# =========================================================
"""
Distance metric used:
- Euclidean Distance

Formula:
distance = sqrt((x2-x1)^2 + (y2-y1)^2)

Objective:
Minimize Within Cluster Sum of Squares (WCSS)
"""

# =========================================================
# 6. K-MEANS FROM SCRATCH (LOGIC)
# =========================================================

import random
import math

# Sample 2D dataset
data = [
    [1, 2], [1, 4], [1, 0],
    [10, 2], [10, 4], [10, 0]
]

K = 2

# Randomly initialize centroids
centroids = random.sample(data, K)

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

for _ in range(5):  # iterations
    clusters = {i: [] for i in range(K)}

    # Assign points to nearest centroid
    for point in data:
        distances = [euclidean_distance(point, c) for c in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)

    # Update centroids
    new_centroids = []
    for i in clusters:
        x_avg = sum(p[0] for p in clusters[i]) / len(clusters[i])
        y_avg = sum(p[1] for p in clusters[i]) / len(clusters[i])
        new_centroids.append([x_avg, y_avg])

    centroids = new_centroids

print("Final Centroids (From Scratch):", centroids)

# =========================================================
# 7. K-MEANS USING SKLEARN
# =========================================================

from sklearn.cluster import KMeans
import numpy as np

X = np.array(data)

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

print("Centroids (Sklearn):", kmeans.cluster_centers_)
print("Cluster Labels:", kmeans.labels_)

# =========================================================
# 8. CHOOSING K – ELBOW METHOD
# =========================================================
"""
Elbow Method:
- Plot K vs WCSS
- Point where decrease slows → best K
"""

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X_blob, _ = make_blobs(n_samples=300, centers=4, random_state=42)

wcss = []
for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_blob)
    wcss.append(km.inertia_)

plt.plot(range(1, 10), wcss)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. Simple & fast
2. Easy to implement
3. Scales well for large datasets

Disadvantages:
1. Need to choose K beforehand
2. Sensitive to outliers
3. Works poorly with non-spherical clusters
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is K-Means?
Ans: An unsupervised clustering algorithm.

Q2. What does K represent?
Ans: Number of clusters.

Q3. Is K-Means supervised?
Ans: No.

Q4. What distance metric is used?
Ans: Euclidean distance.

Q5. What is WCSS?
Ans: Sum of squared distances within a cluster.

Q6. How to choose K?
Ans: Elbow Method.

Q7. Is K-Means sensitive to outliers?
Ans: Yes.

Q8. Can K-Means work with categorical data?
Ans: No (needs numerical data).

Q9. Does K-Means guarantee global optimum?
Ans: No (depends on initialization).

Q10. What happens if K is very large?
Ans: Overfitting.
"""

print("\nDAY 7 K-MEANS CLUSTERING COMPLETED ✅")

