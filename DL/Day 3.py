"""
=========================================
DAY 3 – DEEP LEARNING
Topics Covered:
1. Loss Functions
2. Optimizers
=========================================
"""

# ----------------------------------------
# 1. LOSS FUNCTIONS
# ----------------------------------------

"""
Loss Function tells:
- How wrong the model prediction is
- Lower loss = better model

Loss is calculated during Forward Propagation
Loss is minimized using Backward Propagation
"""

# 1. Mean Squared Error (MSE)
def mean_squared_error(y_true, y_pred):
    return (y_true - y_pred) ** 2

# Example
y_true = 10
y_pred = 8
print("MSE Loss:", mean_squared_error(y_true, y_pred))


"""
Used in:
- Regression problems
Problem:
- Sensitive to outliers
"""

# 2. Mean Absolute Error (MAE)
def mean_absolute_error(y_true, y_pred):
    return abs(y_true - y_pred)

print("MAE Loss:", mean_absolute_error(y_true, y_pred))

"""
Used in:
- Regression
Less sensitive to outliers
"""

# 3. Binary Cross Entropy (Log Loss)
import math

def binary_cross_entropy(y_true, y_pred):
    y_pred = min(max(y_pred, 1e-15), 1 - 1e-15)  # avoid log(0)
    return -(y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred))

y_true = 1
y_pred = 0.7
print("Binary Cross Entropy Loss:", binary_cross_entropy(y_true, y_pred))

"""
Used in:
- Binary Classification
Example: Spam / Not Spam
"""

# 4. Categorical Cross Entropy
def categorical_cross_entropy(y_true, y_pred):
    return -sum(y_true[i] * math.log(y_pred[i]) for i in range(len(y_true)))

y_true = [0, 1, 0]
y_pred = [0.1, 0.8, 0.1]
print("Categorical Cross Entropy Loss:", categorical_cross_entropy(y_true, y_pred))

"""
Used in:
- Multi-class Classification
Example: Digit recognition (0–9)
"""


# ----------------------------------------
# 2. OPTIMIZERS
# ----------------------------------------

"""
Optimizers update weights to minimize loss.
They use gradients calculated by Backward Propagation.
"""

# 1. Gradient Descent
def gradient_descent(weight, gradient, learning_rate):
    return weight - learning_rate * gradient

weight = 0.5
gradient = 0.8
learning_rate = 0.1

new_weight = gradient_descent(weight, gradient, learning_rate)
print("Gradient Descent Updated Weight:", new_weight)

"""
Types of Gradient Descent:
- Batch Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-batch Gradient Descent
"""

# 2. Stochastic Gradient Descent (SGD)
"""
SGD updates weights for each data point.
Faster but noisy updates.
"""

# 3. Momentum Optimizer
"""
Momentum helps optimizer move faster
by adding previous gradient direction.
"""

velocity = 0
beta = 0.9

def momentum_optimizer(weight, gradient, velocity, lr):
    velocity = beta * velocity + lr * gradient
    weight = weight - velocity
    return weight, velocity

weight, velocity = momentum_optimizer(weight, gradient, velocity, learning_rate)
print("Momentum Updated Weight:", weight)

# 4. RMSProp Optimizer
"""
RMSProp reduces learning rate
for large gradients.
"""

cache = 0
beta = 0.9

def rmsprop(weight, gradient, cache, lr):
    cache = beta * cache + (1 - beta) * (gradient ** 2)
    weight = weight - lr * gradient / (math.sqrt(cache) + 1e-8)
    return weight, cache

weight, cache = rmsprop(weight, gradient, cache, learning_rate)
print("RMSProp Updated Weight:", weight)

# 5. Adam Optimizer (Most Popular)
"""
Adam = Momentum + RMSProp
Best default optimizer.
"""

m, v = 0, 0
beta1, beta2 = 0.9, 0.999

def adam(weight, gradient, m, v, lr, t):
    m = beta1 * m + (1 - beta1) * gradient
    v = beta2 * v + (1 - beta2) * (gradient ** 2)

    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)

    weight = weight - lr * m_hat / (math.sqrt(v_hat) + 1e-8)
    return weight, m, v

weight, m, v = adam(weight, gradient, m, v, learning_rate, t=1)
print("Adam Updated Weight:", weight)

"""
Optimizer Summary:
- GD       -> Slow
- SGD      -> Fast but noisy
- Momentum -> Faster convergence
- RMSProp  -> Adaptive learning rate
- Adam     -> Best choice for most problems
"""

# ----------------------------------------
# END OF DAY 3
# ----------------------------------------

