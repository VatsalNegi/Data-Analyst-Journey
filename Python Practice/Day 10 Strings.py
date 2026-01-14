# =====================================
# Day 3 - DSA Problems (51 to 55)
# =====================================

# 51. FizzBuzz (DSA Style)
n = int(input("Enter a number for FizzBuzz: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 52. Check if Substring Exists (DSA Style)
s = input("\nEnter main string: ")
sub = input("Enter substring: ")

found = False

for i in range(len(s) - len(sub) + 1):
    match = True
    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break
    if match:
        found = True
        break

if found:
    print("Substring Found")
else:
    print("Substring Not Found")


# 53. Reverse a String (DSA Style)
s = input("\nEnter a string to reverse: ")
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Reversed String:", rev)


# 54. Frequency of Characters (DSA Style)
s = input("\nEnter a string to count frequency: ")
visited = [False] * len(s)

for i in range(len(s)):
    if visited[i]:
        continue

    count = 1
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            visited[j] = True
            count += 1

    print(s[i], count)


# 55. Remove Duplicate Characters (DSA Style)
s = input("\nEnter a string to remove duplicates: ")
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
