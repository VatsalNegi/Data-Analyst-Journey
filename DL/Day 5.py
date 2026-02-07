"""
=========================================
DAY 5 – BUILD ANN USING TENSORFLOW/KERAS
Real-world Deep Learning Implementation

Topics Covered:
1. Import TensorFlow
2. Create Dataset
3. Build ANN Model
4. Compile Model
5. Train Model
6. Predict Output
=========================================
"""

# ----------------------------------------
# STEP 1: IMPORT LIBRARIES
# ----------------------------------------

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

print("TensorFlow Version:", tf.__version__)


# ----------------------------------------
# STEP 2: CREATE DATASET
# Example: XOR Problem
# ----------------------------------------

# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output data
y = np.array([
    [0],
    [1],
    [1],
    [0]
])


# ----------------------------------------
# STEP 3: BUILD ANN MODEL
# ----------------------------------------

model = keras.Sequential()

# Hidden layer (2 neurons)
model.add(layers.Dense(
    units=2,
    activation='relu',
    input_shape=(2,)
))

# Output layer (1 neuron)
model.add(layers.Dense(
    units=1,
    activation='sigmoid'
))


# ----------------------------------------
# STEP 4: COMPILE MODEL
# ----------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Show model structure
model.summary()


# ----------------------------------------
# STEP 5: TRAIN MODEL
# ----------------------------------------

model.fit(
    X,
    y,
    epochs=1000,
    verbose=1
)


# ----------------------------------------
# STEP 6: MAKE PREDICTIONS
# ----------------------------------------

print("\nPredictions:\n")

predictions = model.predict(X)

for i in range(len(X)):
    print("Input:", X[i], "Predicted Output:", predictions[i][0])


# ----------------------------------------
# STEP 7: TEST NEW DATA
# ----------------------------------------

new_data = np.array([[1, 0]])

prediction = model.predict(new_data)

print("\nNew Input:", new_data[0])
print("Prediction:", prediction[0][0])


# ----------------------------------------
# END OF DAY 5
# ----------------------------------------
