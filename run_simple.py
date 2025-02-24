with open('test_numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
i = 0

final_binary_results = []
for i, num in enumerate(numbers):
    num = numbers[i]
    binary: int = 0 if (num // 10 + num % 10) % 2 == 0 else 1    
    final_binary_results.append(binary)

print(final_binary_results)

with open('results.txt', 'w') as output_file:
    output_file.write('\n'.join(map(str, final_binary_results)))