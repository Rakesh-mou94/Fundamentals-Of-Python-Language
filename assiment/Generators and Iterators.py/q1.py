#  Write a generator function that generates the first 10 even numbers.
def generate_even():
    count = 0
    num = 2
    
    while count < 10:
        yield num
        num += 2
        count += 1

# Using the generator
for value in generate_even():
    print(value)
