list_with_nums = input().split()
opposite_nums = []

for number in list_with_nums:
    current_num = -int(number)
    opposite_nums.append(current_num)

print(opposite_nums)