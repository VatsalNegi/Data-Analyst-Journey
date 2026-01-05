"""
Day 2: OOPS, File Handling & Multithreading
Author: Vatsal Negi
Goal: Strengthen core Python concepts used in real-world applications
"""

# ======================================================
# 1. OBJECT ORIENTED PROGRAMMING (OOPS)
# ======================================================

print("\n===== OOPS CONCEPTS =====")

# --------------------------
# Class & Object
# --------------------------

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

s1 = Student("Vatsal", 101)
s1.display()


# --------------------------
# Inheritance
# --------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"My name is {self.name}")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def details(self):
        print(f"Employee ID: {self.emp_id}")

emp = Employee("Vatsal", "DA102")
emp.intro()
emp.details()


# --------------------------
# Encapsulation
# --------------------------

class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
print("Balance:", account.get_balance())


# --------------------------
# Polymorphism
# --------------------------

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()


# ======================================================
# 2. FILE HANDLING
# ======================================================

print("\n===== FILE HANDLING =====")

# --------------------------
# Writing to a file
# --------------------------

with open("day2_notes.txt", "w") as file:
    file.write("Day 2 Python Learning\n")
    file.write("Topics: OOPS, File Handling, Multithreading\n")

print("File written successfully.")


# --------------------------
# Reading from a file
# --------------------------

with open("day2_notes.txt", "r") as file:
    content = file.read()

print("File Content:\n", content)


# --------------------------
# Appending to a file
# --------------------------

with open("day2_notes.txt", "a") as file:
    file.write("Progress: Good consistency maintained.\n")

print("File appended successfully.")


# ======================================================
# 3. EXCEPTION HANDLING (Real-world use)
# ======================================================

print("\n===== EXCEPTION HANDLING =====")

try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("Execution completed.")


# ======================================================
# 4. MULTI-THREADING
# ======================================================

print("\n===== MULTI-THREADING =====")

import threading
import time

# --------------------------
# Single thread task
# --------------------------

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {ch}")
        time.sleep(1)

# --------------------------
# Creating threads
# --------------------------

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Multithreading execution completed.")


# ======================================================
# 5. WHY THIS MATTERS (DATA ANALYST CONTEXT)
# ======================================================

"""
OOPS:
- Used in ML pipelines, reusable classes, clean architecture

File Handling:
- Reading CSV, logs, reports, datasets

Multithreading:
- Speed up data loading, ETL processes, background tasks
"""

print("\nDay 2 completed successfully 🚀")
