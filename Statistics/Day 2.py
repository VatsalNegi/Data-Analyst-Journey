"""
Day 2: Statistics for Data Analysis (Extended & Detailed)
--------------------------------------------------------
This file focuses on NUMERICALS + PRACTICAL understanding
of statistics, which is very important for:

- Data Analyst Interviews
- Exploratory Data Analysis (EDA)
- Business Insights
- Data Cleaning Decisions

--------------------------------------------------------
Topics Covered:
1. Mean, Median, Mode (Detailed + Edge Cases)
2. Variance (Population vs Sample)
3. Standard Deviation (Interpretation)
4. Quartiles & Percentiles (Concept + Code)
5. Interquartile Range (IQR)
6. Outliers Detection (IQR Method)
7. Comparison: Mean vs Median
8. Real-world Data Analyst Use Cases
--------------------------------------------------------
"""

# =====================================================
# 1. MEAN (AVERAGE)
# =====================================================

"""
Mean is the arithmetic average of the data.

Formula:
Mean = (Sum of all observations) / (Total number of observations)

Mean is sensitive to outliers.
"""

data = [10, 20, 30, 40, 50]

mean_value = sum(data) / len(data)
print("Mean of data:", mean_value)

# Example with outlier
data_with_outlier = [10, 20, 30, 40, 500]
mean_with_outlier = sum(data_with_outlier) / len(data_with_outlier)

print("Mean with outlier:", mean_with_outlier)

"""
Observation:
- Mean increases drastically due to a single extreme value.
"""

# =====================================================
# 2. MEDIAN
# =====================================================

"""
Median is the middle value of sorted data.

Why Median is important:
- Robust to outliers
- Preferred for skewed data (income, salary, house prices)
"""

sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 0:
    median_value = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median_value = sorted_data[n//2]

print("Median of data:", median_value)

# Median with outlier
sorted_outlier_data = sorted(data_with_outlier)
n2 = len(sorted_outlier_data)

if n2 % 2 == 0:
    median_outlier = (sorted_outlier_data[n2//2 - 1] + sorted_outlier_data[n2//2]) / 2
else:
    median_outlier = sorted_outlier_data[n2//2]

print("Median with outlier:", median_outlier)

"""
Observation:
- Median remains stable even with extreme values.
"""

# =====================================================
# 3. MODE
# =====================================================

"""
Mode is the value that appears most frequently.

Types:
- Unimodal (one mode)
- Bimodal (two modes)
- Multimodal (more than two)
"""

data_mode = [5, 10, 10, 20, 30, 30]

frequency = {}
for value in data_mode:
    frequency[value] = frequency.get(value, 0) + 1

max_freq = max(frequency.values())
modes = [k for k, v in frequency.items() if v == max_freq]

print("Mode(s):", modes)

# =====================================================
# 4. VARIANCE
# =====================================================

"""
Variance measures how far each value is from the mean.

Population Variance Formula:
σ² = Σ(x - μ)² / N

Sample Variance Formula:
s² = Σ(x - x̄)² / (n - 1)

Sample variance uses (n - 1) to avoid underestimation.
"""

# Population Variance
mean = mean_value
squared_diff = [(x - mean) ** 2 for x in data]
population_variance = sum(squared_diff) / len(data)

print("Population Variance:", population_variance)

# Sample Variance
sample_variance = sum(squared_diff) / (len(data) - 1)
print("Sample Variance:", sample_variance)

# =====================================================
# 5. STANDARD DEVIATION
# =====================================================

"""
Standard Deviation is the square root of variance.

Interpretation:
- Small SD → data points are close to mean
- Large SD → data points are spread out
"""

population_std = population_variance ** 0.5
sample_std = sample_variance ** 0.5

print("Population Standard Deviation:", population_std)
print("Sample Standard Deviation:", sample_std)

# =====================================================
# 6. QUARTILES
# =====================================================

"""
Quartiles divide the dataset into 4 equal parts.

Q1 → 25th percentile
Q2 → 50th percentile (Median)
Q3 → 75th percentile
"""

quartile_data = [5, 7, 10, 15, 20, 25, 30, 35]
quartile_data.sort()

def percentile(data, p):
    """
    Simple percentile calculation.
    """
    index = (p / 100) * (len(data) - 1)
    return data[int(index)]

Q1 = percentile(quartile_data, 25)
Q2 = percentile(quartile_data, 50)
Q3 = percentile(quartile_data, 75)

print("Q1 (25th percentile):", Q1)
print("Q2 (Median):", Q2)
print("Q3 (75th percentile):", Q3)

# =====================================================
# 7. INTERQUARTILE RANGE (IQR)
# =====================================================

"""
IQR measures spread of the middle 50% of data.

Formula:
IQR = Q3 - Q1

Why IQR is important:
- Less affected by outliers
- Used in boxplots
"""

IQR = Q3 - Q1
print("Interquartile Range (IQR):", IQR)

# =====================================================
# 8. OUTLIERS DETECTION (IQR METHOD)
# =====================================================

"""
Outliers are extreme values that differ significantly
from most observations.

IQR Rule:
Lower Bound = Q1 - 1.5 * IQR
Upper Bound = Q3 + 1.5 * IQR
"""

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in quartile_data if x < lower_bound or x > upper_bound]

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Detected Outliers:", outliers)

# =====================================================
# 9. MEAN vs MEDIAN (IMPORTANT INTERVIEW CONCEPT)
# =====================================================

"""
When to use Mean:
- Data is symmetric
- No extreme values

When to use Median:
- Data is skewed
- Presence of outliers
"""

salary_data = [25000, 27000, 30000, 32000, 500000]

mean_salary = sum(salary_data) / len(salary_data)

sorted_salary = sorted(salary_data)
median_salary = sorted_salary[len(sorted_salary)//2]

print("Mean Salary:", mean_salary)
print("Median Salary:", median_salary)

"""
Observation:
- Mean is misleading
- Median represents typical salary
"""

# =====================================================
# 10. REAL-WORLD DATA ANALYST USE CASES
# =====================================================

"""
1. Mean & Median:
   - Salary analysis
   - House price analysis

2. Standard Deviation:
   - Risk analysis
   - Sales variability

3. Quartiles & IQR:
   - Detect outliers
   - Boxplot analysis

4. Outliers:
   - Fraud detection
   - Data cleaning decisions
"""

# =====================================================
# INTERVIEW QUICK REVISION
# =====================================================

"""
Key Interview Lines:
- "Median is preferred for skewed data."
- "IQR is more robust than range."
- "Standard deviation explains variability."
- "Outliers can heavily affect mean."

End of Day 2 Statistics (Extended)
"""
