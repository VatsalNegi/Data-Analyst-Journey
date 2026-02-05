# ==================================================
# Day 4 : Power Query Based Data Wrangling in Excel
# ==================================================

# --------------------------------------------------
# 1. What is Power Query?
# --------------------------------------------------
# Power Query is a tool in Excel used for:
# - Importing data
# - Cleaning data
# - Transforming data
# - Combining multiple data sources
#
# It is also called ETL tool:
# E = Extract
# T = Transform
# L = Load

# Power Query is better than manual cleaning because:
# - Faster
# - Automatic
# - Repeatable
# - Handles large data easily

# --------------------------------------------------
# 2. Opening Power Query
# --------------------------------------------------
# Steps:
# 1. Open Excel
# 2. Go to Data tab
# 3. Click "Get Data"
# 4. Choose source:
#    - Excel file
#    - CSV file
#    - Text file
#    - Database
#    - Web

# This opens Power Query Editor.

# --------------------------------------------------
# 3. Power Query Editor Interface
# --------------------------------------------------
# Important parts:

# Left side:
# Query list (shows loaded tables)

# Center:
# Data preview

# Right side:
# Applied steps (shows all transformations)

# Top:
# Transformation tools

# --------------------------------------------------
# 4. Removing Columns
# --------------------------------------------------
# Removes unwanted columns.

# Steps:
# Select column → Right click → Remove

# Example:
# Remove unnecessary ID column

# --------------------------------------------------
# 5. Renaming Columns
# --------------------------------------------------
# Steps:
# Double click column name → type new name

# Example:
# "Cust_Name" → "Customer Name"

# --------------------------------------------------
# 6. Changing Data Type
# --------------------------------------------------
# Data types:
# - Text
# - Number
# - Date
# - Boolean

# Steps:
# Select column → Click Data Type → Choose type

# Example:
# "Age" → Number
# "Date" → Date format

# --------------------------------------------------
# 7. Removing Duplicate Rows
# --------------------------------------------------
# Steps:
# Select column → Remove duplicates

# Useful for:
# Customer data
# Student records

# --------------------------------------------------
# 8. Removing Blank Rows
# --------------------------------------------------
# Steps:
# Filter column → Uncheck blanks

# OR

# Home → Remove Rows → Remove Blank Rows

# --------------------------------------------------
# 9. Splitting Columns
# --------------------------------------------------
# Used to divide data.

# Example:
# "John Smith" → First Name | Last Name

# Steps:
# Select column → Split Column → By delimiter

# --------------------------------------------------
# 10. Merging Columns
# --------------------------------------------------
# Combines multiple columns.

# Example:
# First Name + Last Name → Full Name

# Steps:
# Select columns → Merge Columns

# --------------------------------------------------
# 11. Filtering Data
# --------------------------------------------------
# Same as Excel filter.

# Example:
# Show only Sales > 5000

# Steps:
# Click filter icon → Apply condition

# --------------------------------------------------
# 12. Adding New Columns
# --------------------------------------------------
# You can create new columns.

# Example:
# Create Bonus column from Salary

# Steps:
# Add Column → Custom Column

# Example formula:
# = Salary * 0.10

# --------------------------------------------------
# 13. Sorting Data
# --------------------------------------------------
# Arrange data in order.

# Ascending or Descending

# Example:
# Sort Salary from highest to lowest

# --------------------------------------------------
# 14. Automatic Recording of Steps
# --------------------------------------------------
# Power Query records every step.

# This means:
# If new data comes,
# Power Query can automatically clean it again.

# This saves time.

# --------------------------------------------------
# 15. Loading Data Back to Excel
# --------------------------------------------------
# Steps:
# Click "Close & Load"

# Clean data will appear in Excel sheet.

# --------------------------------------------------
# 16. Real-Life Use Cases
# --------------------------------------------------
# - Cleaning sales data
# - Cleaning customer database
# - Preparing data for dashboard
# - Preparing data for Power BI
# - Preparing data for Machine Learning

# --------------------------------------------------
# 17. Why Power Query is Important for Data Analysts
# --------------------------------------------------
# Power Query is used in:
# - Excel
# - Power BI
# - Business Intelligence tools

# Interview Question:
# Q: Why use Power Query?
# Answer:
# Power Query is used to clean, transform,
# and automate data preparation efficiently.

# --------------------------------------------------
# End of Day 4 : Power Query Based Data Wrangling
# --------------------------------------------------

