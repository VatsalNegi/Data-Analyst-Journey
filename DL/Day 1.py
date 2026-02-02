"""
=========================================
DAY 1 – DEEP LEARNING BASICS
Topics Covered:
1. Introduction to Deep Learning
2. Perceptron
3. Forward Propagation
=========================================
"""

# ----------------------------------------
# 1. INTRODUCTION TO DEEP LEARNING
# ----------------------------------------

"""
Deep Learning is a subset of Machine Learning.
It uses Artificial Neural Networks (ANNs) inspired by the human brain.

Machine Learning:
- Learns patterns from data
- Uses algorithms like Linear Regression, Decision Trees, etc.

Deep Learning:
- Uses multiple layers of neurons (Deep Neural Networks)
- Works very well with large data (images, text, audio, video)

Examples of Deep Learning:
- Face recognition
- Speech recognition (Google Assistant, Alexa)
- Self-driving cars
- Chatbots
"""

# Key Terms:
# Neuron       -> Basic unit of neural network
# Weight       -> Importance of input
# Bias         -> Extra value added to shift output
# Activation   -> Decides whether neuron should fire or not


# ----------------------------------------
# 2. PERCEPTRON
# ----------------------------------------

"""
Perceptron is the simplest neural network.
It is a single neuron model.

Structure of a Perceptron:
Inputs  ->  Weights  ->  Summation  ->  Activation Function  -> Output
"""

# Mathematical representation:
# y = w1*x1 + w2*x2 + ... + wn*xn + bias

# Example Perceptron Calculation:

# Inputs
x1 = 1
x2 = 0

# Weights
w1 = 0.7
w2 = 0.4

# Bias
bias = 0.3

# Weighted sum
z = (x1 * w1) + (x2 * w2) + bias

# Step Activation Function
def step_function(value):
    if value >= 0:
        return 1
    else:
        return 0

# Output
output = step_function(z)

print("Perceptron Output:", output)

"""
Limitations of Perceptron:
- Can solve only linear problems
- Cannot solve XOR problem
"""


# ----------------------------------------
# 3. FORWARD PROPAGATION
# ----------------------------------------

"""
Forward Propagation is the process where:
- Input data moves forward through the network
- Output is generated layer by layer

Steps in Forward Propagation:
1. Take input values
2. Multiply by weights
3. Add bias
4. Apply activation function
5. Pass output to next layer
"""

import math

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Example of Forward Propagation for ONE neuron

# Inputs
x1 = 2
x2 = 3

# Weights
w1 = 0.5
w2 = 0.8

# Bias
bias = 1

# Step 1 & 2: Weighted Sum
z = (x1 * w1) + (x2 * w2) + bias

# Step 3: Activation
output = sigmoid(z)

print("Forward Propagation Output:", output)

"""
Why Forward Propagation is important?
- Used during prediction
- Helps calculate loss
- Output is used for Backward Propagation
"""

# ----------------------------------------
# END OF DAY 1
# ----------------------------------------

