"""
===========================================================
DAY 11 – GRADIENT BOOSTING (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Gradient Boosting?
2. Why Gradient Boosting is needed?
3. Boosting vs Bagging
4. How Gradient Boosting Works
5. Loss Function Intuition
6. Gradient Boosting for Classification
7. Gradient Boosting for Regression
8. Important Hyperparameters
9. Advantages & Disadvantages
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS GRADIENT BOOSTING?
# =========================================================
"""
Gradient Boosting is an ENSEMBLE learning algorithm
that builds models sequentially.

Each new model tries to FIX the errors of the previous model.

Usually uses:
- Decision Trees (weak learners)
"""

# =========================================================
# 2. WHY GRADIENT BOOSTING IS NEEDED?
# =========================================================
"""
Problems with single models:
1. High bias
2. Underfitting

Gradient Boosting solves:
✔ Reduces bias
✔ Improves accuracy
✔ Learns complex patterns
"""

# =========================================================
# 3. BOOSTING VS BAGGING
# =========================================================
"""
Bagging (Random Forest):
- Models built independently
- Reduces variance

Boosting (Gradient Boosting):
- Models built sequentially
- Reduces bias
"""

# =========================================================
# 4. HOW GRADIENT BOOSTING WORKS
# =========================================================
"""
1. Train initial model
2. Calculate errors (residuals)
3. Train next model on residuals
4. Add predictions to previous model
5. Repeat
"""

# =========================================================
# 5. LOSS FUNCTION INTUITION
# =========================================================
"""
Gradient Boosting minimizes a loss function.

Common losses:
- Mean Squared Error (Regression)
- Log Loss (Classification)

Uses gradient descent concept.
"""

# =========================================================
# 6. GRADIENT BOOSTING – CLASSIFICATION
# =========================================================

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Binary classification
X = X[y != 2]
y = y[y != 2]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
gb_clf = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train
gb_clf.fit(X_train, y_train)

# Predict
y_pred = gb_clf.predict(X_test)

# Accuracy
print("Gradient Boosting Classification Accuracy:",
      accuracy_score(y_test, y_pred))

# =========================================================
# 7. GRADIENT BOOSTING – REGRESSION
# =========================================================

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Create regression dataset
X_reg, y_reg = make_regression(
    n_samples=200, n_features=1, noise=15, random_state=42
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# Create model
gb_reg = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train
gb_reg.fit(X_train, y_train)

# Predict
y_pred = gb_reg.predict(X_test)

print("Gradient Boosting Regression MSE:",
      mean_squared_error(y_test, y_pred))

# =========================================================
# 8. IMPORTANT HYPERPARAMETERS
# =========================================================
"""
n_estimators:
- Number of trees

learning_rate:
- Contribution of each tree

max_depth:
- Depth of individual trees

subsample:
- Fraction of samples for each tree
"""

# =========================================================
# 9. ADVANTAGES & DISADVANTAGES
# =========================================================
"""
Advantages:
1. High predictive accuracy
2. Handles complex patterns
3. Works well with structured data

Disadvantages:
1. Slow training
2. Sensitive to hyperparameters
3. Prone to overfitting
"""

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is Gradient Boosting?
Ans: Sequential ensemble algorithm that corrects errors.

Q2. Boosting vs Bagging?
Ans:
- Boosting reduces bias
- Bagging reduces variance

Q3. What is learning rate?
Ans: Step size of model updates.

Q4. What are weak learners?
Ans: Simple models like shallow trees.

Q5. Is Gradient Boosting prone to overfitting?
Ans: Yes, if not tuned properly.

Q6. Can Gradient Boosting handle non-linear data?
Ans: Yes.

Q7. Gradient Boosting vs Random Forest?
Ans:
- RF builds trees independently
- GB builds trees sequentially

Q8. Why is Gradient Boosting powerful?
Ans: Learns from mistakes.

Q9. Does it need feature scaling?
Ans: No.

Q10. Examples of Gradient Boosting?
Ans: XGBoost, LightGBM, CatBoost
"""

print("\nDAY 11 GRADIENT BOOSTING COMPLETED ✅")

