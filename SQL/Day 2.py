"""
=========================================
📘 Day 2 – SQL Constraints & Joins
File Name: Day2_SQL.py
=========================================

This file covers SQL constraints, differences
between commands, and SQL joins.
"""

# =================================================
# 8. What is NOT NULL Constraint?
# =================================================
"""
NOT NULL constraint ensures that a column
cannot store NULL (empty) values.

Meaning:
- Every record must have a value in this column.

Example:
CREATE TABLE students (
    id INT,
    name VARCHAR(50) NOT NULL
);

Here, 'name' cannot be empty.
"""


# =================================================
# 9. What is DEFAULT Constraint?
# =================================================
"""
DEFAULT constraint assigns a default value
to a column if no value is provided.

Example:
CREATE TABLE users (
    country VARCHAR(50) DEFAULT 'India'
);

If country is not given, 'India' is stored automatically.
"""


# =================================================
# 10. Difference between DELETE, TRUNCATE, and DROP
# =================================================
"""
DELETE:
- Removes specific rows
- WHERE condition can be used
- Can be rolled back

Example:
DELETE FROM students WHERE id = 1;

TRUNCATE:
- Removes all rows
- WHERE not allowed
- Faster than DELETE
- Cannot be rolled back

Example:
TRUNCATE TABLE students;

DROP:
- Deletes entire table
- Structure + data removed permanently

Example:
DROP TABLE students;
"""


# =================================================
# 11. Difference between WHERE and HAVING
# =================================================
"""
WHERE:
- Used to filter rows
- Used with SELECT, UPDATE, DELETE
- Cannot be used with aggregate functions

Example:
SELECT * FROM students WHERE age > 20;

HAVING:
- Used to filter groups
- Used with GROUP BY
- Used with aggregate functions

Example:
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
"""


# =================================================
# 12. What are Joins in SQL?
# =================================================
"""
Joins are used to combine data from
two or more tables based on a related column.

Purpose:
- Fetch data spread across multiple tables
- Maintain data normalization

Common Join Types:
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- SELF JOIN
- CROSS JOIN
"""


# =================================================
# 13. What is INNER JOIN?
# =================================================
"""
INNER JOIN returns only matching records
from both tables.

Example:
SELECT students.name, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id;

Only common records are shown.
"""


# =================================================
# 14. What is LEFT JOIN?
# =================================================
"""
LEFT JOIN returns:
- All records from left table
- Matching records from right table
- NULL if no match exists

Example:
SELECT students.name, marks.marks
FROM students
LEFT JOIN marks
ON students.id = marks.student_id;
"""


# =================================================
# 15. What is RIGHT JOIN?
# =================================================
"""
RIGHT JOIN returns:
- All records from right table
- Matching records from left table
- NULL if no match exists

Example:
SELECT students.name, marks.marks
FROM students
RIGHT JOIN marks
ON students.id = marks.student_id;
"""


# =================================================
# 16. What is FULL JOIN?
# =================================================
"""
FULL JOIN returns:
- All records from both tables
- NULL where no match exists

Example:
SELECT students.name, marks.marks
FROM students
FULL JOIN marks
ON students.id = marks.student_id;
"""


# =================================================
# 17. What is SELF JOIN?
# =================================================
"""
SELF JOIN is a join where a table
is joined with itself.

Used when table has hierarchical data.

Example:
SELECT A.name AS Employee, B.name AS Manager
FROM employees A, employees B
WHERE A.manager_id = B.id;
"""


# =================================================
# 18. What is CROSS JOIN?
# =================================================
"""
CROSS JOIN returns Cartesian product.

Meaning:
- Every row of first table
  joins with every row of second table.

Example:
SELECT students.name, subjects.subject
FROM students
CROSS JOIN subjects;

If students = 3 rows and subjects = 4 rows
Result = 12 rows
"""


# =================================================
# End of Day 2 SQL File
# =================================================
"""
✅ Day 2 SQL completed successfully!
"""

