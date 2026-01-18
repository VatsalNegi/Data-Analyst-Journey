"""
=========================================
📘 Day 4 – SQL Queries & Advanced Concepts
File Name: Day4_SQL.py
=========================================

This file covers:
- Subqueries
- Group By
- Interview-based SQL queries
- CTE and Temporary Tables
"""

# =================================================
# 26. What is Subquery?
# =================================================
"""
A Subquery is a query written inside
another SQL query.

It is executed first and its result
is used by the main query.

Example:
SELECT name
FROM employees
WHERE salary > (
    SELECT AVG(salary) FROM employees
);
"""


# =================================================
# 27. What is Nested Query?
# =================================================
"""
Nested Query means one SQL query
inside another SQL query.

Subquery and Nested Query mean the same thing.

Example:
SELECT * FROM students
WHERE marks > (
    SELECT marks FROM students WHERE name = 'Aman'
);
"""


# =================================================
# 28. What is Correlated Subquery?
# =================================================
"""
A Correlated Subquery depends on
the outer query for its execution.

It runs once for each row of outer query.

Example:
SELECT name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
"""


# =================================================
# 29. What is GROUP BY in SQL?
# =================================================
"""
GROUP BY groups rows that have
the same values in a column.

Used with aggregate functions:
- COUNT
- SUM
- AVG
- MIN
- MAX

Example:
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
"""


# =================================================
# 30. Difference between GROUP BY and ORDER BY
# =================================================
"""
GROUP BY:
- Groups rows
- Used with aggregate functions
- Reduces number of rows

ORDER BY:
- Sorts rows
- Used for display
- Does not reduce rows

Example:
GROUP BY department
ORDER BY salary DESC
"""


# =================================================
# 31. Use of LIMIT in SQL
# =================================================
"""
LIMIT restricts the number of rows
returned by a query.

Example:
SELECT * FROM employees
LIMIT 5;

Returns only first 5 records.
"""


# =================================================
# 32. Find Second Highest Salary in SQL
# =================================================
"""
Method 1: Using Subquery

SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary) FROM employees
);

Method 2: Using ORDER BY and LIMIT

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
"""


# =================================================
# 33. Find Duplicate Records in a Table
# =================================================
"""
Duplicates are records having
same values in a column.

Example:
Find duplicate emails

SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
"""


# =================================================
# 34. What is CTE (Common Table Expression)?
# =================================================
"""
CTE is a temporary result set
defined using WITH keyword.

Improves query readability.

Example:
WITH HighSalary AS (
    SELECT * FROM employees WHERE salary > 50000
)
SELECT * FROM HighSalary;
"""


# =================================================
# 35. What is Temporary Table?
# =================================================
"""
Temporary Table stores data temporarily.

- Exists only during session
- Automatically deleted

Example:
CREATE TEMPORARY TABLE temp_students (
    id INT,
    name VARCHAR(50)
);

Used for intermediate results.
"""


# =================================================
# End of Day 4 SQL File
# =================================================
"""
✅ Day 4 SQL completed successfully!
"""

