
def sum_odd_and_even(nums_as_string):
    odd_sum = 0
    even_sum = 0
    for char in num_as_string:
        current_char = int(char)
        if current_char % 2 == 0:
            even_sum += current_char
        else:
            odd_sum += current_char
    return [odd_sum, even_sum]

num_as_string = input()

result = sum_odd_and_even(num_as_string)

print(f'Odd sum = {result[0]}, Even sum = {result[1]}')