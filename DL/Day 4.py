"""
=========================================
DAY 4 – BUILD ANN FROM SCRATCH
No TensorFlow, No PyTorch
Only Python + Math

Topics Covered:
1. ANN Structure
2. Forward Propagation
3. Backward Propagation
4. Weight Update
5. Training Loop
=========================================
"""

import math
import random

# ----------------------------------------
# ACTIVATION FUNCTION
# ----------------------------------------

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


# ----------------------------------------
# STEP 1: DEFINE INPUT AND OUTPUT
# Example: XOR Problem
# ----------------------------------------

inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

outputs = [
    [0],
    [1],
    [1],
    [0]
]


# ----------------------------------------
# STEP 2: INITIALIZE WEIGHTS RANDOMLY
# ----------------------------------------

# Input layer → Hidden layer
weights_input_hidden = [
    [random.uniform(-1, 1), random.uniform(-1, 1)],
    [random.uniform(-1, 1), random.uniform(-1, 1)]
]

# Hidden layer → Output layer
weights_hidden_output = [
    [random.uniform(-1, 1)],
    [random.uniform(-1, 1)]
]

# Bias
bias_hidden = [random.uniform(-1, 1), random.uniform(-1, 1)]
bias_output = [random.uniform(-1, 1)]

learning_rate = 0.5


# ----------------------------------------
# STEP 3: TRAINING LOOP
# ----------------------------------------

epochs = 10000

for epoch in range(epochs):

    total_error = 0

    for i in range(len(inputs)):

        # ----------------------------------------
        # FORWARD PROPAGATION
        # ----------------------------------------

        input_layer = inputs[i]

        # Hidden layer
        hidden_layer = []

        for j in range(2):
            sum_value = (
                input_layer[0] * weights_input_hidden[0][j] +
                input_layer[1] * weights_input_hidden[1][j] +
                bias_hidden[j]
            )
            hidden_layer.append(sigmoid(sum_value))

        # Output layer
        output_layer = []

        for j in range(1):
            sum_value = (
                hidden_layer[0] * weights_hidden_output[0][j] +
                hidden_layer[1] * weights_hidden_output[1][j] +
                bias_output[j]
            )
            output_layer.append(sigmoid(sum_value))

        predicted = output_layer[0]
        actual = outputs[i][0]

        # ----------------------------------------
        # ERROR CALCULATION
        # ----------------------------------------

        error = actual - predicted
        total_error += error ** 2


        # ----------------------------------------
        # BACKWARD PROPAGATION
        # ----------------------------------------

        # Output gradient
        d_predicted = error * sigmoid_derivative(predicted)

        # Hidden gradients
        hidden_gradients = []

        for j in range(2):
            gradient = d_predicted * weights_hidden_output[j][0] * sigmoid_derivative(hidden_layer[j])
            hidden_gradients.append(gradient)


        # ----------------------------------------
        # UPDATE WEIGHTS
        # ----------------------------------------

        # Hidden → Output weights
        for j in range(2):
            weights_hidden_output[j][0] += learning_rate * d_predicted * hidden_layer[j]

        bias_output[0] += learning_rate * d_predicted


        # Input → Hidden weights
        for j in range(2):
            weights_input_hidden[0][j] += learning_rate * hidden_gradients[j] * input_layer[0]
            weights_input_hidden[1][j] += learning_rate * hidden_gradients[j] * input_layer[1]

            bias_hidden[j] += learning_rate * hidden_gradients[j]


    # Print error every 1000 epochs
    if epoch % 1000 == 0:
        print("Epoch:", epoch, "Error:", total_error)



# ----------------------------------------
# STEP 4: TEST THE TRAINED NETWORK
# ----------------------------------------

print("\nTesting Neural Network:\n")

for i in range(len(inputs)):

    input_layer = inputs[i]

    hidden_layer = []

    for j in range(2):
        sum_value = (
            input_layer[0] * weights_input_hidden[0][j] +
            input_layer[1] * weights_input_hidden[1][j] +
            bias_hidden[j]
        )
        hidden_layer.append(sigmoid(sum_value))

    output_layer = []

    for j in range(1):
        sum_value = (
            hidden_layer[0] * weights_hidden_output[0][j] +
            hidden_layer[1] * weights_hidden_output[1][j] +
            bias_output[j]
        )
        output_layer.append(sigmoid(sum_value))

    print("Input:", input_layer, "Output:", output_layer[0])


# ----------------------------------------
# END OF DAY 4
# ----------------------------------------

