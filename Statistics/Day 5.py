"""
=====================================================
STATISTICS – DAY 5
TOPICS:
1. t-Test
2. Bayes' Theorem
3. Type I Error
4. Type II Error
=====================================================

Language: Simple English
Style: Exam + Interview Friendly
=====================================================
"""

import math

# --------------------------------------------------
# 1. t-TEST
# --------------------------------------------------
"""
t-Test is used when:
- Sample size is small (n < 30)
- Population standard deviation (σ) is UNKNOWN
- Data is approximately normally distributed

Types of t-test:
1. One Sample t-test
2. Independent Sample t-test
3. Paired Sample t-test

Here we demonstrate ONE SAMPLE t-test
"""

"""
Formula:
t = (x̄ - μ) / (s / √n)

Where:
x̄ = sample mean
μ = population mean
s = sample standard deviation
n = sample size
"""

sample_data = [48, 50, 52, 49, 51]

# Step 1: Calculate sample mean
total = 0
for value in sample_data:
    total += value

x_bar = total / len(sample_data)

# Step 2: Calculate sample standard deviation manually
variance_sum = 0
for value in sample_data:
    variance_sum += (value - x_bar) ** 2

s = math.sqrt(variance_sum / (len(sample_data) - 1))

# Given population mean
mu = 50
n = len(sample_data)

# Step 3: Calculate t value
t_value = (x_bar - mu) / (s / math.sqrt(n))

print("1. One Sample t-Test")
print("Sample Data:", sample_data)
print("Sample Mean:", x_bar)
print("Sample Standard Deviation:", s)
print("Calculated t-value:", t_value)
print()


# --------------------------------------------------
# 2. BAYES' THEOREM
# --------------------------------------------------
"""
Bayes' Theorem is used to find conditional probability.

Formula:
P(A|B) = [P(B|A) × P(A)] / P(B)

Where:
P(A|B) = Probability of A given B
P(B|A) = Probability of B given A
P(A) = Probability of A
P(B) = Probability of B
"""

# Given probabilities
P_A = 0.3       # Probability of A
P_B_given_A = 0.8
P_B = 0.5

# Applying Bayes' theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

print("2. Bayes' Theorem")
print("P(A):", P_A)
print("P(B|A):", P_B_given_A)
print("P(B):", P_B)
print("P(A|B):", P_A_given_B)
print()


# --------------------------------------------------
# 3. TYPE I ERROR
# --------------------------------------------------
"""
Type I Error:
- Rejecting a TRUE null hypothesis
- Also called FALSE POSITIVE

Probability of Type I Error = α (significance level)

Example:
Saying a medicine works when it actually does not
"""

alpha = 0.05

print("3. Type I Error")
print("Type I Error: Rejecting true Null Hypothesis")
print("Probability of Type I Error (α):", alpha)
print()


# --------------------------------------------------
# 4. TYPE II ERROR
# --------------------------------------------------
"""
Type II Error:
- Failing to reject a FALSE null hypothesis
- Also called FALSE NEGATIVE

Probability of Type II Error = β

Example:
Saying a medicine does not work when it actually works
"""

beta = 0.2

print("4. Type II Error")
print("Type II Error: Failing to reject false Null Hypothesis")
print("Probability of Type II Error (β):", beta)
print()


"""
=====================================================
SUMMARY:
- t-Test: Small sample, σ unknown
- Bayes' Theorem: Conditional probability
- Type I Error: False positive (α)
- Type II Error: False negative (β)
=====================================================

END OF DAY 5 – STATISTICS
"""
