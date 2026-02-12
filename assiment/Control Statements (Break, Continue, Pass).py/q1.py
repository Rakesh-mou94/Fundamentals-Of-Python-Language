# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    if fruit == 'banana':
        print("Banana found! Stopping the loop.")
        break
    print(fruit)
