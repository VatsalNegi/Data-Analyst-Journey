"""
===========================================================
DAY 1 – LINEAR REGRESSION (FULL THEORY + PRACTICAL)
===========================================================

This file covers:
1. What is Linear Regression?
2. Types of Linear Regression
3. Assumptions of Linear Regression
4. Mathematical Formula
5. Cost Function (MSE)
6. Gradient Descent (Concept)
7. Practical Implementation (From Scratch)
8. Practical Using sklearn
9. Evaluation Metrics
10. Interview Questions & Answers

===========================================================
"""

# =========================================================
# 1. WHAT IS LINEAR REGRESSION?
# =========================================================
"""
Linear Regression is a supervised machine learning algorithm
used to predict a continuous value.

Example:
- Predict house price based on area
- Predict salary based on years of experience

It finds the BEST FIT STRAIGHT LINE that describes the
relationship between input (X) and output (Y).
"""

# =========================================================
# 2. TYPES OF LINEAR REGRESSION
# =========================================================
"""
1. Simple Linear Regression
   - One independent variable
   - Example: Salary vs Experience

2. Multiple Linear Regression
   - More than one independent variable
   - Example: House price vs area, rooms, location
"""

# =========================================================
# 3. ASSUMPTIONS OF LINEAR REGRESSION
# =========================================================
"""
1. Linearity: Relationship between X and Y must be linear
2. Independence: Observations are independent
3. Homoscedasticity: Constant variance of errors
4. Normality: Errors should be normally distributed
5. No Multicollinearity: Independent variables not highly correlated
"""

# =========================================================
# 4. MATHEMATICAL FORMULA
# =========================================================
"""
Simple Linear Regression Equation:

y = mx + c

where:
m = slope (weight)
c = intercept
x = input
y = predicted output
"""

# =========================================================
# 5. COST FUNCTION (MEAN SQUARED ERROR)
# =========================================================
"""
Cost function tells how wrong our predictions are.

Mean Squared Error (MSE):

MSE = (1/n) * Σ(actual - predicted)^2
"""

def mean_squared_error(actual, predicted):
    n = len(actual)
    error = 0
    for i in range(n):
        error += (actual[i] - predicted[i]) ** 2
    return error / n


# =========================================================
# 6. GRADIENT DESCENT (CONCEPT)
# =========================================================
"""
Gradient Descent is an optimization algorithm
used to minimize the cost function.

Steps:
1. Start with random m and c
2. Calculate error
3. Update m and c
4. Repeat until error is minimum
"""

# =========================================================
# 7. LINEAR REGRESSION FROM SCRATCH
# =========================================================

# Sample dataset
X = [1, 2, 3, 4, 5]        # Experience
Y = [2, 4, 6, 8, 10]      # Salary (simple example)

# Initialize parameters
m = 0
c = 0
learning_rate = 0.01
epochs = 1000
n = len(X)

# Gradient Descent
for _ in range(epochs):
    y_pred = []
    for i in range(n):
        y_pred.append(m * X[i] + c)

    # Calculate gradients
    dm = 0
    dc = 0
    for i in range(n):
        dm += -2 * X[i] * (Y[i] - y_pred[i])
        dc += -2 * (Y[i] - y_pred[i])

    dm = dm / n
    dc = dc / n

    # Update parameters
    m = m - learning_rate * dm
    c = c - learning_rate * dc

print("Slope (m):", m)
print("Intercept (c):", c)

# =========================================================
# 8. LINEAR REGRESSION USING SKLEARN
# =========================================================
"""
sklearn is a machine learning library in Python.
"""

from sklearn.linear_model import LinearRegression
import numpy as np

X_np = np.array(X).reshape(-1, 1)
Y_np = np.array(Y)

model = LinearRegression()
model.fit(X_np, Y_np)

print("Sklearn Slope:", model.coef_)
print("Sklearn Intercept:", model.intercept_)

# Prediction
prediction = model.predict([[6]])
print("Predicted value for X=6:", prediction)

# =========================================================
# 9. EVALUATION METRICS
# =========================================================
"""
1. Mean Squared Error (MSE)
2. Root Mean Squared Error (RMSE)
3. R² Score (Coefficient of Determination)
"""

from sklearn.metrics import mean_squared_error, r2_score

y_pred_sklearn = model.predict(X_np)

print("MSE:", mean_squared_error(Y_np, y_pred_sklearn))
print("R2 Score:", r2_score(Y_np, y_pred_sklearn))

# =========================================================
# 10. INTERVIEW QUESTIONS & ANSWERS
# =========================================================
"""
Q1. What is Linear Regression?
Ans: A supervised ML algorithm used to predict continuous values.

Q2. Difference between Linear and Logistic Regression?
Ans:
- Linear: predicts continuous values
- Logistic: predicts categorical values

Q3. What is cost function?
Ans: A function that measures prediction error.

Q4. Why Mean Squared Error is used?
Ans: It penalizes large errors more and is differentiable.

Q5. What is Gradient Descent?
Ans: Optimization algorithm to minimize cost function.

Q6. What does R² score represent?
Ans: How well the model explains variance in data.

Q7. Can Linear Regression handle non-linear data?
Ans: No, unless features are transformed.

Q8. What happens if assumptions are violated?
Ans: Model accuracy decreases.

Q9. What is multicollinearity?
Ans: High correlation between independent variables.

Q10. Is Linear Regression sensitive to outliers?
Ans: Yes, very sensitive.
"""

print("\nDAY 1 LINEAR REGRESSION COMPLETED ✅")

