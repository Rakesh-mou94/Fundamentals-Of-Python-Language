#Write a Python program to check if a person is eligible to donate blood nested if using.
# Practical Example 8: Blood Donation Eligibility using Nested If

age = int(input("Enter your age: "))
weight = int(input("Enter your weight (in kg): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible: Weight must be at least 50 kg.")
else:
    print("You are not eligible: Age must be at least 18 years.")

