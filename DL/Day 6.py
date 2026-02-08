"""
=========================================
DAY 6 – BLACK BOX vs WHITE BOX MODELS
Topics Covered:
1. White Box Models
2. Black Box Models
3. Differences
4. Examples in Python
5. When to use each
=========================================
"""

# ----------------------------------------
# 1. WHITE BOX MODELS
# ----------------------------------------

"""
White Box Models are models whose internal working is clearly visible
and understandable by humans.

We can see:
- How input is processed
- How output is calculated
- How decision is made

These models are transparent and explainable.
"""

# Example: Linear Regression

def linear_regression(x, w, b):
    return w * x + b

x = 5
w = 2
b = 1

output = linear_regression(x, w, b)
print("White Box Model Output:", output)

"""
We know exact formula:
y = wx + b

So it is a White Box Model.
"""

# Examples of White Box Models:
"""
Linear Regression
Logistic Regression
Decision Tree
K-Nearest Neighbors (KNN)
Naive Bayes
"""


# ----------------------------------------
# 2. BLACK BOX MODELS
# ----------------------------------------

"""
Black Box Models are models whose internal working is NOT clearly visible.

We know:
Input → Output

But we do NOT easily understand how decision is made internally.
"""

# Example: Neural Network

import math

def neuron(x, w, b):
    z = x * w + b
    return 1 / (1 + math.exp(-z))   # sigmoid

output = neuron(5, 2, 1)

print("Black Box Model Output:", output)

"""
We cannot easily explain:
Why neuron gave this exact output.

Because many layers, weights, and complex calculations exist.
"""

# Examples of Black Box Models:
"""
Artificial Neural Networks (ANN)
Deep Learning models
Random Forest
Gradient Boosting
Support Vector Machine (SVM)
"""


# ----------------------------------------
# 3. DIFFERENCE BETWEEN WHITE BOX AND BLACK BOX
# ----------------------------------------

"""
White Box Model:
- Easy to understand
- Transparent
- Explainable
- Less complex
- Less accurate sometimes

Black Box Model:
- Hard to understand
- Not transparent
- Not easily explainable
- More complex
- More accurate
"""


# ----------------------------------------
# 4. REAL LIFE EXAMPLES
# ----------------------------------------

"""
White Box Example:
Bank loan approval using Decision Tree
Bank can explain why loan was rejected.

Black Box Example:
Face recognition using Deep Learning
Hard to explain exact reason.
"""


# ----------------------------------------
# 5. WHEN TO USE WHICH
# ----------------------------------------

"""
Use White Box when:
- Explainability is important
- Medical applications
- Banking
- Government systems

Use Black Box when:
- Accuracy is more important
- Image recognition
- Speech recognition
- ChatGPT, AI assistants
"""


# ----------------------------------------
# 6. INTERVIEW QUESTIONS
# ----------------------------------------

"""
Q: What is White Box Model?
Answer:
A White Box Model is a model whose internal working is understandable.

Q: What is Black Box Model?
Answer:
A Black Box Model is a model whose internal working is not easily understandable.

Q: Is Neural Network Black Box or White Box?
Answer:
Black Box Model.

Q: Is Decision Tree Black Box or White Box?
Answer:
White Box Model.
"""


# ----------------------------------------
# END OF DAY 6
# ----------------------------------------
