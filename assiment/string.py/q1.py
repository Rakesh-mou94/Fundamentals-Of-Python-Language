# Write a Python program that manipulates and prints strings using various string methods.
text = "  python Programming  "

print("Original string:", text)

# 1️⃣ Convert to uppercase
print("Uppercase:", text.upper())

# 2️⃣ Convert to lowercase
print("Lowercase:", text.lower())

# 3️⃣ Remove leading and trailing spaces
print("Stripped:", text.strip())

# 4️⃣ Capitalize first letter
print("Capitalized:", text.capitalize())

# 5️⃣ Title case (first letter of each word capitalized)
print("Title Case:", text.title())

# 6️⃣ Count occurrence of a substring
print("Count of 'g':", text.count('g'))

# 7️⃣ Replace substring
print("Replace 'Python' with 'Java':", text.replace("python", "Java"))

# 8️⃣ Check if string starts with 'py'
print("Starts with 'py':", text.strip().startswith("py"))

# 9️⃣ Check if string ends with 'ing'
print("Ends with 'ing':", text.strip().endswith("ing"))

# 1️⃣0️⃣ Split string into a list
print("Split:", text.strip().split())

# 1️⃣1️⃣ Join a list of words into a string
words = ['Python', 'is', 'fun']
print("Join words:", ' '.join(words))

# 1️⃣2️⃣ Find index of a substring
print("Index of 'Programming':", text.find('Programming'))
