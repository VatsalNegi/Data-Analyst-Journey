"""
========================================
Day 1: Introduction to SQL (PostgreSQL)
========================================

Topics Covered:
1. What is SQL?
2. Why SQL is used?
3. Installing PostgreSQL (Windows & Mac)
4. pgAdmin overview
5. Basic CRUD Operations
6. Data Types in SQL
7. Constraints in SQL

Note:
This file is for LEARNING PURPOSES.
SQL commands are written inside multi-line comments.
"""

# ---------------------------------------
# 1. INTRODUCTION TO SQL
# ---------------------------------------

"""
SQL (Structured Query Language) is a standard language
used to store, retrieve, manipulate, and manage data
in a relational database.

Popular Databases using SQL:
- PostgreSQL
- MySQL
- Oracle
- SQL Server
- SQLite
"""

# ---------------------------------------
# 2. WHY SQL IS USED?
# ---------------------------------------

"""
SQL is used to:
- Create databases and tables
- Insert, update, delete data
- Retrieve data using queries
- Apply conditions and filters
- Maintain data integrity using constraints
"""

# ---------------------------------------
# 3. INSTALLING POSTGRESQL
# ---------------------------------------

"""
Windows Installation:
1. Download PostgreSQL from official website
2. Run installer
3. Set password for postgres user
4. Install pgAdmin
5. Complete installation

Mac Installation:
1. Download PostgreSQL
2. Follow installer steps
3. pgAdmin comes bundled
"""

# ---------------------------------------
# 4. IMPORTANT THINGS IN pgAdmin
# ---------------------------------------

"""
pgAdmin is a GUI tool for PostgreSQL.

Key Components:
- Server
- Databases
- Schemas
- Tables
- Query Tool

Query Tool is used to write and execute SQL queries.
"""

# ---------------------------------------
# 5. BASIC CRUD OPERATIONS
# ---------------------------------------

"""
CRUD stands for:
C → Create
R → Read
U → Update
D → Delete
"""

# CREATE DATABASE
"""
CREATE DATABASE company;
"""

# CREATE TABLE
"""
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT
);
"""

# INSERT DATA
"""
INSERT INTO employees VALUES (1, 'Amit', 30000);
INSERT INTO employees VALUES (2, 'Riya', 40000);
"""

# READ DATA
"""
SELECT * FROM employees;
"""

# UPDATE DATA
"""
UPDATE employees
SET salary = 45000
WHERE emp_id = 2;
"""

# DELETE DATA
"""
DELETE FROM employees
WHERE emp_id = 1;
"""

# ---------------------------------------
# 6. DATA TYPES IN SQL
# ---------------------------------------

"""
Common SQL Data Types:

INT         → Integer values
VARCHAR(n) → Variable-length string
CHAR(n)    → Fixed-length string
TEXT       → Long text
FLOAT      → Decimal numbers
BOOLEAN    → TRUE / FALSE
DATE       → Date values
"""

# Example Table with Data Types
"""
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    marks FLOAT,
    is_active BOOLEAN,
    dob DATE
);
"""

# ---------------------------------------
# 7. CONSTRAINTS IN SQL
# ---------------------------------------

"""
Constraints are rules applied to table columns
to ensure data accuracy and integrity.
"""

# TYPES OF CONSTRAINTS

"""
1. NOT NULL  → Column cannot have NULL value
2. UNIQUE   → All values must be unique
3. PRIMARY KEY → NOT NULL + UNIQUE
4. FOREIGN KEY → Links two tables
5. CHECK    → Condition-based restriction
6. DEFAULT  → Sets default value
"""

# NOT NULL
"""
CREATE TABLE users (
    user_id INT NOT NULL,
    username VARCHAR(50) NOT NULL
);
"""

# UNIQUE
"""
CREATE TABLE emails (
    email VARCHAR(100) UNIQUE
);
"""

# PRIMARY KEY
"""
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50)
);
"""

# DEFAULT
"""
CREATE TABLE orders (
    order_id INT,
    status VARCHAR(20) DEFAULT 'Pending'
);
"""

# CHECK
"""
CREATE TABLE employees_check (
    emp_id INT,
    age INT CHECK (age >= 18)
);
"""

# ---------------------------------------
# END OF DAY 1
# ---------------------------------------

"""
Next Day Topics:
- Exercise / Test
- Clauses in SQL
- Operators
- Aggregate Functions
"""

