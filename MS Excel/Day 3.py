# ==================================================
# Day 3 : Excel Based Data Wrangling
# ==================================================

# ----------------------------------------------
# 1. What is Data Wrangling?
# ----------------------------------------------
# Data Wrangling means cleaning, organizing,
# and transforming raw data into useful data.
#
# In real life, data is often messy:
# - Missing values
# - Duplicate records
# - Wrong formats
# - Extra spaces
# - Inconsistent text
#
# Excel is widely used for basic data wrangling.

# ----------------------------------------------
# 2. Removing Duplicate Data
# ----------------------------------------------
# Duplicate data means repeated rows.
#
# Steps in Excel:
# 1. Select the data
# 2. Go to Data tab
# 3. Click "Remove Duplicates"
# 4. Choose columns
# 5. Click OK

# ----------------------------------------------
# 3. Handling Missing Values
# ----------------------------------------------
# Missing values are blank or empty cells.
#
# Common methods:
# - Delete rows with blanks
# - Replace blanks with 0
# - Replace blanks with average or text like "N/A"

# Example:
# =IF(A1="", "N/A", A1)

# ----------------------------------------------
# 4. TRIM Function (Remove Extra Spaces)
# ----------------------------------------------
# TRIM removes unwanted spaces from text.
#
# Example:
# =TRIM(A1)

# Useful when data is copied from websites or PDFs.

# ----------------------------------------------
# 5. Cleaning Text Data
# ----------------------------------------------

# UPPER:
# Converts text to uppercase
# Example:
# =UPPER(A1)

# LOWER:
# Converts text to lowercase
# Example:
# =LOWER(A1)

# PROPER:
# Capitalizes first letter of each word
# Example:
# =PROPER(A1)

# ----------------------------------------------
# 6. Find and Replace
# ----------------------------------------------
# Used to replace wrong or unwanted values.
#
# Shortcut:
# Ctrl + H
#
# Example:
# Replace "M" with "Male"
# Replace "F" with "Female"

# ----------------------------------------------
# 7. Text to Columns
# ----------------------------------------------
# Used to split data into multiple columns.
#
# Example:
# "John,Delhi,25" → Name | City | Age
#
# Steps:
# 1. Select column
# 2. Go to Data tab
# 3. Click "Text to Columns"
# 4. Choose delimiter (comma, space, etc.)

# ----------------------------------------------
# 8. Data Type Conversion
# ----------------------------------------------
# Sometimes numbers are stored as text.
#
# Ways to fix:
# - Convert to Number
# - Use VALUE() function
#
# Example:
# =VALUE(A1)

# ----------------------------------------------
# 9. Sorting Data
# ----------------------------------------------
# Sorting arranges data in order.
#
# Types:
# - Ascending (A to Z, Small to Large)
# - Descending (Z to A, Large to Small)

# Steps:
# 1. Select data
# 2. Go to Data tab
# 3. Click Sort

# ----------------------------------------------
# 10. Filtering Data
# ----------------------------------------------
# Filtering shows only required data.
#
# Example:
# Show students with marks > 60
#
# Steps:
# 1. Select data
# 2. Click Filter
# 3. Apply conditions

# ----------------------------------------------
# 11. Conditional Formatting
# ----------------------------------------------
# Highlights data based on conditions.
#
# Example:
# - Marks < 40 → Red
# - Marks > 75 → Green
#
# Used to quickly analyze data visually.

# ----------------------------------------------
# 12. Removing Errors
# ----------------------------------------------
# Excel errors may appear during wrangling.
#
# Common errors:
# #N/A, #VALUE!, #DIV/0!
#
# Example to handle error:
# =IFERROR(A1/B1, 0)

# ----------------------------------------------
# 13. Creating Clean Final Dataset
# ----------------------------------------------
# Final clean data should:
# - Have no duplicates
# - No missing values
# - Correct data types
# - Consistent text format
#
# Clean data is ready for:
# - Analysis
# - Visualization
# - Reporting
# - Machine Learning

# ----------------------------------------------
# 14. Real-Life Examples
# ----------------------------------------------
# - Cleaning student result data
# - Sales data preparation
# - Customer data cleaning
# - Survey data analysis

# ----------------------------------------------
# End of Day 3 : Excel Based Data Wrangling
# ----------------------------------------------

