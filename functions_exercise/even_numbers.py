num_as_string = input().split()

list_of_nums = []
for integer in num_as_string:
    list_of_nums.append(int(integer))

def is_even(x): return x % 2 == 0

# using filter
lis2 = list(filter(is_even, list_of_nums))

# Printing output
print(lis2)