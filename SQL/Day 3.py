"""
=========================================
📘 Day 3 – SQL Advanced Basics
File Name: Day3_SQL.py
=========================================

This file covers:
- UNION & UNION ALL
- Normalization (with types & examples)
- Denormalization
- CHAR vs VARCHAR
- SQL vs MySQL
- AUTO INCREMENT
"""

# =================================================
# 19. What is UNION and UNION ALL?
# =================================================
"""
UNION and UNION ALL combine results
of multiple SELECT queries.

Rules:
- Same number of columns
- Same data types
- Same order of columns

Example:
SELECT name FROM students
UNION
SELECT name FROM teachers;
"""


# =================================================
# 20. Difference between UNION and UNION ALL
# =================================================
"""
UNION:
- Removes duplicate values
- Slower

UNION ALL:
- Keeps duplicate values
- Faster
"""


# =================================================
# 21. What is Normalization?
# =================================================
"""
Normalization is a process of organizing data
to reduce duplication and improve data integrity.

Main goals:
- Remove redundant data
- Avoid update anomalies
- Make database efficient
"""


# =================================================
# Types of Normalization
# =================================================

# -------------------------
# First Normal Form (1NF)
# -------------------------
"""
Rules of 1NF:
- Each column must contain atomic (single) values
- No multiple values in one column

❌ Before 1NF:
Student Table:
| id | name | subjects        |
|----|------|-----------------|
| 1  | Ravi | Math, Science   |

✅ After 1NF:
| id | name | subject  |
|----|------|----------|
| 1  | Ravi | Math     |
| 1  | Ravi | Science  |
"""


# -------------------------
# Second Normal Form (2NF)
# -------------------------
"""
Rules of 2NF:
- Must be in 1NF
- No partial dependency
- Non-key attributes must depend on full primary key

❌ Before 2NF:
Enrollment Table (Composite Key: student_id + course_id)

| student_id | course_id | student_name | course_fee |
|------------|-----------|--------------|------------|
| 1          | C1        | Aman         | 5000       |

Problem:
- student_name depends only on student_id
- course_fee depends only on course_id

✅ After 2NF:

Student Table:
| student_id | student_name |

Course Table:
| course_id | course_fee |

Enrollment Table:
| student_id | course_id |
"""


# -------------------------
# Third Normal Form (3NF)
# -------------------------
"""
Rules of 3NF:
- Must be in 2NF
- No transitive dependency
- Non-key columns should not depend on other non-key columns

❌ Before 3NF:
Employee Table:

| emp_id | emp_name | dept_id | dept_name |
|--------|----------|---------|-----------|

Problem:
- dept_name depends on dept_id (not directly on emp_id)

✅ After 3NF:

Employee Table:
| emp_id | emp_name | dept_id |

Department Table:
| dept_id | dept_name |
"""


# =================================================
# 22. What is Denormalization?
# =================================================
"""
Denormalization is the opposite of normalization.

It adds duplicate data intentionally
to improve performance.

Used in:
- Data warehouses
- Reporting systems

Example:
Merging Employee and Department tables
to avoid JOIN operations.
"""


# =================================================
# 23. Difference between CHAR and VARCHAR
# =================================================
"""
CHAR:
- Fixed length
- Faster
- Wastes space

VARCHAR:
- Variable length
- Saves space
- Slightly slower

Example:
CHAR(10) -> Uses 10 characters always
VARCHAR(10) -> Uses required characters only
"""


# =================================================
# 24. Difference between SQL and MySQL
# =================================================
"""
SQL:
- Query language
- Used to communicate with databases

MySQL:
- Database software
- Uses SQL language
"""


# =================================================
# 25. What is AUTO INCREMENT?
# =================================================
"""
AUTO INCREMENT automatically generates
unique numbers for a column.

Example:
CREATE TABLE students (
    id INT AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

Records:
1 → Aman
2 → Riya
3 → Rahul
"""


# =================================================
# End of Day 3 SQL File
# =================================================
"""
✅ Day 3 SQL completed successfully!
"""

