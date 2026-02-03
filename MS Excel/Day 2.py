# ============================================
# Day 2 : Excel Formulas & Functions
# ============================================

# --------------------------------------------
# 1. What is a Formula in Excel?
# --------------------------------------------
# A formula is an expression used to perform calculations.
# Every formula in Excel starts with an '=' sign.

# Example:
# =A1 + A2

# --------------------------------------------
# 2. What is a Function in Excel?
# --------------------------------------------
# A function is a predefined formula in Excel
# that performs a specific calculation.

# Syntax:
# =FUNCTION_NAME(arguments)

# Example:
# =SUM(A1:A5)

# --------------------------------------------
# 3. Basic Arithmetic Formulas
# --------------------------------------------

# Addition
# =A1 + A2

# Subtraction
# =A1 - A2

# Multiplication
# =A1 * A2

# Division
# =A1 / A2

# --------------------------------------------
# 4. Common Mathematical Functions
# --------------------------------------------

# SUM:
# Adds multiple values
# Example:
# =SUM(A1:A10)

# AVERAGE:
# Calculates average
# Example:
# =AVERAGE(A1:A10)

# MIN:
# Finds smallest value
# Example:
# =MIN(A1:A10)

# MAX:
# Finds largest value
# Example:
# =MAX(A1:A10)

# COUNT:
# Counts numeric cells
# Example:
# =COUNT(A1:A10)

# --------------------------------------------
# 5. Logical Functions
# --------------------------------------------

# IF Function:
# Performs logical test

# Syntax:
# =IF(condition, value_if_true, value_if_false)

# Example:
# =IF(A1 >= 40, "Pass", "Fail")

# AND Function:
# Returns TRUE if all conditions are true
# Example:
# =AND(A1 > 35, B1 > 35)

# OR Function:
# Returns TRUE if any condition is true
# Example:
# =OR(A1 > 35, B1 > 35)

# --------------------------------------------
# 6. Text Functions
# --------------------------------------------

# CONCAT / CONCATENATE:
# Joins text
# Example:
# =CONCAT(A1, " ", B1)

# LEFT:
# Extracts text from left
# Example:
# =LEFT(A1, 4)

# RIGHT:
# Extracts text from right
# Example:
# =RIGHT(A1, 2)

# LEN:
# Counts number of characters
# Example:
# =LEN(A1)

# --------------------------------------------
# 7. Date & Time Functions
# --------------------------------------------

# TODAY:
# Returns current date
# Example:
# =TODAY()

# NOW:
# Returns current date and time
# Example:
# =NOW()

# DAY:
# Extracts day from date
# Example:
# =DAY(A1)

# MONTH:
# Extracts month from date
# Example:
# =MONTH(A1)

# YEAR:
# Extracts year from date
# Example:
# =YEAR(A1)

# --------------------------------------------
# 8. Lookup & Reference Functions
# --------------------------------------------

# VLOOKUP:
# Searches value vertically

# Syntax:
# =VLOOKUP(lookup_value, table_array, col_index, [range_lookup])

# Example:
# =VLOOKUP(A2, A1:D10, 3, FALSE)

# HLOOKUP:
# Searches value horizontally
# Example:
# =HLOOKUP(A1, A1:D5, 2, FALSE)

# --------------------------------------------
# 9. Absolute, Relative & Mixed References
# --------------------------------------------

# Relative Reference:
# Changes when copied
# Example:
# =A1 + B1

# Absolute Reference:
# Does not change
# Example:
# =$A$1 + $B$1

# Mixed Reference:
# Partially fixed
# Example:
# =$A1 or A$1

# --------------------------------------------
# 10. Common Errors in Excel
# --------------------------------------------

# #DIV/0!   -> Division by zero
# #VALUE!   -> Wrong data type
# #NAME?    -> Incorrect function name
# #REF!     -> Invalid cell reference
# #N/A      -> Value not available

# --------------------------------------------
# 11. Real-Life Use Cases
# --------------------------------------------
# - Student result calculation
# - Salary computation
# - Sales analysis
# - Attendance evaluation
# - Financial calculations

# --------------------------------------------
# End of Day 2 : Excel Formulas & Functions
# --------------------------------------------

