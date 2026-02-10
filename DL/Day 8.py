"""
=========================================
DAY 8 – CNN IMPORTANT COMPONENTS

Topics Covered:
1. Layers in CNN
2. Padding
3. Stride
4. Pooling
5. Max Pooling
=========================================
"""

# ----------------------------------------
# 1. LAYERS IN CNN
# ----------------------------------------

"""
CNN contains multiple layers. Each layer has a specific function.

Main Layers in CNN:

1. Convolution Layer
   - Extracts features from image
   - Detects edges, shapes, patterns

2. Activation Layer (ReLU)
   - Removes negative values
   - Adds non-linearity

3. Pooling Layer
   - Reduces image size
   - Keeps important information

4. Flatten Layer
   - Converts 2D → 1D

5. Dense Layer (Fully Connected)
   - Final prediction
"""

print("CNN Layers: Conv → ReLU → Pool → Flatten → Dense")


# ----------------------------------------
# 2. PADDING
# ----------------------------------------

"""
Padding means adding extra pixels around image border.

Why padding is used:
- Prevent image from shrinking
- Preserve important edge information

Types of Padding:

1. Valid Padding:
   No padding added
   Output size decreases

2. Same Padding:
   Padding added
   Output size remains same
"""

import numpy as np

# Example image
image = np.array([
    [1, 2],
    [3, 4]
])

# Same padding example
padded_image = np.pad(image, pad_width=1, mode='constant')

print("\nOriginal Image:\n", image)
print("\nPadded Image:\n", padded_image)


# ----------------------------------------
# 3. STRIDE
# ----------------------------------------

"""
Stride means how much the filter moves each step.

Stride = 1 → moves 1 pixel
Stride = 2 → moves 2 pixels

Higher stride:
- Smaller output
- Faster computation
"""

image = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

filter = np.array([
    [1,0],
    [0,-1]
])

# stride = 1 example
output_stride1 = (
    image[0][0]*filter[0][0] +
    image[0][1]*filter[0][1] +
    image[1][0]*filter[1][0] +
    image[1][1]*filter[1][1]
)

print("\nStride 1 Output:", output_stride1)


# ----------------------------------------
# 4. POOLING
# ----------------------------------------

"""
Pooling reduces feature map size.

Benefits:
- Reduces computation
- Prevents overfitting
- Keeps important features

Types:
- Max Pooling
- Average Pooling
"""

# ----------------------------------------
# 5. MAX POOLING
# ----------------------------------------

"""
Max Pooling selects maximum value from region.

Example:
Region:
[1 3]
[2 4]

Max value = 4
"""

feature_map = np.array([
    [1, 3],
    [2, 4]
])

max_value = np.max(feature_map)

print("\nMax Pooling Result:", max_value)


# ----------------------------------------
# CNN IMPLEMENTATION USING KERAS
# ----------------------------------------

import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()

# Convolution Layer with padding and stride
model.add(layers.Conv2D(
    filters=32,
    kernel_size=(3,3),
    strides=(1,1),
    padding='same',
    activation='relu',
    input_shape=(28,28,1)
))

# Max Pooling Layer
model.add(layers.MaxPooling2D(
    pool_size=(2,2),
    strides=(2,2)
))

# Flatten Layer
model.add(layers.Flatten())

# Dense Layer
model.add(layers.Dense(64, activation='relu'))

# Output Layer
model.add(layers.Dense(1, activation='sigmoid'))

# Show model summary
model.summary()


# ----------------------------------------
# SUMMARY
# ----------------------------------------

"""
Padding:
- Adds border pixels

Stride:
- Controls filter movement

Pooling:
- Reduces size

Max Pooling:
- Keeps strongest feature

CNN Flow:
Input → Conv → ReLU → Pool → Flatten → Dense → Output
"""

# ----------------------------------------
# END OF DAY 8
# ----------------------------------------
