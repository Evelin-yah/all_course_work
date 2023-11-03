def sum_numbers(a, b):
     return a+b
def subtract_numbers(num1, num2):
    return num1-num2

def add_and_subtract(first, second, third):
    sum_of_numbers = sum_numbers(first, second)
    final_result = subtract_numbers(sum_of_numbers, third)
    return final_result
first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))