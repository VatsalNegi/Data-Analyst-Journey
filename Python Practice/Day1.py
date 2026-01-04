"""
Python Practice – Numbers (DSA Basics)
Repository: Data_analyst0-Journey
Purpose: Logic building & interview preparation for Data Analyst role
"""

# --------------------------------------------------
# Question 1: Climbing Stairs
# --------------------------------------------------
# You can climb 1 or 2 steps at a time.
# Find number of distinct ways to reach the top.

def climb_stairs(n):
    if n <= 2:
        return n

    prev1 = 1  # ways to reach step 1
    prev2 = 2  # ways to reach step 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2


# --------------------------------------------------
# Question 2: Check Leap Year
# --------------------------------------------------
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# --------------------------------------------------
# Question 3: Prime Number
# --------------------------------------------------
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# --------------------------------------------------
# Question 4: Positive, Negative, Odd, Even, Zero
# --------------------------------------------------
def number_type(n):
    if n == 0:
        return "Zero"
    elif n > 0:
        if n % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    else:
        if n % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"


# --------------------------------------------------
# Question 5: All Divisors of a Natural Number
# --------------------------------------------------
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


# --------------------------------------------------
# MAIN DRIVER CODE (for testing)
# --------------------------------------------------
if __name__ == "__main__":

    print("----- Question 1: Climbing Stairs -----")
    steps = int(input("Enter number of steps: "))
    print("Number of ways:", climb_stairs(steps))

    print("\n----- Question 2: Leap Year -----")
    year = int(input("Enter year: "))
    if is_leap_year(year):
        print(year, "is a Leap Year")
    else:
        print(year, "is NOT a Leap Year")

    print("\n----- Question 3: Prime Number -----")
    num = int(input("Enter number: "))
    if is_prime(num):
        print("Prime Number")
    else:
        print("Not Prime")

    print("\n----- Question 4: Number Type -----")
    num = int(input("Enter number: "))
    print(number_type(num))

    print("\n----- Question 5: All Divisors -----")
    num = int(input("Enter number: "))
    print("Divisors:", find_divisors(num))
  
