"""
=====================================================
STATISTICS – DAY 4
TOPIC: INFERENTIAL STATISTICS
=====================================================

This file covers:
1. Inferential Statistics
2. Point Estimate
3. Interval Estimate (Confidence Interval)
4. Hypothesis Testing
5. Null and Alternative Hypothesis
6. Significance Level (alpha)
7. p-value
8. Z-Test with numerical example

Language: Simple English
Style: Exam + Interview Friendly
=====================================================
"""

# --------------------------------------------------
# 1. INFERENTIAL STATISTICS
# --------------------------------------------------
"""
Inferential Statistics is used to make conclusions
about a population using sample data.

Example:
Population → All students in a university
Sample → 100 students selected randomly

We use sample data to:
- Estimate population parameters
- Test hypotheses
"""

print("1. Inferential Statistics")
print("Used to draw conclusions about population using sample data\n")


# --------------------------------------------------
# 2. POINT ESTIMATE
# --------------------------------------------------
"""
Point Estimate:
A single value used to estimate a population parameter.

Common Point Estimates:
- Sample Mean (x̄) → estimates Population Mean (μ)
- Sample Proportion → estimates Population Proportion
"""

sample_data = [50, 52, 54, 56, 58]

# Calculating sample mean manually (no inbuilt mean)
total = 0
for value in sample_data:
    total += value

sample_mean = total / len(sample_data)

print("2. Point Estimate")
print("Sample Data:", sample_data)
print("Point Estimate (Sample Mean):", sample_mean, "\n")


# --------------------------------------------------
# 3. INTERVAL ESTIMATE (CONFIDENCE INTERVAL)
# --------------------------------------------------
"""
Interval Estimate:
A range of values within which the population parameter lies.

Formula for Confidence Interval (Z-test):
CI = x̄ ± Z * (σ / √n)

Where:
x̄ = sample mean
Z = z-score (1.96 for 95% confidence)
σ = population standard deviation
n = sample size
"""

import math

x_bar = 100      # sample mean
sigma = 10       # population standard deviation
n = 25           # sample size
z = 1.96         # z value for 95% confidence

margin_of_error = z * (sigma / math.sqrt(n))

lower_limit = x_bar - margin_of_error
upper_limit = x_bar + margin_of_error

print("3. Interval Estimate (95% Confidence Interval)")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit, "\n")


# --------------------------------------------------
# 4. HYPOTHESIS TESTING
# --------------------------------------------------
"""
Hypothesis Testing is a process to make decisions
using data.

Steps:
1. State hypotheses
2. Choose significance level (α)
3. Calculate test statistic
4. Find p-value
5. Make decision
"""

print("4. Hypothesis Testing")
print("Used to test assumptions using sample data\n")


# --------------------------------------------------
# 5. NULL AND ALTERNATIVE HYPOTHESIS
# --------------------------------------------------
"""
Null Hypothesis (H0):
- Default assumption
- No effect or no difference

Alternative Hypothesis (H1 or Ha):
- Opposite of null hypothesis
- What we want to prove
"""

print("5. Null and Alternative Hypothesis")
print("H0: Population mean = 50")
print("H1: Population mean ≠ 50\n")


# --------------------------------------------------
# 6. SIGNIFICANCE LEVEL (ALPHA)
# --------------------------------------------------
"""
Significance Level (α):
- Probability of rejecting a true null hypothesis
- Common values: 0.05, 0.01
"""

alpha = 0.05

print("6. Significance Level")
print("Alpha (α):", alpha, "\n")


# --------------------------------------------------
# 7. P-VALUE
# --------------------------------------------------
"""
p-value:
- Probability of getting the observed result
  assuming null hypothesis is true

Decision Rule:
If p-value ≤ α → Reject H0
If p-value > α → Fail to reject H0
"""

p_value = 0.03

print("7. p-value")
print("p-value:", p_value)

if p_value <= alpha:
    print("Decision: Reject Null Hypothesis\n")
else:
    print("Decision: Fail to Reject Null Hypothesis\n")


# --------------------------------------------------
# 8. Z-TEST WITH EXAMPLE
# --------------------------------------------------
"""
Z-Test is used when:
- Population standard deviation is known
- Sample size ≥ 30 (or population is normal)

Z-Test Formula:
Z = (x̄ - μ) / (σ / √n)

Where:
x̄ = sample mean
μ = population mean
σ = population standard deviation
n = sample size
"""

# Given values
x_bar = 105     # sample mean
mu = 100        # population mean
sigma = 10      # population standard deviation
n = 36          # sample size

z_calculated = (x_bar - mu) / (sigma / math.sqrt(n))

print("8. Z-Test Example")
print("Calculated Z value:", z_calculated)

# Decision using critical value method
z_critical = 1.96   # for 95% confidence

if abs(z_calculated) > z_critical:
    print("Decision: Reject Null Hypothesis")
else:
    print("Decision: Fail to Reject Null Hypothesis")


"""
=====================================================
END OF DAY 4 – STATISTICS
=====================================================
"""

