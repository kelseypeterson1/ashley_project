import random

# Generate 500 random numbers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(500)]

# Write the random numbers to a text file, each on a new line
with open('random_numbers.txt', 'w') as file:
    for number in random_numbers:
        file.write(f'{number}\n')

print('500 random numbers have been saved to random_numbers.txt')