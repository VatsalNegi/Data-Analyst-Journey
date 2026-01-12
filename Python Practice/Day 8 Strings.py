# ==========================
# Day 1 - String DSA Problems
# ==========================

# 1. Check if a String is Palindrome
s = "madam"
i = 0
j = len(s) - 1
is_palindrome = True

while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")


# 2. Reverse a String
s = "python"
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Reversed String:", rev)


# 3. Count Vowels in a String
s = "education"
vowels = 0

for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        vowels += 1

print("Vowel Count:", vowels)


# 4. Remove Duplicate Characters from String
s = "programming"
result = ""

for i in range(len(s)):
    found = False
    for j in range(len(result)):
        if s[i] == result[j]:
            found = True
            break
    if not found:
        result += s[i]

print("After Removing Duplicates:", result)


# 5. Count Words in a String
s = "Python is very easy"
word_count = 1

for i in range(len(s)):
    if s[i] == ' ':
        word_count += 1

print("Word Count:", word_count)

