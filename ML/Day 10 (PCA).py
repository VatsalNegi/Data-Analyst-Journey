"""
===========================================================
DAY 10 – SUPPORT VECTOR MACHINE (SVM)
===========================================================

This file covers:
1. What is SVM?
2. Why SVM is needed?
3. Key Terminologies
4. Types of SVM
5. Kernel Trick
6. Mathematical Intuition
7. SVM for Classification
8. SVM for Regression (SVR)
9. Advantages & Disadvantages
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS SVM?
# =========================================================
"""
Support Vector Machine (SVM) is a supervised machine learning
algorithm used for:
- Classification
- Regression

Goal:
Find the BEST hyperplane that separates data points
with maximum margin.
"""

# =========================================================
# 2. WHY SVM IS NEEDED?
# =========================================================
"""
Benefits:
1. Works well in high-dimensional spaces
2. Effective when data is not linearly separable
3. Uses kernel trick
"""

# =========================================================
# 3. KEY TERMINOLOGIES
# =========================================================
"""
Hyperplane:
- Decision boundary separating classes

Margin:
- Distance between hyperplane and nearest points

Support Vectors:
- Data points closest to hyperplane
"""

# =========================================================
# 4. TYPES OF SVM
# =========================================================
"""
1. Linear SVM
2. Non-Linear SVM
3. SVM for Regression (SVR)
"""

# =========================================================
# 5. KERNEL TRICK
# =========================================================
"""
Kernel trick transforms data into higher dimensions
to make it linearly separable.

Common kernels:
- Linear
- Polynomial
- RBF (Gaussian)
- Sigmoid
"""

# =========================================================
# 6. MATHEMATICAL INTUITION
# =========================================================
"""
Objective:
Maximize margin while minimizing classification error.

Regularization parameter (C):
- Controls trade-off between margin and misclassification
"""

# =========================================================
# 7. SVM FOR CLASSIFICATION
# =========================================================

from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Binary classification (Class 0 vs 1)
X = X[y != 2]
y = y[y != 2]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create SVM model
svm_clf = SVC(kernel="linear", C=1)
svm_clf.fit(X_train, y_train)

# Prediction
y_pred = svm_clf.predict(X_test)

# Accuracy
print("SVM Classification Accuracy:",
      accuracy_score(y_test, y_pred))

# =========================================================
# 8. SVM FOR REGRESSION (SVR)
# =========================================================

from sklearn.svm import SVR
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Create regression dataset
X_reg, y_reg = make_regression(
    n_samples=200, n_features=1, noise=10, random_state=42
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# Create SVR model
svr = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr.fit(X_train, y_train)

# Predict
y_pred = svr.predict(X_test)

print("SVR Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. Effective in high dimensions
2. Works with non-linear data
3. Memory efficient

Disadvantages:
1. Slow on large datasets
2. Kernel selection is tricky
3. Hard to interpret
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is SVM?
Ans: A supervised ML algorithm that finds optimal hyperplane.

Q2. What is margin?
Ans: Distance between hyperplane and closest points.

Q3. What are support vectors?
Ans: Points closest to decision boundary.

Q4. What is kernel trick?
Ans: Mapping data to higher dimension.

Q5. Linear vs RBF kernel?
Ans:
- Linear → linearly separable data
- RBF → non-linear data

Q6. What is C parameter?
Ans: Controls regularization.

Q7. Is SVM sensitive to outliers?
Ans: Yes.

Q8. Does SVM need feature scaling?
Ans: Yes.

Q9. Can SVM handle multi-class?
Ans: Yes (One-vs-One).

Q10. SVM vs Logistic Regression?
Ans:
- SVM maximizes margin
- Logistic predicts probabilities
"""

print("\nDAY 10 SVM COMPLETED ✅")

