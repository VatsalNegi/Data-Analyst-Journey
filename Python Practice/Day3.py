"""
Day 3 – Python Numbers Practice (DSA Based)
Repository: Data_analyst0-Journey
Focus: Logic Building for Data Analyst Role

Questions Covered:
11. Perfect Number
12. Armstrong Number
13. Roots of Quadratic Equation
15. Circular Permutations
17. Maximum Product of Three Numbers
18. Happy Number
"""

# --------------------------------------------------
# Question 11: Perfect Number
# --------------------------------------------------
def is_perfect_number(n):
    if n <= 0:
        return False

    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum == n


# --------------------------------------------------
# Question 12: Armstrong Number
# --------------------------------------------------
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


# --------------------------------------------------
# Question 13: Roots of Quadratic Equation
# --------------------------------------------------
def quadratic_roots(a, b, c):
    D = b * b - 4 * a * c

    if D > 0:
        root1 = (-b + (D ** 0.5)) / (2 * a)
        root2 = (-b - (D ** 0.5)) / (2 * a)
        return root1, root2

    elif D == 0:
        root = -b / (2 * a)
        return root, root

    else:
        real = -b / (2 * a)
        imag = ((-D) ** 0.5) / (2 * a)
        return (real, imag), (real, -imag)


# --------------------------------------------------
# Question 15: Circular Permutations (NO library)
# --------------------------------------------------
def circular_permutations(n):
    if n <= 0:
        return 0

    fact = 1
    for i in range(1, n):
        fact *= i

    return fact


# --------------------------------------------------
# Question 17: Maximum Product of Three Numbers (DSA)
# --------------------------------------------------
def max_product_of_three(arr):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product1 = max1 * max2 * max3
    product2 = min1 * min2 * max1

    return product1 if product1 > product2 else product2


# --------------------------------------------------
# Question 18: Happy Number
# --------------------------------------------------
def is_happy_number(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return n == 1


# --------------------------------------------------
# DRIVER CODE (TESTING)
# --------------------------------------------------
if __name__ == "__main__":

    print("Q11 Perfect Number:", is_perfect_number(6))
    print("Q12 Armstrong Number:", is_armstrong(153))
    print("Q13 Quadratic Roots:", quadratic_roots(1, -5, 6))
    print("Q15 Circular Permutations (n=4):", circular_permutations(4))
    print("Q17 Max Product:", max_product_of_three([-10, -10, 5, 2]))
    print("Q18 Happy Number:", is_happy_number(19))
