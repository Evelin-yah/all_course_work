list_of_nums = input().split()
rounded = []

for num in list_of_nums:
    rounded.append(round(float(num)))

print(rounded)