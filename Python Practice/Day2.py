"""
Day 2 – Python Numbers Practice
Repository: Data_analyst0-Journey
Focus: DSA Basics for Data Analyst (Logic Building)
"""

# --------------------------------------------------
# Question 6: Convert Decimal to Hexadecimal
# --------------------------------------------------
def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    result = ""

    while n > 0:
        remainder = n % 16
        result = hex_digits[remainder] + result
        n = n // 16

    return result


# --------------------------------------------------
# Question 7: Check Perfect Square
# --------------------------------------------------
def is_perfect_square(n):
    if n < 0:
        return False

    root = int(n ** 0.5)
    return root * root == n


# --------------------------------------------------
# Question 8: Add Two Fractions
# --------------------------------------------------
def add_fractions(a, b, c, d):
    numerator = a * d + c * b
    denominator = b * d
    return numerator, denominator


# --------------------------------------------------
# Question 9: Add Digits (Digital Root)
# --------------------------------------------------
def add_digits(n):
    while n > 9:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n


# --------------------------------------------------
# Question 10: Replace all 0 with 5
# --------------------------------------------------
def replace_zero_with_five(n):
    result = 0
    place = 1

    while n > 0:
        digit = n % 10
        if digit == 0:
            digit = 5
        result += digit * place
        place *= 10
        n //= 10

    return result


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------
if __name__ == "__main__":

    print("Q6 Decimal to Hexadecimal:", decimal_to_hexadecimal(26))
    print("Q7 Perfect Square:", is_perfect_square(16))
    print("Q8 Add Fractions:", add_fractions(1, 2, 3, 4))
    print("Q9 Add Digits:", add_digits(38))
    print("Q10 Replace 0 with 5:", replace_zero_with_five(1020))
  
