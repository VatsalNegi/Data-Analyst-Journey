"""
===========================================================
DAY 5 – DECISION TREE (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Decision Tree?
2. Types of Decision Tree
3. Key Terminologies
4. How Decision Tree Works
5. Impurity Measures (Gini, Entropy)
6. Information Gain
7. Decision Tree From Scratch (Conceptual Code)
8. Decision Tree using sklearn
9. Advantages & Disadvantages
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS DECISION TREE?
# =========================================================
"""
Decision Tree is a supervised machine learning algorithm
used for BOTH:
- Classification
- Regression

It works like a tree structure:
- Root Node
- Internal Nodes
- Leaf Nodes

Example:
If weather is sunny → go outside
Else → stay inside
"""

# =========================================================
# 2. TYPES OF DECISION TREE
# =========================================================
"""
1. Classification Tree
   - Output is categorical (Yes/No)

2. Regression Tree
   - Output is continuous (Price, Salary)
"""

# =========================================================
# 3. KEY TERMINOLOGIES
# =========================================================
"""
Root Node      → Starting point of tree
Decision Node  → Splits the data
Leaf Node      → Final output
Splitting      → Dividing data
Pruning        → Removing extra branches
Depth          → Levels in tree
"""

# =========================================================
# 4. HOW DECISION TREE WORKS
# =========================================================
"""
1. Select best feature
2. Split data
3. Repeat for each child
4. Stop when:
   - Data is pure
   - Max depth reached
"""

# =========================================================
# 5. IMPURITY MEASURES
# =========================================================
"""
Impurity tells how mixed the data is.

Two common measures:
1. Gini Index
2. Entropy
"""

import math

def gini_index(labels):
    """
    Gini = 1 - Σ(p^2)
    """
    total = len(labels)
    classes = set(labels)
    gini = 1

    for c in classes:
        p = labels.count(c) / total
        gini -= p ** 2

    return gini


def entropy(labels):
    """
    Entropy = - Σ(p * log2(p))
    """
    total = len(labels)
    classes = set(labels)
    ent = 0

    for c in classes:
        p = labels.count(c) / total
        ent -= p * math.log2(p)

    return ent

# =========================================================
# 6. INFORMATION GAIN
# =========================================================
"""
Information Gain tells how good a split is.

IG = Entropy(parent) - Weighted Entropy(children)
"""

def information_gain(parent, left_child, right_child):
    total = len(parent)
    weight_left = len(left_child) / total
    weight_right = len(right_child) / total

    return entropy(parent) - (weight_left * entropy(left_child) + weight_right * entropy(right_child))

# =========================================================
# 7. DECISION TREE FROM SCRATCH (CONCEPT)
# =========================================================
"""
Below is a simplified conceptual approach.
(Not full production tree, but good for understanding & interviews)
"""

# Example dataset
# Feature: Study Hours
X = [1, 2, 3, 4, 5]
Y = ["Fail", "Fail", "Fail", "Pass", "Pass"]

# Simple rule-based split
def simple_decision_tree(x):
    if x >= 4:
        return "Pass"
    else:
        return "Fail"

print("Prediction for 2 hours:", simple_decision_tree(2))
print("Prediction for 5 hours:", simple_decision_tree(5))

# =========================================================
# 8. DECISION TREE USING SKLEARN
# =========================================================

from sklearn.tree import DecisionTreeClassifier
import numpy as np

X_np = np.array(X).reshape(-1, 1)
Y_np = np.array(Y)

model = DecisionTreeClassifier(criterion="gini", max_depth=2)
model.fit(X_np, Y_np)

print("Prediction for X=3:", model.predict([[3]]))
print("Prediction for X=5:", model.predict([[5]]))

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. Easy to understand
2. No feature scaling needed
3. Handles non-linear data
4. Works with numerical & categorical data

Disadvantages:
1. Overfitting
2. Sensitive to small data
3. Unstable trees
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is Decision Tree?
Ans: A supervised ML algorithm that splits data like a tree.

Q2. What impurity measures are used?
Ans: Gini Index and Entropy.

Q3. Difference between Gini and Entropy?
Ans:
- Gini is faster
- Entropy is more informative

Q4. What is Information Gain?
Ans: Reduction in entropy after split.

Q5. What is pruning?
Ans: Removing unnecessary branches to avoid overfitting.

Q6. Does Decision Tree need normalization?
Ans: No.

Q7. Can Decision Tree handle missing values?
Ans: Yes (with some strategies).

Q8. What is overfitting?
Ans: Model performs well on training but poor on testing.

Q9. Which algorithm uses entropy?
Ans: ID3

Q10. Which uses Gini Index?
Ans: CART
"""

print("\nDAY 3 DECISION TREE COMPLETED ✅")

