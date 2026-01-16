"""
=====================================================
STATISTICS – DAY 6
TOPICS:
1. Chi-Square Test
2. ANOVA (One-Way)
3. F-Test (Variance Test)
=====================================================

Language: Simple English
Style: Exam + Interview Friendly
=====================================================
"""

import math

# --------------------------------------------------
# 1. CHI-SQUARE TEST
# --------------------------------------------------
"""
Chi-Square Test is used for:
- Categorical data
- Testing relationship between two variables
- Testing goodness of fit

Formula:
χ² = Σ ( (O - E)² / E )

Where:
O = Observed frequency
E = Expected frequency
"""

observed = [50, 30, 20]
expected = [40, 40, 20]

chi_square = 0

for i in range(len(observed)):
    chi_square += ((observed[i] - expected[i]) ** 2) / expected[i]

print("1. Chi-Square Test")
print("Observed Frequencies:", observed)
print("Expected Frequencies:", expected)
print("Chi-Square Value:", chi_square)
print()


# --------------------------------------------------
# 2. ONE-WAY ANOVA
# --------------------------------------------------
"""
ANOVA (Analysis of Variance) is used to:
- Compare means of MORE THAN TWO groups
- Check if at least one group mean is different

Null Hypothesis (H0):
All group means are equal

Steps:
1. Calculate group means
2. Calculate overall mean
3. Calculate variance between groups
4. Calculate variance within groups
"""

group1 = [10, 12, 14]
group2 = [20, 22, 24]
group3 = [30, 32, 34]

groups = [group1, group2, group3]

# Step 1: Group means
group_means = []
for group in groups:
    total = 0
    for value in group:
        total += value
    group_means.append(total / len(group))

# Step 2: Overall mean
total_all = 0
count_all = 0

for group in groups:
    for value in group:
        total_all += value
        count_all += 1

overall_mean = total_all / count_all

# Step 3: Between-group variance (SSB)
SSB = 0
for i in range(len(groups)):
    SSB += len(groups[i]) * (group_means[i] - overall_mean) ** 2

# Step 4: Within-group variance (SSW)
SSW = 0
for i in range(len(groups)):
    for value in groups[i]:
        SSW += (value - group_means[i]) ** 2

print("2. One-Way ANOVA")
print("Group Means:", group_means)
print("Overall Mean:", overall_mean)
print("Between Group Variance (SSB):", SSB)
print("Within Group Variance (SSW):", SSW)
print()


# --------------------------------------------------
# 3. F-TEST (VARIANCE TEST)
# --------------------------------------------------
"""
F-Test is used to:
- Compare variances of two samples
- Check consistency or stability

Formula:
F = Larger Variance / Smaller Variance
"""

sample1 = [10, 12, 14, 16, 18]
sample2 = [11, 13, 15, 17, 19]

# Mean of sample 1
mean1 = sum(sample1) / len(sample1)

# Mean of sample 2
mean2 = sum(sample2) / len(sample2)

# Variance of sample 1
var1 = 0
for value in sample1:
    var1 += (value - mean1) ** 2
var1 = var1 / (len(sample1) - 1)

# Variance of sample 2
var2 = 0
for value in sample2:
    var2 += (value - mean2) ** 2
var2 = var2 / (len(sample2) - 1)

# F-statistic
F_value = max(var1, var2) / min(var1, var2)

print("3. F-Test")
print("Variance of Sample 1:", var1)
print("Variance of Sample 2:", var2)
print("F Value:", F_value)
print()


"""
=====================================================
SUMMARY – DAY 6
-----------------------------------------------------
Chi-Square Test → Categorical data
ANOVA           → Compare 3 or more means
F-Test          → Compare variances
=====================================================

END OF DAY 6 – STATISTICS
"""

