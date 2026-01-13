"""
===========================================================
Day 3 : Statistics Fundamentals
Topic Covered:
1. Histogram and Skewness
2. Probability Density Function (PDF) and its Types
3. Covariance and Correlation
4. Central Limit Theorem (CLT)
===========================================================

Note:
This file focuses on CONCEPTS, FORMULAS, and INTUITION.
No advanced libraries are used.
-----------------------------------------------------------
"""

# =========================================================
# 1. HISTOGRAM AND SKEWNESS
# =========================================================

"""
HISTOGRAM:
-----------
A histogram is a graphical representation of data distribution.
It shows how frequently data values occur within fixed intervals (bins).

X-axis  -> Data values (class intervals)
Y-axis  -> Frequency (count)

Example:
Marks of students: [40, 50, 55, 60, 60, 70, 75, 80]

Histogram helps to understand:
- Shape of data
- Spread of data
- Skewness
"""

"""
SKEWNESS:
----------
Skewness tells us about the ASYMMETRY of data distribution.

Types of Skewness:

1. Symmetric Distribution
   Mean = Median = Mode

2. Positive Skewness (Right Skewed)
   Mean > Median > Mode
   Long tail on the RIGHT side

3. Negative Skewness (Left Skewed)
   Mean < Median < Mode
   Long tail on the LEFT side
"""

"""
Skewness Formula (Karl Pearson):

Skewness = (Mean - Mode) / Standard Deviation

OR

Skewness = 3 * (Mean - Median) / Standard Deviation
"""

# =========================================================
# 2. PROBABILITY DENSITY FUNCTION (PDF)
# =========================================================

"""
PROBABILITY DENSITY FUNCTION (PDF):
-----------------------------------
PDF is used for CONTINUOUS random variables.

Key Properties of PDF:
1. f(x) >= 0 for all x
2. Total area under curve = 1
"""

"""
Mathematical Representation:

P(a <= X <= b) = ∫[a to b] f(x) dx
"""

"""
TYPES OF PDF:
-------------

1. UNIFORM DISTRIBUTION:
------------------------
All outcomes are equally likely.

Formula:
f(x) = 1 / (b - a)   for a <= x <= b

Mean = (a + b) / 2
Variance = (b - a)^2 / 12
"""

"""
2. NORMAL DISTRIBUTION:
-----------------------
Most commonly used distribution.
Bell-shaped curve.

PDF Formula:

f(x) = (1 / (σ√(2π))) * e^(-(x - μ)^2 / (2σ^2))

Where:
μ = Mean
σ = Standard Deviation
"""

"""
3. EXPONENTIAL DISTRIBUTION:
----------------------------
Used to model time between events.

PDF Formula:
f(x) = λe^(-λx),  x >= 0

Mean = 1 / λ
Variance = 1 / λ^2
"""

# =========================================================
# 3. COVARIANCE AND CORRELATION
# =========================================================

"""
COVARIANCE:
-----------
Covariance measures how two variables move together.

Formula:
Cov(X, Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / n

Interpretation:
- Positive Covariance → variables increase together
- Negative Covariance → one increases, other decreases
- Zero Covariance → no linear relationship
"""

"""
Limitation of Covariance:
-------------------------
- Value depends on units
- Difficult to interpret magnitude
"""

"""
CORRELATION:
------------
Correlation standardizes covariance.

Formula:
Correlation (r) = Cov(X, Y) / (σx * σy)

Range:
-1 <= r <= 1

Interpretation:
r = +1 → Perfect positive correlation
r = -1 → Perfect negative correlation
r = 0  → No linear correlation
"""

"""
Difference Between Covariance and Correlation:
----------------------------------------------
Covariance → direction only
Correlation → direction + strength
"""

# =========================================================
# 4. CENTRAL LIMIT THEOREM (CLT)
# =========================================================

"""
CENTRAL LIMIT THEOREM:
---------------------
CLT states that:

For a sufficiently large sample size (n >= 30),
the sampling distribution of the sample mean
approaches a NORMAL distribution,
regardless of the population distribution.
"""

"""
Important Conditions:
---------------------
1. Samples must be independent
2. Sample size should be large
3. Population variance should be finite
"""

"""
Mathematical Representation:

Sample Mean (μx̄) = μ
Standard Error = σ / √n
"""

"""
Why CLT is Important?
--------------------
- Used in hypothesis testing
- Used in confidence intervals
- Foundation of inferential statistics
"""

"""
Real-Life Example:
------------------
Heights of students may not be normally distributed.
But the average height of samples will follow normal distribution.
"""

# =========================================================
# END OF DAY 3
# =========================================================

print("Day 3 Statistics Notes Loaded Successfully ✔")

