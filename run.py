from typing import Optional

with open('test_numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
i = 0

def seven_x_seven_check(prior_num_first_digit: Optional[int], first_digit: Optional[int], second_digit: Optional[int], prior_num_second_digit: Optional[int]) -> bool:
    if first_digit == 7:
        if prior_num_first_digit == 7:
            return True
    if second_digit == 7:
        if prior_num_second_digit == 7:
            return True
    return False

## dynamically adjusting numbers list
while i < len(numbers):
    
    ## declaring variables
    num = numbers[i]
    first_digit = num // 10 
    second_digit = num % 10 
    prior_num: Optional[int] = numbers[i-1] if i > 0 else None
    prior_num_first_digit: Optional[int] = prior_num // 10 if prior_num is not None else None
    prior_num_second_digit: Optional[int] = prior_num % 10 if prior_num is not None else None
    next_num: Optional[int] = numbers[i+1] if i < len(numbers) - 1 else None
    next_num_second_digit: Optional[int] = next_num % 10 if next_num is not None else None
    next_num_first_digit: Optional[int] = next_num // 10 if next_num is not None else None
    
    ## running checks
    add_one_to_second_digit: bool = seven_x_seven_check(prior_num_first_digit, first_digit, second_digit, prior_num_second_digit)
    if add_one_to_second_digit:
        numbers[i] = (first_digit * 10) + (second_digit + 1)
    i += 1
    
def return_binary(first_digit, second_digit, invert_binary: bool) -> int:
    original_binary: int = 0 if (first_digit + second_digit) % 2 == 0 else 1    
    if invert_binary:
        return 0 if original_binary == 1 else 1
    else:
        return original_binary
    
def palindrome_check(prior_num_first_digit: Optional[int], prior_num_second_digit: Optional[int], next_num_second_digit: Optional[int], next_num_first_digit: Optional[int], invert_binary: bool) -> bool:
    if prior_num_first_digit == next_num_second_digit and prior_num_second_digit == next_num_first_digit:
        ##palindrome identified
        return not invert_binary
    

def prior_or_next_digit_seven_check(prior_num: Optional[int], next_num: Optional[int], invert_binary: bool) -> bool:
    return not invert_binary if '7' in str(prior_num) or '7' in str(next_num) else invert_binary

def is_69(num: int, invert_binary: bool) -> bool:
    return not invert_binary if num == '69' else invert_binary

## finding and potentially inverting binary results
final_binary_results = []
for i, num in enumerate(numbers):
    
    ## declaring variables
    num = numbers[i]
    first_digit = num // 10  # Integer division to get the first digit
    second_digit = num % 10 
    prior_num: Optional[int] = numbers[i-1] if i > 0 else None
    prior_num_first_digit: Optional[int] = prior_num // 10 if prior_num is not None else None
    prior_num_second_digit: Optional[int] = prior_num % 10 if prior_num is not None else None
    next_num: Optional[int] = numbers[i+1] if i < len(numbers) - 1 else None
    next_num_second_digit: Optional[int] = next_num % 10 if next_num is not None else None
    next_num_first_digit: Optional[int] = next_num // 10 if next_num is not None else None
    
    ## running checks
    invert_binary: bool = False
    invert_binary = prior_or_next_digit_seven_check(prior_num_second_digit, next_num_first_digit, invert_binary)
    invert_binary = palindrome_check(prior_num_first_digit, prior_num_second_digit, next_num_second_digit, next_num_first_digit, invert_binary)
    invert_binary = is_69(num, invert_binary)
    binary: int = return_binary(num // 10, num % 10, invert_binary)
    final_binary_results.append(binary)

print(final_binary_results)

with open('results.txt', 'w') as output_file:
    output_file.write('\n'.join(map(str, final_binary_results)))