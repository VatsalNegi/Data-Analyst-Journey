"""
=========================================
📘 Day 5 – SQL Advanced Functions & Indexing
File Name: Day5_SQL.py
=========================================

This file covers:
- Window Functions
- Ranking Functions
- CASE, COALESCE, NVL
- Indexing concepts
"""

# =================================================
# 36. What is Window Function in SQL?
# =================================================
"""
Window Functions perform calculations
across a set of rows related to the current row.

Important:
- They do NOT reduce rows
- Used with OVER() clause

Common Window Functions:
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- SUM() OVER()
- AVG() OVER()

Example:
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
"""


# =================================================
# 37. Difference between ROW_NUMBER(), RANK(), and DENSE_RANK()
# =================================================
"""
ROW_NUMBER():
- Assigns unique number
- No gaps

RANK():
- Same rank for same values
- Skips next rank

DENSE_RANK():
- Same rank for same values
- No gaps

Example (Salary Order):
Salary: 10000, 9000, 9000, 8000

ROW_NUMBER → 1, 2, 3, 4
RANK       → 1, 2, 2, 4
DENSE_RANK → 1, 2, 2, 3
"""


# =================================================
# 38. What is CASE Statement in SQL?
# =================================================
"""
CASE works like IF-ELSE condition.

Used to apply conditions inside queries.

Example:
SELECT name, salary,
CASE
    WHEN salary >= 50000 THEN 'High'
    WHEN salary >= 30000 THEN 'Medium'
    ELSE 'Low'
END AS salary_level
FROM employees;
"""


# =================================================
# 39. What is COALESCE in SQL?
# =================================================
"""
COALESCE returns the first
non-NULL value from a list.

Used to handle NULL values.

Example:
SELECT COALESCE(phone, 'Not Available')
FROM users;

If phone is NULL → returns 'Not Available'
"""


# =================================================
# 40. What is NVL Function in SQL?
# =================================================
"""
NVL replaces NULL with a specified value.

Mostly used in Oracle SQL.

Example:
SELECT NVL(salary, 0)
FROM employees;

If salary is NULL → returns 0
"""


# =================================================
# 41. What is Indexing in SQL?
# =================================================
"""
Indexing improves the speed
of data retrieval operations.

Indexes work like a book index.

Advantages:
- Faster SELECT queries

Disadvantages:
- Slower INSERT, UPDATE, DELETE
- Extra storage required
"""


# =================================================
# 42. What is Clustered Index?
# =================================================
"""
Clustered Index:
- Physically sorts data in table
- Only ONE clustered index allowed
- Table data stored in index order

Example:
Primary Key usually creates a clustered index.
"""


# =================================================
# 43. What is Non-Clustered Index?
# =================================================
"""
Non-Clustered Index:
- Does NOT change physical order
- Creates separate index structure
- Multiple allowed per table

Example:
Index on email column for fast search.
"""


# =================================================
# 44. Difference between Clustered and Non-Clustered Index
# =================================================
"""
Clustered Index:
- Data stored in index order
- One per table
- Faster for range queries

Non-Clustered Index:
- Separate index structure
- Multiple allowed
- Faster for search queries

Summary:
Clustered → Data sorted
Non-Clustered → Pointer based
"""


# =================================================
# End of Day 5 SQL File
# =================================================
"""
✅ Day 5 SQL completed successfully!
"""

