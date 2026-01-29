"""
========================================
Day 3: String Functions, ALTER, CASE & JOINS
========================================

Topics Covered:
1. String Functions in SQL
2. ALTER TABLE with Examples
3. CASE Statement in SQL
4. Relationships in SQL
5. One-to-One Relationship
6. One-to-Many Relationship
7. JOINS in SQL

Note:
All SQL queries are written inside comments
for learning and practice purposes.
"""

# ---------------------------------------
# 1. STRING FUNCTIONS IN SQL
# ---------------------------------------

"""
String functions are used to perform
operations on text/string values.
"""

# SAMPLE TABLE
"""
CREATE TABLE users (
    user_id INT,
    name VARCHAR(50),
    email VARCHAR(100)
);
"""

# LENGTH()
"""
SELECT name, LENGTH(name) AS name_length
FROM users;
"""

# UPPER()
"""
SELECT UPPER(name) FROM users;
"""

# LOWER()
"""
SELECT LOWER(email) FROM users;
"""

# CONCAT()
"""
SELECT CONCAT(name, ' - ', email) AS user_info
FROM users;
"""

# SUBSTRING()
"""
SELECT SUBSTRING(email, 1, 5)
FROM users;
"""

# TRIM()
"""
SELECT TRIM('   Hello SQL   ');
"""

# ---------------------------------------
# 2. ALTER TABLE WITH EXAMPLES
# ---------------------------------------

"""
ALTER is used to modify an existing table.
"""

# ADD COLUMN
"""
ALTER TABLE users
ADD phone VARCHAR(15);
"""

# DROP COLUMN
"""
ALTER TABLE users
DROP COLUMN phone;
"""

# RENAME COLUMN
"""
ALTER TABLE users
RENAME COLUMN name TO full_name;
"""

# CHANGE DATA TYPE
"""
ALTER TABLE users
ALTER COLUMN email TYPE VARCHAR(150);
"""

# ---------------------------------------
# 3. CASE STATEMENT IN SQL
# ---------------------------------------

"""
CASE is used to apply conditional logic
inside SQL queries.
"""

# SAMPLE TABLE
"""
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT
);
"""

"""
SELECT emp_name,
CASE
    WHEN salary >= 50000 THEN 'High Salary'
    WHEN salary >= 30000 THEN 'Medium Salary'
    ELSE 'Low Salary'
END AS salary_status
FROM employees;
"""

# ---------------------------------------
# 4. RELATIONSHIPS IN SQL
# ---------------------------------------

"""
Relationship defines how tables are
connected to each other.
"""

"""
Types of Relationships:
1. One-to-One
2. One-to-Many
3. Many-to-Many (later)
"""

# ---------------------------------------
# 5. ONE-TO-ONE RELATIONSHIP
# ---------------------------------------

"""
One record in Table A is related to
one record in Table B.
"""

"""
CREATE TABLE person (
    person_id INT PRIMARY KEY,
    name VARCHAR(50)
);
"""

"""
CREATE TABLE passport (
    passport_id INT PRIMARY KEY,
    person_id INT UNIQUE,
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);
"""

# ---------------------------------------
# 6. ONE-TO-MANY RELATIONSHIP
# ---------------------------------------

"""
One record in Table A is related to
multiple records in Table B.
"""

"""
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);
"""

"""
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
"""

# ---------------------------------------
# 7. JOINS IN SQL
# ---------------------------------------

"""
JOIN is used to combine rows from
two or more tables based on a related column.
"""

# SAMPLE TABLES
"""
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(50)
);
"""

"""
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    amount INT
);
"""

# ---------------------------------------
# INNER JOIN
# ---------------------------------------

"""
Returns records that have matching values
in both tables.
"""

"""
SELECT customers.customer_name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
"""

# ---------------------------------------
# LEFT JOIN
# ---------------------------------------

"""
Returns all records from left table
and matching records from right table.
"""

"""
SELECT customers.customer_name, orders.amount
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
"""

# ---------------------------------------
# RIGHT JOIN
# ---------------------------------------

"""
Returns all records from right table
and matching records from left table.
"""

"""
SELECT customers.customer_name, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;
"""

# ---------------------------------------
# FULL JOIN
# ---------------------------------------

"""
Returns all records when there is a match
in either left or right table.
"""

"""
SELECT customers.customer_name, orders.amount
FROM customers
FULL JOIN orders
ON customers.customer_id = orders.customer_id;
"""

# ---------------------------------------
# END OF DAY 3 (Upto JOINS)
# ---------------------------------------

"""
Next Topics:
- Exercise 3 / Test 3
- Many-to-Many Relationship
- Views
- Procedures
"""

