factor = int(input())
count = int(input())

list_with_nums = []

for i in range(1, count + 1):
    list_with_nums.append(factor * i)

print(list_with_nums)