# ==========================================================
# Day 5 : Data Modelling and DAX with Power Pivot in Excel
# ==========================================================

# ----------------------------------------------------------
# 1. What is Power Pivot?
# ----------------------------------------------------------
# Power Pivot is an advanced data analysis tool in Excel.
#
# It is used for:
# - Creating data models
# - Connecting multiple tables
# - Performing advanced calculations
# - Handling large datasets
#
# Power Pivot is similar to database systems.

# Example:
# Table 1: Customers
# Table 2: Orders
# Table 3: Products
#
# Power Pivot can connect all these tables.

# ----------------------------------------------------------
# 2. What is Data Modelling?
# ----------------------------------------------------------
# Data modelling means creating relationships between tables.
#
# Instead of storing everything in one table,
# data is divided into multiple related tables.

# Example:

# Customers Table
# CustomerID | CustomerName
# 101        | Vatsal
# 102        | Rahul

# Orders Table
# OrderID | CustomerID | Amount
# 1       | 101        | 500
# 2       | 102        | 800

# CustomerID connects both tables.

# ----------------------------------------------------------
# 3. Why Data Modelling is Important?
# ----------------------------------------------------------
# Benefits:
# - Reduces data duplication
# - Improves performance
# - Makes analysis easier
# - Used in Power BI and databases

# ----------------------------------------------------------
# 4. Opening Power Pivot
# ----------------------------------------------------------
# Steps:
# 1. Open Excel
# 2. Go to Power Pivot tab
# 3. Click Manage

# This opens Power Pivot window.

# ----------------------------------------------------------
# 5. Adding Tables to Data Model
# ----------------------------------------------------------
# Steps:
# 1. Select table
# 2. Click "Add to Data Model"

# Multiple tables can be added.

# ----------------------------------------------------------
# 6. Creating Relationships Between Tables
# ----------------------------------------------------------
# Relationships connect tables using common column.

# Example:
# Customers.CustomerID → Orders.CustomerID

# Steps:
# 1. Go to Diagram View
# 2. Drag common column
# 3. Connect tables

# This creates relationship.

# ----------------------------------------------------------
# 7. What is DAX?
# ----------------------------------------------------------
# DAX = Data Analysis Expressions
#
# DAX is a formula language used in:
# - Power Pivot
# - Power BI

# Used for:
# - Calculations
# - Analysis
# - Creating measures

# ----------------------------------------------------------
# 8. Calculated Column
# ----------------------------------------------------------
# Calculated column creates new column.

# Example:
# Total Price = Quantity * Price

# DAX formula:
# = Quantity * Price

# Each row will calculate separately.

# ----------------------------------------------------------
# 9. Measures in DAX
# ----------------------------------------------------------
# Measures perform aggregate calculations.

# Example:
# Total Sales

# DAX formula:
# = SUM(Sales[Amount])

# Example:
# Average Sales
# = AVERAGE(Sales[Amount])

# ----------------------------------------------------------
# 10. Common DAX Functions
# ----------------------------------------------------------

# SUM:
# Adds values
# = SUM(Table[Column])

# COUNT:
# Counts rows
# = COUNT(Table[Column])

# AVERAGE:
# Finds average
# = AVERAGE(Table[Column])

# MAX:
# Finds maximum
# = MAX(Table[Column])

# MIN:
# Finds minimum
# = MIN(Table[Column])

# ----------------------------------------------------------
# 11. Example of DAX Measure
# ----------------------------------------------------------

# Total Sales:
# = SUM(Orders[Amount])

# Total Orders:
# = COUNT(Orders[OrderID])

# Average Sales:
# = AVERAGE(Orders[Amount])

# ----------------------------------------------------------
# 12. Diagram View in Power Pivot
# ----------------------------------------------------------
# Diagram view shows relationships visually.

# It looks like:
# Customers -------- Orders -------- Products

# Helps understand data structure.

# ----------------------------------------------------------
# 13. Benefits of Power Pivot
# ----------------------------------------------------------
# - Handles millions of rows
# - Fast calculations
# - Advanced analysis
# - Used in dashboards
# - Used in Power BI

# ----------------------------------------------------------
# 14. Real-Life Use Cases
# ----------------------------------------------------------
# - Sales analysis
# - Customer analysis
# - Business reporting
# - Dashboard creation
# - Financial analysis

# ----------------------------------------------------------
# 15. Interview Questions
# ----------------------------------------------------------

# Q: What is Power Pivot?
# Answer:
# Power Pivot is an Excel tool used for data modelling,
# relationships,
