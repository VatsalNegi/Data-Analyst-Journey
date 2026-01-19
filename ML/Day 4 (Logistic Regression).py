"""
===========================================================
DAY 4 – LOGISTIC REGRESSION (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Logistic Regression?
2. Why not Linear Regression for Classification?
3. Types of Logistic Regression
4. Sigmoid Function
5. Cost Function (Log Loss)
6. Gradient Descent (Concept)
7. Logistic Regression From Scratch
8. Logistic Regression using sklearn
9. Evaluation Metrics
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS LOGISTIC REGRESSION?
# =========================================================
"""
Logistic Regression is a supervised machine learning algorithm
used for CLASSIFICATION problems.

It predicts probabilities and outputs values as:
- 0 (Negative class)
- 1 (Positive class)

Example:
- Email spam or not spam
- Pass or fail
- Disease present or not
"""

# =========================================================
# 2. WHY NOT LINEAR REGRESSION FOR CLASSIFICATION?
# =========================================================
"""
Problems with Linear Regression:
1. Output can be less than 0 or greater than 1
2. No probability interpretation
3. Sensitive to outliers

Solution:
➡ Use Logistic Regression with Sigmoid Function
"""

# =========================================================
# 3. TYPES OF LOGISTIC REGRESSION
# =========================================================
"""
1. Binary Logistic Regression
   - Two classes (0 or 1)

2. Multinomial Logistic Regression
   - More than two classes (Softmax)

3. Ordinal Logistic Regression
   - Ordered classes
"""

# =========================================================
# 4. SIGMOID FUNCTION
# =========================================================
"""
Sigmoid function converts any value into range (0,1)

Formula:
σ(z) = 1 / (1 + e^(-z))

z = mx + c
"""

import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# =========================================================
# 5. COST FUNCTION (LOG LOSS / BINARY CROSS ENTROPY)
# =========================================================
"""
Log Loss Formula:

Loss = -( y*log(ŷ) + (1-y)*log(1-ŷ) )

Lower loss = better model
"""

def log_loss(y, y_pred):
    loss = 0
    for i in range(len(y)):
        loss += -(y[i] * math.log(y_pred[i]) + (1 - y[i]) * math.log(1 - y_pred[i]))
    return loss / len(y)

# =========================================================
# 6. GRADIENT DESCENT (CONCEPT)
# =========================================================
"""
Gradient Descent updates weights to minimize log loss.

Steps:
1. Initialize weights
2. Predict output
3. Calculate error
4. Update weights
5. Repeat
"""

# =========================================================
# 7. LOGISTIC REGRESSION FROM SCRATCH
# =========================================================

# Sample dataset (Binary Classification)
# Example: Hours studied vs Pass(1)/Fail(0)

X = [1, 2, 3, 4, 5]
Y = [0, 0, 0, 1, 1]

# Initialize parameters
m = 0
c = 0
learning_rate = 0.1
epochs = 1000
n = len(X)

# Training using Gradient Descent
for _ in range(epochs):
    y_pred = []

    for i in range(n):
        z = m * X[i] + c
        y_pred.append(sigmoid(z))

    dm = 0
    dc = 0

    for i in range(n):
        dm += (y_pred[i] - Y[i]) * X[i]
        dc += (y_pred[i] - Y[i])

    dm = dm / n
    dc = dc / n

    m = m - learning_rate * dm
    c = c - learning_rate * dc

print("Slope (m):", m)
print("Intercept (c):", c)

# Prediction
def predict(x):
    z = m * x + c
    return 1 if sigmoid(z) >= 0.5 else 0

print("Prediction for X=2:", predict(2))
print("Prediction for X=5:", predict(5))

# =========================================================
# 8. LOGISTIC REGRESSION USING SKLEARN
# =========================================================

from sklearn.linear_model import LogisticRegression
import numpy as np

X_np = np.array(X).reshape(-1, 1)
Y_np = np.array(Y)

model = LogisticRegression()
model.fit(X_np, Y_np)

print("Sklearn Coefficient:", model.coef_)
print("Sklearn Intercept:", model.intercept_)

print("Prediction for X=3:", model.predict([[3]]))
print("Probability for X=3:", model.predict_proba([[3]]))

# =========================================================
# 9. EVALUATION METRICS
# =========================================================
"""
1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. Confusion Matrix
"""

from sklearn.metrics import accuracy_score, confusion_matrix

y_pred_sklearn = model.predict(X_np)

print("Accuracy:", accuracy_score(Y_np, y_pred_sklearn))
print("Confusion Matrix:\n", confusion_matrix(Y_np, y_pred_sklearn))

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is Logistic Regression?
Ans: Classification algorithm that predicts probabilities.

Q2. Why sigmoid function?
Ans: It maps values between 0 and 1.

Q3. Difference between Linear and Logistic Regression?
Ans:
- Linear → Continuous output
- Logistic → Categorical output

Q4. What is log loss?
Ans: Cost function for logistic regression.

Q5. What is decision boundary?
Ans: Line that separates classes.

Q6. Why threshold is 0.5?
Ans: Standard probability cutoff.

Q7. Can Logistic Regression be used for multi-class?
Ans: Yes, using Softmax.

Q8. Is Logistic Regression linear?
Ans: Linear in parameters, non-linear in output.

Q9. What happens with imbalanced data?
Ans: Accuracy becomes misleading.

Q10. Is Logistic Regression sensitive to outliers?
Ans: Yes.
"""

print("\nDAY 4 LOGISTIC REGRESSION COMPLETED ✅")

