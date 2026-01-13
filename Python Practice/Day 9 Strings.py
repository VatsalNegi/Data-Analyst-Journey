# =====================================
# Day 2 - DSA String Problems (46 to 50)
# =====================================

# 46. Sort a String (Bubble Sort - DSA Style)
s = input("Enter a string to sort: ")

arr = []
for i in range(len(s)):
    arr.append(s[i])

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

sorted_str = ""
for i in range(len(arr)):
    sorted_str += arr[i]

print("Sorted String:", sorted_str)


# 47. Convert Characters to Opposite Case
s = input("\nEnter a string to change case: ")
result = ""

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        result += chr(ord(s[i]) - 32)
    elif 'A' <= s[i] <= 'Z':
        result += chr(ord(s[i]) + 32)
    else:
        result += s[i]

print("Opposite Case String:", result)


# 48. Check if One String is Subsequence of Another
s1 = input("\nEnter first string (small): ")
s2 = input("Enter second string (large): ")

i = 0
j = 0

while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        i += 1
    j += 1

if i == len(s1):
    print("Subsequence")
else:
    print("Not Subsequence")


# 49. Count Vowels, Consonants, Digits, Special Characters
s = input("\nEnter a string to analyze: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for i in range(len(s)):
    ch = s[i]

    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            vowels += 1
        else:
            consonants += 1

    elif '0' <= ch <= '9':
        digits += 1

    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)


# 50. Detect Capital Usage
word = input("\nEnter a word to check capital usage: ")

upper = 0
lower = 0

for i in range(len(word)):
    if 'A' <= word[i] <= 'Z':
        upper += 1
    elif 'a' <= word[i] <= 'z':
        lower += 1

if upper == len(word):
    print("Valid Capital Usage")
elif lower == len(word):
    print("Valid Capital Usage")
elif ('A' <= word[0] <= 'Z') and lower == len(word) - 1:
    print("Valid Capital Usage")
else:
    print("Invalid Capital Usage")
