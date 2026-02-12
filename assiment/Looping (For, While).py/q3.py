#Write a Python program to find a specific string in the list using a simple for loop and if condition.
List1 = ['apple', 'banana', 'mango']
search_item = input("Enter fruit to search: ")

found = False

for item in List1:
    if item == search_item:
        found = True
        break

if found:
    print(search_item, "is found in the list.")
else:
    print(search_item, "is not found in the list.")
