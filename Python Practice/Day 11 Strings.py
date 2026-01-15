# =====================================
# Day 4 - DSA Problems (56 to 58)
# =====================================

# 56. Find the Longest Word in a Sentence (DSA Style)
s = input("Enter a sentence: ")

max_len = 0
longest_word = ""
current_word = ""

for i in range(len(s)):
    if s[i] != ' ':
        current_word += s[i]
    else:
        if len(current_word) > max_len:
            max_len = len(current_word)
            longest_word = current_word
        current_word = ""

# Check the last word
if len(current_word) > max_len:
    longest_word = current_word

print("Longest Word:", longest_word)


# 57. Count Words in a String (DSA Style)
s = input("\nEnter a sentence to count words: ")

count = 1
for i in range(len(s)):
    if s[i] == ' ':
        count += 1

print("Total Words:", count)


# 58. Replace Spaces with Special Character (DSA Style)
s = input("\nEnter a sentence to replace spaces: ")
result = ""

for i in range(len(s)):
    if s[i] == ' ':
        result += '@'
    else:
        result += s[i]

print("After Replacing Spaces:", result)
