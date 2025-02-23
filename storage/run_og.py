from typing import Optional

# Read the random numbers from the text file
with open('test_numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    
final_answers: list[int] = []

def prior_next_digit_seven_check(prior_num: Optional[int], next_num: Optional[int], invert_binary: bool) -> bool:
    return not invert_binary if '7' in str(prior_num) or '7' in str(next_num) else invert_binary

def seven_x_seven_check(prior_num_first_digit: Optional[int], first_digit: Optional[int], second_digit: Optional[int], prior_num_second_digit: Optional[int], invert_binary: bool) -> bool:
    if first_digit == 7:
        if prior_num_first_digit == 7:
            invert_binary = not invert_binary
    if second_digit == 7:
        if prior_num_second_digit == 7:
            invert_binary = not invert_binary
    return invert_binary

for i, num in enumerate(numbers):
    first_digit = num // 10  # Integer division to get the first digit
    second_digit = num % 10 
    prior_num: Optional[int] = numbers[i-1] if i > 0 else None
    prior_num_first_digit: Optional[int] = prior_num // 10 if prior_num is not None else None
    prior_num_second_digit: Optional[int] = prior_num % 10 if prior_num is not None else None
    next_num: Optional[int] = numbers[i+1] if i < len(numbers) - 1 else None
    next_num_second_digit: Optional[int] = next_num % 10 if next_num is not None else None
    next_num_first_digit: Optional[int] = next_num // 10 if next_num is not None else None

    binary: int = 0 if (first_digit + second_digit) % 2 == 0 else 1
    
    invert_binary: bool = False
    invert_binary = prior_next_digit_seven_check(prior_num_second_digit, next_num_first_digit, invert_binary)
    invert_binary = seven_x_seven_check(prior_num_first_digit, first_digit, second_digit, prior_num_second_digit, invert_binary)
            
    final_binary: int = binary if not invert_binary else 0 if binary == 1 else 1
    
    final_answers.append(final_binary)
    


with open('results.txt', 'w') as output_file:
    output_file.write('\n'.join(map(str, final_answers)))

print('Results have been saved to results.txt')
