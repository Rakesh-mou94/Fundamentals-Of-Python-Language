# Write a Python program to demonstrate string slicing.
text = "PythonProgramming"

print("Original String:", text)

# 1️⃣ Slice first 6 characters
print("First 6 characters:", text[:6])

# 2️⃣ Slice from index 2 to 8
print("Index 2 to 7:", text[2:8])

# 3️⃣ Slice from index 5 to end
print("From index 5 to end:", text[5:])

# 4️⃣ Slice every 2nd character
print("Every 2nd character:", text[::2])

# 5️⃣ Reverse the string
print("Reverse string:", text[::-1])

# 6️⃣ Slice last 5 characters
print("Last 5 characters:", text[-5:])

# 7️⃣ Slice from index 3 to 12 with step 3
print("Index 3 to 12 with step 3:", text[3:13:3])

