# Write a Python program to calculate grades based on percentage using
# if-else ladder

mark = int(input("Enter your mark here: "))

if 90 <= mark <= 100:
    print("A+")
elif 80 <= mark <= 89:
    print("A")
elif 70 <= mark <= 79:
    print("B")
elif 0 <= mark <= 69:
    print("C")
else:
    print("Invalid mark")

