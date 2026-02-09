"""
=========================================
DAY 7 – CONVOLUTIONAL NEURAL NETWORK (CNN)
Topics Covered:
1. Introduction to CNN
2. How CNN Works
3. Understanding CNN Architecture
=========================================
"""

# ----------------------------------------
# 1. INTRODUCTION TO CNN
# ----------------------------------------

"""
CNN stands for Convolutional Neural Network.

CNN is a type of Deep Learning model specially designed for image data.

Normal ANN Problems with images:
- Too many parameters
- Cannot detect spatial features
- Poor performance on images

CNN solves these problems using:
- Filters (kernels)
- Feature maps
- Convolution operation

CNN can automatically detect:
- Edges
- Shapes
- Patterns
- Objects

Applications of CNN:
- Face recognition
- Image classification
- Object detection
- Medical image analysis
- Self-driving cars
"""

# Example: Image representation in numbers

image = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]
]

print("Example Image Matrix:", image)


# ----------------------------------------
# 2. HOW CNN WORKS
# ----------------------------------------

"""
CNN works by extracting features step by step.

Step 1: Convolution
- Apply filter on image
- Detect features like edges

Step 2: Activation (ReLU)
- Remove negative values
- Add non-linearity

Step 3: Pooling
- Reduce image size
- Keep important features

Step 4: Flatten
- Convert 2D data into 1D

Step 5: Fully Connected Layer
- Final prediction
"""

# Example: Simple convolution operation

import numpy as np

# Image (3x3)
image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Filter (2x2)
filter = np.array([
    [1, 0],
    [0, -1]
])

# Convolution output calculation
output = (
    image[0][0]*filter[0][0] +
    image[0][1]*filter[0][1] +
    image[1][0]*filter[1][0] +
    image[1][1]*filter[1][1]
)

print("Convolution Output:", output)


# ----------------------------------------
# 3. UNDERSTANDING CNN ARCHITECTURE
# ----------------------------------------

"""
Basic CNN Architecture:

Input Image
     ↓
Convolution Layer
     ↓
Activation Function (ReLU)
     ↓
Pooling Layer
     ↓
Flatten Layer
     ↓
Fully Connected Layer
     ↓
Output Layer


Example Architecture:

Input: 28x28 image
        ↓
Conv Layer (feature extraction)
        ↓
ReLU
        ↓
Pooling
        ↓
Flatten
        ↓
Dense Layer
        ↓
Output (Prediction)
"""

# Example using TensorFlow/Keras

import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()

# Convolution Layer
model.add(layers.Conv2D(
    filters=32,
    kernel_size=(3,3),
    activation='relu',
    input_shape=(28,28,1)
))

# Pooling Layer
model.add(layers.MaxPooling2D((2,2)))

# Flatten Layer
model.add(layers.Flatten())

# Dense Layer
model.add(layers.Dense(64, activation='relu'))

# Output Layer
model.add(layers.Dense(1, activation='sigmoid'))

# Show architecture
model.summary()


# ----------------------------------------
# WHY CNN IS POWERFUL
# ----------------------------------------

"""
CNN advantages:
- Automatic feature extraction
- Less parameters than ANN
- High accuracy on images
- Detect complex patterns

ANN vs CNN:

ANN:
Input → Dense → Output

CNN:
Input → Conv → Pool → Flatten → Dense → Output
"""


# ----------------------------------------
# END OF DAY 7
# ----------------------------------------
