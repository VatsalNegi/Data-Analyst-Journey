"""
=========================================================
CALCULUS FOR MACHINE LEARNING – THEORY + EXAMPLES
Author: Vatsal Negi
File Name: Calculus.py
=========================================================

This file covers the core concepts of Calculus required for:
✔ Machine Learning
✔ Data Science
✔ AI
✔ Deep Learning

The file includes:
1. Introduction to Calculus
2. Limits
3. Derivatives
4. Rules of Differentiation
5. Partial Derivatives
6. Gradients
7. Applications of Derivatives
8. Integrals
9. Applications of Integrals

All concepts are explained with:
✔ Clear theory
✔ Mathematical meaning
✔ Python examples (SymPy)
=========================================================
"""

# --------------------------------------------------------
# IMPORT REQUIRED LIBRARY
# --------------------------------------------------------

import sympy as sp


# --------------------------------------------------------
# 1. INTRODUCTION TO CALCULUS
# --------------------------------------------------------

"""
CALCULUS:
Calculus is the branch of mathematics that studies change.

There are two main parts of calculus:
1. Differential Calculus  → Rate of change
2. Integral Calculus      → Accumulation / Area

Why calculus is important in Machine Learning?
- To minimize loss functions
- To update weights in models
- Used in Gradient Descent
"""


# --------------------------------------------------------
# 2. LIMITS
# --------------------------------------------------------

"""
LIMIT:
A limit tells us what value a function approaches when the input
gets closer to a certain point.

Mathematical notation:
lim (x → a) f(x)

Example:
lim (x → 0) sin(x)/x = 1
"""

x = sp.symbols('x')

limit_example = sp.limit(sp.sin(x)/x, x, 0)
print("Limit Example (sin(x)/x as x→0):", limit_example)


# --------------------------------------------------------
# 3. DERIVATIVES
# --------------------------------------------------------

"""
DERIVATIVE:
Derivative represents the rate of change of a function.

In Machine Learning:
Derivative tells us how the loss changes with respect to weights.

Mathematical notation:
f'(x) = d/dx (f(x))
"""

f = x**2
derivative_example = sp.diff(f, x)
print("Derivative of x^2:", derivative_example)


# --------------------------------------------------------
# 4. RULES OF DIFFERENTIATION
# --------------------------------------------------------

"""
Important differentiation rules:

1. Power Rule:
d/dx (x^n) = n*x^(n-1)

2. Constant Rule:
d/dx (c) = 0

3. Sum Rule:
d/dx (f(x) + g(x)) = f'(x) + g'(x)

4. Chain Rule:
Used when functions are inside functions
"""

expr = 3*x**3 + 5*x + 7
print("Expression:", expr)
print("Derivative:", sp.diff(expr, x))


# --------------------------------------------------------
# 5. PARTIAL DERIVATIVES
# --------------------------------------------------------

"""
PARTIAL DERIVATIVE:
Used when a function has more than one variable.

Very important in Machine Learning because:
Loss function depends on multiple parameters.

Notation:
∂f/∂x , ∂f/∂y
"""

x, y = sp.symbols('x y')
f_xy = x**2 + y**2 + x*y

partial_x = sp.diff(f_xy, x)
partial_y = sp.diff(f_xy, y)

print("Function:", f_xy)
print("Partial derivative w.r.t x:", partial_x)
print("Partial derivative w.r.t y:", partial_y)


# --------------------------------------------------------
# 6. GRADIENT
# --------------------------------------------------------

"""
GRADIENT:
Gradient is a vector of partial derivatives.

Gradient points in the direction of maximum increase.
In Gradient Descent, we move in the opposite direction.

Gradient of f(x, y) = [∂f/∂x , ∂f/∂y]
"""

gradient = [partial_x, partial_y]
print("Gradient Vector:", gradient)


# --------------------------------------------------------
# 7. APPLICATIONS OF DERIVATIVES
# --------------------------------------------------------

"""
Applications in ML:
1. Finding minimum of loss function
2. Gradient Descent optimization
3. Backpropagation in Neural Networks
"""

loss = (x - 3)**2
loss_derivative = sp.diff(loss, x)

print("Loss Function:", loss)
print("Derivative of Loss:", loss_derivative)


# --------------------------------------------------------
# 8. INTEGRALS
# --------------------------------------------------------

"""
INTEGRAL:
Integral is the reverse of derivative.

It represents:
✔ Area under curve
✔ Accumulated quantity

Two types:
1. Indefinite Integral
2. Definite Integral
"""

integral_example = sp.integrate(x**2, x)
print("Indefinite Integral of x^2:", integral_example)

definite_integral = sp.integrate(x, (x, 0, 5))
print("Definite Integral of x from 0 to 5:", definite_integral)


# --------------------------------------------------------
# 9. APPLICATIONS OF INTEGRALS
# --------------------------------------------------------

"""
Applications:
✔ Probability Density Functions (PDF)
✔ Expected value in statistics
✔ Area under curve
"""

pdf = x
area = sp.integrate(pdf, (x, 0, 1))
print("Area under PDF from 0 to 1:", area)


# --------------------------------------------------------
# END OF FILE
# --------------------------------------------------------

"""
=========================================================
SUMMARY:
✔ Limits explain behavior near a point
✔ Derivatives measure change
✔ Partial derivatives handle multiple variables
✔ Gradients optimize ML models
✔ Integrals calculate accumulation

This file builds a strong calculus foundation for:
Machine Learning | AI | Data Science
=========================================================
"""

