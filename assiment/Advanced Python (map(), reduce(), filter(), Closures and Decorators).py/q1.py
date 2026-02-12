# Write a Python program to apply the map() function to square a list of numbers.
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to square a number
def square(n):
    return n * n

# Apply map() function
squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
