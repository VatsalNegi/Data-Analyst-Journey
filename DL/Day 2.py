"""
=========================================
DAY 2 – DEEP LEARNING
Topics Covered:
1. Backward Propagation
2. Vanishing Gradient Problem
3. Activation Functions
=========================================
"""

# ----------------------------------------
# 1. BACKWARD PROPAGATION
# ----------------------------------------

"""
Backward Propagation is the learning process of a neural network.

After Forward Propagation:
- We get predicted output
- We compare it with actual output
- We calculate error (loss)
- We update weights to reduce error

Backward Propagation moves from:
Output Layer  --->  Hidden Layer  --->  Input Layer
"""

# Mean Squared Error (Loss Function)
def mean_squared_error(y_true, y_pred):
    return (y_true - y_pred) ** 2

# Example values
y_true = 1        # actual output
y_pred = 0.6      # predicted output

# Loss
loss = mean_squared_error(y_true, y_pred)
print("Loss:", loss)

"""
Steps of Backward Propagation:
1. Calculate loss
2. Find gradient (partial derivative)
3. Update weights using Gradient Descent
"""

# Gradient Descent Weight Update
learning_rate = 0.1
weight = 0.5
gradient = -0.8   # example gradient value

# New weight calculation
new_weight = weight - learning_rate * gradient
print("Updated Weight:", new_weight)


# ----------------------------------------
# 2. VANISHING GRADIENT PROBLEM
# ----------------------------------------

"""
Vanishing Gradient Problem occurs when:
- Gradients become very small
- Weights update very slowly
- Deep networks stop learning

Mostly happens when:
- Using Sigmoid or Tanh activation
- Network has many layers
"""

# Example of vanishing gradient using sigmoid derivative
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Large input value
x = 10
grad = sigmoid_derivative(x)
print("Sigmoid Derivative (Vanishing Gradient Example):", grad)

"""
Why is this a problem?
- Early layers learn very slowly
- Model accuracy does not improve

Solutions:
- Use ReLU activation
- Proper weight initialization
- Batch Normalization
- Residual connections
"""


# ----------------------------------------
# 3. ACTIVATION FUNCTIONS
# ----------------------------------------

"""
Activation Functions decide whether a neuron should activate or not.
They add non-linearity to the network.
"""

# 1. Step Function
def step(x):
    return 1 if x >= 0 else 0

# 2. Sigmoid Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# 3. Tanh Function
def tanh(x):
    return math.tanh(x)

# 4. ReLU Function
def relu(x):
    return max(0, x)

# 5. Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x

# Testing activation functions
x = -2
print("Step:", step(x))
print("Sigmoid:", sigmoid(x))
print("Tanh:", tanh(x))
print("ReLU:", relu(x))
print("Leaky ReLU:", leaky_relu(x))

"""
Comparison Summary:
- Step      -> Not used in deep networks
- Sigmoid   -> Output between 0 and 1 (vanishing gradient)
- Tanh      -> Output between -1 and 1
- ReLU      -> Most popular, avoids vanishing gradient
- LeakyReLU -> Fixes dead neuron problem
"""

# ----------------------------------------
# END OF DAY 2
# ----------------------------------------

