"""
=========================================
📘 Day 1 – SQL Basics (Theory)
File Name: Day1_SQL.py
=========================================

This file contains basic SQL concepts explained
using Python-style comments for easy understanding.
"""

# =================================================
# 1. What is SQL?
# =================================================
"""
SQL stands for Structured Query Language.

SQL is used to:
- Store data
- Retrieve data
- Update data
- Delete data

SQL works with relational databases.

Examples of SQL databases:
- MySQL
- PostgreSQL
- Oracle
- SQL Server

SQL is NOT a programming language.
It is a query language.
"""


# =================================================
# 2. What is a Database?
# =================================================
"""
A Database is an organized collection of data.

It stores data in the form of tables.
Each table has:
- Rows (records)
- Columns (fields)

Example:
Table: Students

| id | name  | age |
|----|-------|-----|
| 1  | Rahul | 20  |
| 2  | Anjali| 21  |

Benefits of Database:
- Fast data access
- Data security
- Data consistency
- Easy backup
"""


# =================================================
# 3. Types of SQL Commands
# =================================================
"""
SQL commands are divided into 5 main types:
"""

# ---- 1. DDL (Data Definition Language)
"""
Used to define database structure.

Examples:
- CREATE
- ALTER
- DROP
- TRUNCATE
"""

# ---- 2. DML (Data Manipulation Language)
"""
Used to manipulate data inside tables.

Examples:
- INSERT
- UPDATE
- DELETE
"""

# ---- 3. DQL (Data Query Language)
"""
Used to retrieve data from database.

Example:
- SELECT
"""

# ---- 4. DCL (Data Control Language)
"""
Used to control access to data.

Examples:
- GRANT
- REVOKE
"""

# ---- 5. TCL (Transaction Control Language)
"""
Used to manage transactions.

Examples:
- COMMIT
- ROLLBACK
- SAVEPOINT
"""


# =================================================
# 4. What is a Primary Key?
# =================================================
"""
Primary Key:
- Uniquely identifies each record in a table
- Cannot have duplicate values
- Cannot be NULL

Only ONE primary key is allowed per table.

Example:
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

Here, 'id' is the Primary Key.
"""


# =================================================
# 5. What is a Foreign Key?
# =================================================
"""
Foreign Key:
- Used to connect two tables
- Refers to the Primary Key of another table

Purpose:
- Maintain relationship between tables

Example:
Students Table:
id (Primary Key)

Marks Table:
student_id (Foreign Key)

CREATE TABLE marks (
    student_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
"""


# =================================================
# 6. What is UNIQUE Key?
# =================================================
"""
UNIQUE Key:
- Ensures all values in a column are different
- Can contain ONE NULL value
- Multiple UNIQUE keys allowed per table

Example:
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

Here, email must be unique.
"""


# =================================================
# 7. Difference between Primary Key and UNIQUE Key
# =================================================
"""
| Feature             | Primary Key        | UNIQUE Key          |
|--------------------|--------------------|---------------------|
| Duplicate values   | Not allowed        | Not allowed         |
| NULL values        | Not allowed        | One NULL allowed    |
| Number per table   | Only one           | Multiple allowed    |
| Main purpose       | Identify records   | Ensure uniqueness   |

Summary:
- Primary Key = Identity
- UNIQUE Key = Constraint
"""


# =================================================
# End of Day 1 SQL File
# =================================================
"""
✅ Day 1 SQL completed successfully!
"""

