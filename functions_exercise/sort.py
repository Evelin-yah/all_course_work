def sort_numbers(nums): return sorted(nums)

num_as_string = input().split()
numbers = [int(i) for i in num_as_string]

print(list(sort_numbers(numbers)))
