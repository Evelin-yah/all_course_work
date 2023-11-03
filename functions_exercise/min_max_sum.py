def sort_and_sum(nums):
    return [min(nums), max(nums), sum(nums)]

num_as_string = input().split()
list_of_numbers = [int(i) for i in num_as_string]

result = sort_and_sum(list_of_numbers)

print(f'The minimum number is {result[0]}')
print(f'The maximum number is {result[1]}')
print(f'The sum number is: {result[2]}')