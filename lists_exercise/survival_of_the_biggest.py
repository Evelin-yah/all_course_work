num_list = input().split()
nums_to_remove = int(input())
list_of_ints = []

for char in num_list:
    list_of_ints.append(int(char))

for i in range(nums_to_remove):
    list_of_ints.remove(min(list_of_ints))

print(*list_of_ints, sep =(', '))