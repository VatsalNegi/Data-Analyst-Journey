"""
========================================
Day 2: SQL Clauses, Operators & Aggregates
========================================

Topics Covered:
1. Clauses in SQL
2. Operators in SQL
3. Aggregate (Aggregation) Functions

Note:
This file contains SQL queries inside comments
for learning and practice purposes.
"""

# ---------------------------------------
# 1. CLAUSES IN SQL
# ---------------------------------------

"""
Clauses are used with SELECT statements
to filter, sort, and group data.
"""

# SAMPLE TABLE
"""
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    salary INT
);
"""

# INSERT SAMPLE DATA
"""
INSERT INTO employees VALUES
(1, 'Amit', 'IT', 40000),
(2, 'Riya', 'HR', 35000),
(3, 'Karan', 'IT', 50000),
(4, 'Neha', 'Sales', 30000);
"""

# ---------------------------------------
# WHERE CLAUSE
# ---------------------------------------

"""
Used to filter records based on conditions
"""

"""
SELECT * FROM employees
WHERE department = 'IT';
"""

"""
SELECT * FROM employees
WHERE salary > 40000;
"""

# ---------------------------------------
# ORDER BY CLAUSE
# ---------------------------------------

"""
Used to sort records (ASC / DESC)
"""

"""
SELECT * FROM employees
ORDER BY salary ASC;
"""

"""
SELECT * FROM employees
ORDER BY salary DESC;
"""

# ---------------------------------------
# LIMIT CLAUSE
# ---------------------------------------

"""
Used to limit number of records
"""

"""
SELECT * FROM employees
LIMIT 2;
"""

# ---------------------------------------
# DISTINCT CLAUSE
# ---------------------------------------

"""
Used to remove duplicate values
"""

"""
SELECT DISTINCT department FROM employees;
"""

# ---------------------------------------
# GROUP BY CLAUSE
# ---------------------------------------

"""
Used with aggregate functions
to group rows with same values
"""

"""
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
"""

# ---------------------------------------
# HAVING CLAUSE
# ---------------------------------------

"""
HAVING is used with GROUP BY
to apply conditions on groups
"""

"""
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 35000;
"""

# ---------------------------------------
# 2. OPERATORS IN SQL
# ---------------------------------------

"""
Operators are used to perform operations
on data values.
"""

# ---------------------------------------
# ARITHMETIC OPERATORS
# ---------------------------------------

"""
+   Addition
-   Subtraction
*   Multiplication
/   Division
"""

"""
SELECT emp_name, salary + 5000 AS bonus
FROM employees;
"""

# ---------------------------------------
# COMPARISON OPERATORS
# ---------------------------------------

"""
=    Equal
!=   Not Equal
>    Greater Than
<    Less Than
>=   Greater Than or Equal
<=   Less Than or Equal
"""

"""
SELECT * FROM employees
WHERE salary >= 40000;
"""

# ---------------------------------------
# LOGICAL OPERATORS
# ---------------------------------------

"""
AND
OR
NOT
"""

"""
SELECT * FROM employees
WHERE department = 'IT' AND salary > 45000;
"""

"""
SELECT * FROM employees
WHERE department = 'IT' OR department = 'HR';
"""

"""
SELECT * FROM employees
WHERE NOT department = 'Sales';
"""

# ---------------------------------------
# SPECIAL OPERATORS
# ---------------------------------------

# IN OPERATOR
"""
SELECT * FROM employees
WHERE department IN ('IT', 'HR');
"""

# BETWEEN OPERATOR
"""
SELECT * FROM employees
WHERE salary BETWEEN 30000 AND 45000;
"""

# LIKE OPERATOR
"""
SELECT * FROM employees
WHERE emp_name LIKE 'A%';
"""

# IS NULL
"""
SELECT * FROM employees
WHERE department IS NULL;
"""

# ---------------------------------------
# 3. AGGREGATE FUNCTIONS
# ---------------------------------------

"""
Aggregate functions perform calculations
on multiple rows and return a single value.
"""

# COUNT
"""
SELECT COUNT(*) FROM employees;
"""

# SUM
"""
SELECT SUM(salary) FROM employees;
"""

# AVG
"""
SELECT AVG(salary) FROM employees;
"""

# MIN
"""
SELECT MIN(salary) FROM employees;
"""

# MAX
"""
SELECT MAX(salary) FROM employees;
"""

# AGGREGATE WITH GROUP BY
"""
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
"""

# ---------------------------------------
# END OF DAY 2 
# ---------------------------------------

"""
Next Topics:
- String Functions
- ALTER with Examples
"""

