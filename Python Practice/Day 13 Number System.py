# ==================================================
# Number_System.py  (Questions 65 – 70)
# PURE DSA STYLE – NO BUILT-IN BASE CONVERSIONS
# ==================================================

# --------------------------------------------------
# 65. Binary to Decimal
# --------------------------------------------------
binary = input("Enter binary number: ")
decimal = 0
power = 1

i = len(binary) - 1
while i >= 0:
    if binary[i] == '1':
        decimal = decimal + power
    power = power * 2
    i = i - 1

print("Binary to Decimal:", decimal)


# --------------------------------------------------
# 66. Decimal to Binary
# --------------------------------------------------
num = int(input("\nEnter decimal number: "))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        rem = num % 2
        binary = str(rem) + binary
        num = num // 2

print("Decimal to Binary:", binary)


# --------------------------------------------------
# 67. Octal to Decimal
# --------------------------------------------------
octal = input("\nEnter octal number: ")
decimal = 0
power = 1

i = len(octal) - 1
while i >= 0:
    digit = ord(octal[i]) - ord('0')
    decimal = decimal + digit * power
    power = power * 8
    i = i - 1

print("Octal to Decimal:", decimal)


# --------------------------------------------------
# 68. Decimal to Octal
# --------------------------------------------------
num = int(input("\nEnter decimal number: "))
octal = ""

if num == 0:
    octal = "0"
else:
    while num > 0:
        rem = num % 8
        octal = str(rem) + octal
        num = num // 8

print("Decimal to Octal:", octal)


# --------------------------------------------------
# 69. Binary to Octal
# (Binary → Decimal → Octal)
# --------------------------------------------------
binary = input("\nEnter binary number: ")
decimal = 0
power = 1

i = len(binary) - 1
while i >= 0:
    if binary[i] == '1':
        decimal = decimal + power
    power = power * 2
    i = i - 1

octal = ""
if decimal == 0:
    octal = "0"
else:
    while decimal > 0:
        rem = decimal % 8
        octal = str(rem) + octal
        decimal = decimal // 8

print("Binary to Octal:", octal)


# --------------------------------------------------
# 70. Hexadecimal to Decimal
# (Supports A–F and a–f)
# --------------------------------------------------
hex_num = input("\nEnter hexadecimal number: ")
decimal = 0
power = 1

i = len(hex_num) - 1
while i >= 0:
    ch = hex_num[i]

    if ch == 'A' or ch == 'a':
        value = 10
    elif ch == 'B' or ch == 'b':
        value = 11
    elif ch == 'C' or ch == 'c':
        value = 12
    elif ch == 'D' or ch == 'd':
        value = 13
    elif ch == 'E' or ch == 'e':
        value = 14
    elif ch == 'F' or ch == 'f':
        value = 15
    else:
        value = ord(ch) - ord('0')

    decimal = decimal + value * power
    power = power * 16
    i = i - 1

print("Hexadecimal to Decimal:", decimal)
