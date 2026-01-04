"""
Day 1: Python MASTER Fundamentals
Author: Vatsal Negi

This file covers:
- Basic & Advanced Data Types
- Type Casting
- All Operators
- String Operations
- List / Tuple / Set / Dictionary (Deep)
- Conditional Statements
- Loops (basic + advanced)
- Comprehensions
- Functions (intro)
- Exception Handling (intro)
- Useful Built-in Functions
"""

print("\n========== PYTHON DAY 1 : MASTER BASICS ==========\n")

# =================================================
# 1. BASIC DATA TYPES
# =================================================

age = 21                          # int
height = 5.9                     # float
name = "Vatsal Negi"              # string
is_student = True                # boolean

print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)

print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))


# =================================================
# 2. STRING OPERATIONS (DETAILED)
# =================================================

print("\n--- STRING OPERATIONS ---")

message = "Data Analyst Journey"
print("Original String:", message)

print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Length:", len(message))
print("Replace:", message.replace("Journey", "Learning"))

# String slicing
print("Slice [0:4]:", message[0:4])
print("Slice [5:]:", message[5:])
print("Reverse String:", message[::-1])

# String formatting
role = "Data Analyst"
print(f"My role is {role}")


# =================================================
# 3. ADVANCED DATA TYPES
# =================================================

# ---------------- LIST ----------------
print("\n--- LIST OPERATIONS (DEEP) ---")

marks = [78, 85, 90, 92]
print("Original List:", marks)

marks.append(95)
marks.extend([88, 91])
marks.insert(1, 80)

print("After modifications:", marks)

marks.remove(85)
popped_value = marks.pop()
print("After remove & pop:", marks)
print("Popped value:", popped_value)

marks.sort()
print("Sorted List:", marks)

print("Max:", max(marks))
print("Min:", min(marks))
print("Sum:", sum(marks))


# ---------------- TUPLE ----------------
print("\n--- TUPLE OPERATIONS ---")

coordinates = (10, 20, 30, 40)
print("Tuple:", coordinates)
print("Index 1:", coordinates[1])
print("Count of 20:", coordinates.count(20))
print("Index of 30:", coordinates.index(30))


# ---------------- SET ----------------
print("\n--- SET OPERATIONS ---")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

set_a.add(10)
set_a.discard(2)
print("Updated Set A:", set_a)


# ---------------- DICTIONARY ----------------
print("\n--- DICTIONARY OPERATIONS (DEEP) ---")

student = {
    "name": "Vatsal",
    "course": "MCA",
    "semester": 3
}

print("Student Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["college"] = "TMU"
student.update({"semester": 4})

print("Updated Dictionary:", student)

# Looping dictionary
for key, value in student.items():
    print(key, "=>", value)


# =================================================
# 4. TYPE CASTING
# =================================================

print("\n--- TYPE CASTING ---")

num_str = "100"
num_int = int(num_str)
num_float = float(num_int)

print("String:", num_str, type(num_str))
print("Int:", num_int, type(num_int))
print("Float:", num_float, type(num_float))


# =================================================
# 5. OPERATORS (ALL TYPES)
# =================================================

print("\n--- OPERATORS ---")

a, b = 10, 3

# Arithmetic
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Comparison
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less or Equal:", a <= b)

# Logical
print("AND:", a > 5 and b < 5)
print("OR:", a > 20 or b < 5)
print("NOT:", not (a > 5))

# Assignment
x = 5
x += 3
print("Assignment Result:", x)

# Membership
print("In list:", 90 in marks)
print("Not in list:", 50 not in marks)


# =================================================
# 6. CONDITIONAL STATEMENTS
# =================================================

print("\n--- CONDITIONAL STATEMENTS ---")

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 86
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# =================================================
# 7. LOOPS (DETAILED)
# =================================================

print("\n--- FOR LOOP ---")
for i in range(1, 6):
    print(i)

print("\n--- WHILE LOOP ---")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\n--- BREAK & CONTINUE ---")
for i in range(1, 10):
    if i == 4:
        continue
    if i == 8:
        break
    print(i)

print("\n--- NESTED LOOP ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# =================================================
# 8. COMPREHENSIONS
# =================================================

print("\n--- COMPREHENSIONS ---")

squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

square_dict = {x: x**2 for x in range(1, 6)}

print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Square Dictionary:", square_dict)


# =================================================
# 9. FUNCTIONS (INTRO)
# =================================================

print("\n--- FUNCTIONS ---")

def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a + b

print(greet("Vatsal"))
print("Addition:", add(5, 7))


# =================================================
# 10. EXCEPTION HANDLING (INTRO)
# =================================================

print("\n--- EXCEPTION HANDLING ---")

try:
    num = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to int")
finally:
    print("Execution completed")


# =================================================
# 11. USEFUL BUILT-IN FUNCTIONS
# =================================================

print("\n--- BUILT-IN FUNCTIONS ---")

nums = [2, 4, 6, 8]

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("All:", all(nums))
print("Any:", any(nums))


print("\n========== DAY 1 MASTER PYTHON COMPLETED ==========\n")
