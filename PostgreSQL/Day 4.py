"""
========================================
Day 4: Many-to-Many, Views & Procedures
========================================

Topics Covered:
1. Many-to-Many Relationship
2. Junction (Bridge) Table
3. Views in SQL
4. Stored Procedures

Note:
All SQL queries are written inside comments
for learning and practice purposes.
"""

# ---------------------------------------
# 1. MANY-TO-MANY RELATIONSHIP
# ---------------------------------------

"""
Many-to-Many relationship means:
Multiple records in Table A are related
to multiple records in Table B.

Example:
- Students can enroll in many courses
- Courses can have many students
"""

# STUDENTS TABLE
"""
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);
"""

# COURSES TABLE
"""
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);
"""

# ---------------------------------------
# JUNCTION / BRIDGE TABLE
# ---------------------------------------

"""
Junction table breaks many-to-many
into two one-to-many relationships.
"""

"""
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
"""

# ---------------------------------------
# INSERT SAMPLE DATA
# ---------------------------------------

"""
INSERT INTO students VALUES
(1, 'Amit'),
(2, 'Riya');

INSERT INTO courses VALUES
(101, 'SQL'),
(102, 'Python');

INSERT INTO enrollments VALUES
(1, 1, 101),
(2, 1, 102),
(3, 2, 101);
"""

# ---------------------------------------
# FETCH DATA USING JOINS
# ---------------------------------------

"""
SELECT students.student_name, courses.course_name
FROM enrollments
INNER JOIN students
ON enrollments.student_id = students.student_id
INNER JOIN courses
ON enrollments.course_id = courses.course_id;
"""

# ---------------------------------------
# 2. VIEWS IN SQL
# ---------------------------------------

"""
A VIEW is a virtual table based on
the result of a SQL query.
It does not store data physically.
"""

# CREATE VIEW
"""
CREATE VIEW student_courses AS
SELECT students.student_name, courses.course_name
FROM enrollments
INNER JOIN students
ON enrollments.student_id = students.student_id
INNER JOIN courses
ON enrollments.course_id = courses.course_id;
"""

# USE VIEW
"""
SELECT * FROM student_courses;
"""

# UPDATE VIEW (Drop & Recreate)
"""
DROP VIEW student_courses;

CREATE VIEW student_courses AS
SELECT student_name
FROM students;
"""

# ---------------------------------------
# ADVANTAGES OF VIEWS
# ---------------------------------------

"""
1. Improves security
2. Simplifies complex queries
3. Provides data abstraction
"""

# ---------------------------------------
# 3. STORED PROCEDURES
# ---------------------------------------

"""
A stored procedure is a reusable
block of SQL code stored in the database.
"""

# SIMPLE PROCEDURE (PostgreSQL)
"""
CREATE OR REPLACE PROCEDURE get_all_students()
LANGUAGE SQL
AS $$
    SELECT * FROM students;
$$;
"""

# CALL PROCEDURE
"""
CALL get_all_students();
"""

# PROCEDURE WITH PARAMETER
"""
CREATE OR REPLACE PROCEDURE get_student_by_id(sid INT)
LANGUAGE SQL
AS $$
    SELECT * FROM students
    WHERE student_id = sid;
$$;
"""

# CALL PROCEDURE WITH ARGUMENT
"""
CALL get_student_by_id(1);
"""

# ---------------------------------------
# ADVANTAGES OF PROCEDURES
# ---------------------------------------

"""
1. Reusable code
2. Better performance
3. Reduced network traffic
4. Improved security
"""

# ---------------------------------------
# END OF DAY 4
# ---------------------------------------

"""
🎉 SQL COMPLETE!

You have covered:
- Basics to Advanced SQL
- Relationships & Joins
- Views & Procedures

Next Steps:
- SQL Interview Questions
- SQL Practice Problems
- Mini Project using SQL
"""

